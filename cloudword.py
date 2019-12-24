import os
import pandas as pd
import nltk
import common
import matplotlib.pyplot as plt

from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from common import more_stops
from wordcloud import WordCloud


def scan_dir(dir_name):
    """
    scan directory
    """
    for root, dirs, files in os.walk(dir_name):
        root_folder = root.split('\\')[-1]
        if root_folder != common.parent_folder[1:]:
            folders_list.append(root_folder)
        for file_name in files:
            read_file_df(os.path.join(root, file_name))


def read_file_df(file_name):
    """
    read file and append into a dataframe
    """
    df = pd.read_csv(file_name, sep="|", header=None, encoding="ISO-8859–1")
    df.columns = ['subtitle', 'category']
    df_list.append(df)


folders_list=[]
df_list = []
project_root = os.path.dirname(__file__)
directory = project_root + "\\" + common.parent_folder
scan_dir(directory)
df = pd.concat(df_list, axis=0, ignore_index=True)  # axis = 0 concatenate row wise
nltk.download('punkt')
nltk.download("stopwords")
#generate cloudword for every category we have
for category in folders_list:
    print ("Generating wordcloud for ", category)
    category_df = df[df.category == category]
    subtitles = category_df.subtitle.str.cat(sep='|')
    tk = TweetTokenizer()
    tokens = tk.tokenize(subtitles)
    stop_words = set(stopwords.words('english'))
    subtitle_text = [w for w in tokens if not w in stop_words]
    subtitle_text = more_stops(subtitle_text)
    frequency_dist = nltk.FreqDist(subtitle_text)
    sorted(frequency_dist, key=frequency_dist.__getitem__, reverse=True)

    text = category_df.subtitle.values
    wordcloud = WordCloud(
        font_path="verdana",
        width=3200,
        height=1600,
        max_words=120,
        background_color="white",
        stopwords=stop_words
    ).generate_from_frequencies(frequency_dist)

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    # plt.savefig(directory + '\\movie_analysis.png')
    plt.show()
    plt.close()
