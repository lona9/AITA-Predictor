import praw
from dotenv import load_dotenv
import os
from psaw import PushshiftAPI
import datetime as dt
import pandas as pd

## load env file
load_dotenv()
## initiate reddit and pushshift instance
reddit = praw.Reddit(client_id = os.getenv('client_id'),
client_secret = os.getenv('client_secret'), user_agent = os.getenv('user_agent'))
push = PushshiftAPI(reddit)
print("instance initiated...")

## parameters for fetching
before_period = int(dt.datetime(2022,1,1).timestamp())

print("fetching posts...")
test = list(push.search_submissions(before=before_period,
                                    subreddit='AmITheAsshole',
                                    filter=['url','author', 'title', 'subreddit'],
                                    limit=100000,
                                    stickied=False))

print("posts fetched...")
posts = []

print("extracting info...")
for post in test:
    posts.append([post.title, post.id, post.score, post.upvote_ratio, post.url, post.num_comments, post.selftext,
                dt.datetime.fromtimestamp(post.created_utc), post.edited, post.link_flair_text, post.over_18])

print("creating dataframe...")
posts = pd.DataFrame(posts,columns=['title', 'id', 'score', 'upvote_ratio', 'url', 'num_comments', 'body',
                                    'created', 'edited', 'verdict', 'over_18'])
print("creating csv file...")
posts.to_csv("reddit_posts.csv", index=False)

print("done!")
