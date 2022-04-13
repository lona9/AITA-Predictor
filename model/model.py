import pandas as pd
import datetime
import numpy as np
import nltk
import re
import os
import pickle
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer

def load_dataset():
    """
    Loads the dataset and defines the feature and target variables.

    Input:
    None
    Output:
    X, y = Feature and target variables obtained from the dataframe.
    """

    #load file into dataframe
    df = pd.read_csv(os.path.join("../reddit_scraper/reddit_posts.csv"))

    #remove invalid rows
    nan = np.nan
    clean_df = df.query("body not in ['[deleted]', '[removed]'] & verdict not in ['TL;DR', 'UPDATE', @nan, 'Talk ENDED', 'Open Forum', 'Mods Needed!', 'META', 'Not enough info']")

    X = clean_df.body.values
    y = clean_df.verdict.values

    return X, y

def tokenize(text):
    """ Tokenizer function to process text data during the CountVectorizer
    step.

    Input:
    text: text values from the message column.
    Output:
    clean_tokens: tokenized text, normalized and lemmatized.
    """

    lemmatizer = WordNetLemmatizer()

    urls = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    detected_urls = re.findall(urls, text)

    for url in detected_urls:
        text = text.replace(url, "urlplaceholder")

    words = word_tokenize(text)
    stop_words = stopwords.words("english")
    words = [x for x in words if x not in stop_words]

    clean_tokens = []
    for word in words:
        clean_token = lemmatizer.lemmatize(word).strip().lower()
        clean_tokens.append(clean_token)

    return clean_tokens

def build_model():
    """ Builds machine learning pipeline using the body of posts, and outputting
    the verdict targets.

    Input:
    none
    Output:
    model: model using the body to predict the verdict of a post.
    """


    pipeline = Pipeline([
                ('vect', CountVectorizer(tokenizer=tokenize)),
                ('tfidf', TfidfTransformer(use_idf = True)),
                ('clf', DecisionTreeClassifier())
    ])

    parameters = {
            "clf__criterion": ["gini", "entropy"],
            "clf__min_samples_split": [10, 20]
        }

    model = GridSearchCV(pipeline, parameters, verbose = 10)

    return model

def evaluate_model(model, X_test, y_test):
    """ Uses the fitted model to predict using the test set.

    Input:
    model: previously fitted model
    X_test: X values from the test set
    y_test: y values from the test set

    Output:
    Prints the classification_report on each of the verdicts.
    """

    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

def save_model(model):
    """ Saves model into a pickle file.
    Input:
    model: finished machile learning model
    Output:
    Saved model file.
    """

    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

def main():
    print('Loading data...')
    X, y = load_dataset()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    print('Building model...')
    model = build_model()

    print('Training model...')
    model.fit(X_train, y_train)
    print(f"Best parameters for the model: {model.best_params_}")

    print('Evaluating model...')
    evaluate_model(model, X_test, y_test)

    print('Saving model...')
    save_model(model)

    print('Trained model saved!')

if __name__ == '__main__':
    main()
