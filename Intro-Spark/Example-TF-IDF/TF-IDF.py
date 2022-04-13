from pyspark import SparkConf, SparkContext
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.feature import IDF


conf = SparkConf().setMaster("local[*]").setAppName("SparkTFIDF")
sc = SparkContext(conf = conf)

# Use Lambda for seperation
mainData = sc.textFile("wikipediaCorpus.tsv")
emptyLines = mainData.map(lambda x: x.split("\t"))
CorpusDocuments = emptyLines.map(lambda x: x[3].split(" "))

# Data manipulation for data storage:
documentNames = emptyLines.map(lambda x: x[1])

# Hash the words for frequencies
hashingTF = HashingTF(100000)  #100K this is save for avoiding large memory consumption
tf = hashingTF.transform(CorpusDocuments)

# it will be RDD objects
# TF*IDF in the document
tf.cache()
idf = IDF(minDocFreq=2).fit(tf)
tfidf = idf.transform(tf)

# Please try your query below related to your interest

# hash value maps to by finding the
# index a sparse vector from HashingTF
wordTF = hashingTF.transform(["Electronics"])
wordHashValue = int(wordTF.indices[0])

# Now we will extract the TF*IDF score for the query hash value into
# a new RDD for each document:
analysisRelevance = tfidf.map(lambda x: x[wordHashValue])

#
zippedResults = analysisRelevance.zip(documentNames)
#
print("analysis output for your query is the following:")
print(zippedResults.max())
