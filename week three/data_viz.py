#file: data_viz.py
#author:
#desc:
#created:
''' this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''
##import twitter_data_code_along
from wordcloud import WordCloud
import json
from textblob import TextBlob
import matplotlib.pyplot as plt


#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
#create a list for polarity and subjectivity.
polarityList = []

subjectivityList = []

# Continue your program below!
for tweet in tweetData:
    tweetTB = TextBlob(tweet['text'])

    polarityList.append(tweetTB.polarity)
    subjectivityList.append(tweetTB.subjectivity)

total = 0
for i in polarityList:
        total += i
amount = len(polarityList)
averagepolarity = total/amount
print (averagepolarity)

total = 0
for i in subjectivityList:
    total += i
amount = len(subjectivityList)
averagesubjectivity = total/amount
print (averagesubjectivity)

import matplotlib.pyplot as plt

someList = []
plt.hist(polarityList, bins=[-1, -0.5, 0.0, 0.5, 1])
plt.xlabel('polarity')
plt.ylabel('number of Items')
plt.title('Histogram of polarity')
plt.axis([-1.1, 1.1, 0, 100])
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt


someList = []
plt.hist(subjectivityList, bins=[-1, -0.5, 0.0, 0.5, 1])
plt.xlabel('subjectivity')
plt.ylabel('number of Items')
plt.title('Histogram of subjectivity')
plt.axis([-1.1, 1.1, 0, 100])
plt.grid(True)
plt.show()

polarity = []
subjectivityList = []

a_big_word = ""

for j in range(70):
    a_big_word += ' ' + tweet['text']
td = TextBlob(a_big_word)
list1 = a_big_word.split(" ")
filterWords = {}
commonwords = ["and", "about", "the", "but", "like", "htps"]

for i in list1:
    if len (i) < 3:
        continue
    if i in commonwords:
        continue
    if not i.isalpha():
        continue
        
    filterWords[i] = td.word_counts[i]
        
print()
wordC = WordCloud().generate_from_frequencies(filterWords.items())
plt.subplot(111)
plt.imshow(wordC, interpolation='bilinear')
plt.axis('off')
plt.figure(1)
plt.show()

    
    


print(a_big_word)
# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
    

# Textblob sample:
##tb = TextBlob("You are a brilliant computer scientist.")
##print(tb.polarity)
