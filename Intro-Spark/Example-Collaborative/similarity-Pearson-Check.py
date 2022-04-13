from pyspark import SparkConf, SparkContext
import numpy as np
import sys

conf = SparkConf().setMaster("local").setAppName("findcorr")
sc = SparkContext(conf = conf)
sc.setLogLevel("ERROR")

def makePairs(userRatings):
    ratings = userRatings[1]
    (movie1, rating1) = ratings[0]
    (movie2, rating2) = ratings[1]
    return ((movie1, movie2), (rating1, rating2))

def filterDuplicates(userRatings):
    ratings = userRatings[1]
    (movie1, rating1) = ratings[0]
    (movie2, rating2) = ratings[1]
    return movie1 < movie2

def findCorr(pair):
#finds Pearson Correlation coefficient.
    xlist=[]
    ylist=[]
    for x,y in pair:
        xlist.append(x)
        ylist.append(y)
    corr = np.corrcoef(xlist,ylist)
    return corr[0][1]

def loadMovieNames():
    movieNames = {}
    with open("ml-100k/u.ITEM", encoding = "latin-1") as f:
        for line in f:
            fields = line.split('|')
            movieNames[int(fields[0])] = fields[1]
    return movieNames
print("\n Loading movie archive")
nameDict = loadMovieNames()

data = sc.textFile("ml-100k/u.data")
ratings = data.map(lambda x: x.split()).map(lambda x: (int(x[0]), (int(x[1]), float(x[2]))))
joinedRatings = ratings.join(ratings)
uniqueJoinedRatings = joinedRatings.filter(filterDuplicates)
moviePairs = uniqueJoinedRatings.map(makePairs)
moviePairRatings = moviePairs.groupByKey()
#getting filmID
filmID = int(sys.argv[1])
#getting rdds ((filmID, pairedfilm),((rating11, rating21),(rating12, rating22), ..... (rating1n, rating2n)))
selectedFilmPairs = moviePairRatings.filter(lambda x: x[0][0] == filmID and len(x[1]) >= 50)
#getting correlation rdds ((filmID, pairedfilm), corrcoef)
corrPairs = selectedFilmPairs.mapValues(findCorr)
#getting most correlated films with filmID
top10 = corrPairs.map(lambda x: (x[1], x[0])).sortByKey(ascending = False).take(10)
top10 = list(top10)
#printing with film names
for i in top10:
    print(nameDict[int(i[1][0])], nameDict[int(i[1][1])], "with correlation =", i[0])
