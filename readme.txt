the purpose of this project is to predict the genre of the movie based on the subtitles.
data is split as learning and testing. The results are pretty good using logistics.
More subtitles should be added, this would be quite interesting to play with.

movies-source are the original movie downloaded from the internet
cleandata: remove numbers and put all text on the same line, you can always copy the content of "movies-Source" to "movies" to run cleandata more than 1 time
cloudword: generate wordlcloud for each movie category
logistic and knn : each contain algorithm implemented