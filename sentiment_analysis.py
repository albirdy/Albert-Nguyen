from string import punctuation

def computeTweets(tweets, keywords):
#empty list to add values to for each reigon
    pacificScore = [0,0,0]
    mountainScore = [0,0,0]
    centralScore = [0,0,0]
    easternScore = [0,0,0]

#happiness score for each reigon
    pacificHVal = 0
    mountainHval = 0
    centralHval = 0
    easternHVal = 0

#keyword tweets for each reigon
    pacificKeyWords = 0
    mountainKeyWords = 0
    centralKeyWords = 0
    easternKeyWords = 0

#try loop to throw error if there is an issue with the file
    try:

        #opens tweet file and keyword file
        tweets = open(tweets, "r", encoding="utf-8")
        keywords = open(keywords, "r", encoding="utf-8")

        #empty list for each keyword and heir values
        keywordList = []
        keywordValList = []

        #loop going through each line in keyword file
        for word in keywords:

            #breaking the keyword list into a 2 lists with keywords in one and respective values in the maching index for the other list
            word = word.split(",")
            keywordList.append(word[0])
            keywordValList.append(word[1])

        #loop going through each line in keywords file
        for line in tweets:

            #putting variable declaration for hVal and keywordCount here to reset each variable for each line
            hVal = 0
            keywordCount = 0
            tweetList = tweetCleaner(line)

            #getting float values for longitude and latitude
            lat = tweetList[0].strip('[], ')
            long = tweetList[1].strip('[], ')
            lat = float(lat)
            long = float(long)
            timeZone = timeZoneCalculator(lat, long)

            #going through each word in each tweet and checking then going through each work in keyworfile to find any matches
            for i in tweetList:
                for x in range(len(keywordList)):
                    if i == keywordList[x]:
                        hVal = hVal + int(keywordValList[x])
                        keywordCount = keywordCount + 1

            #to avoid dividing by 0 and then calculating happiness score for each tweet
            if keywordCount != 0:
                hScore = hVal/keywordCount


            #adding respective values based on reigon and adding 1 to count how many keyword tweets and normal tweets
            if timeZone == "pacific":
                pacificScore[2] = pacificScore[2] + 1

            if timeZone == "pacific" and keywordCount != 0:
                pacificHVal = pacificHVal+hScore
                pacificKeyWords = pacificKeyWords + 1

            if timeZone == "mountain":
                mountainScore[2] = mountainScore[2] + 1

            if timeZone == "mountain" and keywordCount != 0:
                mountainHval = mountainHval + hScore
                mountainKeyWords = mountainKeyWords + 1

            if timeZone == "central":
                centralScore[2] = centralScore[2]+1

            if timeZone == "central" and keywordCount != 0:
                centralHval = centralHval + hScore
                centralKeyWords = centralKeyWords + 1

            if timeZone == "eastern":
                easternScore[2] = easternScore[2]+1

            if timeZone == "eastern" and keywordCount != 0:
                easternHVal = easternHVal + hScore
                easternKeyWords = easternKeyWords + 1

        #adding each values to the correct spot on the list
        pacificScore[1] = pacificKeyWords
        mountainScore[1] = mountainKeyWords
        centralScore[1] = centralKeyWords
        easternScore[1] = easternKeyWords

        #to avoid dividing by zero then calculating average for each reigon
        if pacificScore[1] != 0:
            pacificScore[0] = pacificHVal/pacificScore[1]
        if mountainScore[1] != 0:
            mountainScore[0] = mountainHval/mountainScore[1]
        if centralScore[1] != 0:
            centralScore[0] = centralHval/centralScore[1]
        if easternScore[1] != 0:
            easternScore[0] = easternHVal/easternScore[1]

        #closing files
        tweets.close()
        keywords.close()

        #returns tuples
        return[tuple(pacificScore), tuple(mountainScore), tuple(centralScore), tuple(easternScore)]

    #returns empty list if there is an ioerror
    except IOError:
        return[]

#tweet cleaning function that strips punctuation and lowerscases all words
def tweetCleaner(tweet):
    tweetList = tweet.split()
    for i in range (2, len(tweetList)):
        tweetList[i] = tweetList[i].strip(punctuation).lower()
    return tweetList

#function that determines which reigon the tweet is from
def timeZoneCalculator(cordLat, cordLong):
    if cordLat > 24.660845 and cordLat < 49.189787:
        if -115.236428 > cordLong > -125.242264:
            return "pacific"

        elif -101.998892 > cordLong > -115.236428:
            return "mountain"

        elif -87.518395 > cordLong > -101.998892:
            return "central"

        elif -67.444574 > cordLong > -87.518395:
            return "eastern"
    return 0





