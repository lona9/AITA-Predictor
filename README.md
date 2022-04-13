# DATA SCIENTIST CAPSTONE PROJECT
-----
### Introduction

This project was created for the Udacity Data Scientist Nanodegree Capstone Project, which is the final submission for graduation. In this project, an ELT Pipeline was built to obtain Reddit posts information from a particular subreddit: r/AmITheAsshole. This information was analyzed to look for trends and other descriptive statistics from the subreddit, and the body from posts was used to build a Machine Learning model that could classify each post in one of the different verdicts the Reddit public gives the original poster.

-----
### Installations

The following repository requires the following libraries to run properly:
- pandas
- numpy
- plotly
- nltk
- os
- pickle
- sklearn
- wordcloud
- matplotlib
- PIL
- praw
- psaw
- dotenv
- re
- seaborn
- joblib

-----
### Files
- `AITA Predict.ipynb`: Jupyter Notebook with an overview of the project, analytics, and a model tester.
- wordclouds folder:
  - `wordcloud_builder.py`: script to create word clouds.
- model folder:
  - `model.py`: script to build and train the ML pipeline.
- reddit_scraper folder:
  - `scraper.py`: script to run the reddit scraper to fetch post information.
  - `reddit_posts.csv`: output file from the previous script with Reddit post data.

-----
### Instructions

1. To get posts information using Reddit APIs, you need to register for a Reddit application in order to obtain your client credentials and initiate an instance and fetch posts. These credentials are secret and should be saved in an .env file to avoid exposing your credentials. The fetching process takes around 2 hours to finish, running the `python reddit_scraper/scraper.py` command from the main folder. If you can't or won't get credentials, the .csv file with the posts information is available in this repo as well.

2. After fetching, run the following command: `python model/model.py` to run the Machine Learning pipeline, and it'll print the classification report of the model.

3. For a project overview, analytics and model testing, you can open the Jupyter Notebook in the main folder. The files necessary to build the word cloud images will be generated when running this notebook.

4. To create the word clouds, run the following command: `python wordclouds/wordcloud_builder.py`

-----

### Main Results
For a longer version of the results, you can check this blog post (link).
