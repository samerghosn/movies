import os
import pandas as pd
import nltk
import common

from nltk.corpus import stopwords
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from common import more_stops


def scan_dir(scan_dir):
    """
    Scan directory and work on files
    """
    for root, dirs, files in os.walk(scan_dir):
        for file_name in files:
            create_df_fromfile(os.path.join(root, file_name))


def create_df_fromfile(file_name):
    """
    create a dataframe from files
    """
    df_sub = pd.read_csv(file_name, sep="|", header=None, encoding="ISO-8859–1")
    df_sub.columns = ['subtitle', 'category']
    subtitle = df_sub['subtitle'][0]
    tokens = subtitle.split()
    tokens = more_stops(tokens)
    subtitle = [w for w in tokens if not w in stop_words]
    df_sub['subtitle'] = " ".join(subtitle)
    df_list.append(df_sub)


nltk.download('punkt')
nltk.download("stopwords")
# df = pd.DataFrame(columns=['subtitle','category'])
stop_words = set(stopwords.words('english'))

df_list = []
project_root = os.path.dirname(__file__)
directory = project_root + "\\" + common.parent_folder
scan_dir(directory)

df = pd.concat(df_list, axis=0, ignore_index=True)  # axis = 0 concatenate row wise

subtitles = df['subtitle'].values
y = df['category'].values

subtitles_train, subtitles_test, y_train, y_test = train_test_split(
    subtitles, y, test_size=0.25, random_state=1000)

vectorizer = CountVectorizer()
vectorizer.fit(subtitles_train)

X_train = vectorizer.transform(subtitles_train)
X_test = vectorizer.transform(subtitles_test)

classifier = LogisticRegression()
classifier.fit(X_train, y_train)
score = classifier.score(X_test, y_test)
print("Accuracy: ", score)
