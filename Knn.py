import os
import pandas as pd
import nltk
import common
import seaborn as sn
import matplotlib.pyplot as plt

from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from common import more_stops


def fill_df(df, the_file):
    """

  :param the_file:
  :return:
  """
    df.append(the_file)


def scan_dir(dir_name):
    for root, dirs, files in os.walk(dir_name):
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

# df = pd.DataFrame(columns=['subtitle','category'])
df = pd.DataFrame()
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


classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
df_cm = pd.DataFrame(cm, range(7), range(7))
sn.set(font_scale=1.4)
fig = plt.figure(figsize=(10, 7))
sn.heatmap(df_cm, annot=True, annot_kws={"size": 16})
plt.show()
