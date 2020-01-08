from sentiment_analysis import computeTweets

#takes user input to open specified file
tweetFile = input("what tweet file would you like to use?: ")
keyWordsFile = input("what keywords file would you like to use?: ")

#takes the list of tuples and unpacks each item in the list of tuples and adding a string before them to clarify for user comprehension
bigList = (computeTweets(tweetFile, keyWordsFile))
print("the respective average happiness score, number of keywords tweets, and number of normal tweets for each respective timezone based on the files passed in are......")
pacificList = bigList[0]
print("pacific average happiness: ", pacificList[0])
print("pacific keyword tweet count: ", pacificList[1])
print("pacific tweet count: ", pacificList[2])
mountainList = bigList[1]
print("mountain average happiness: ", mountainList[0])
print("mountain keyword tweet count: ", mountainList[1])
print("mountain tweet count: ", mountainList[2])
centralList = bigList[2]
print("central average happiness: ", centralList[0])
print("central keyword tweet count: ", centralList[1])
print("central tweet count: ", centralList[2])
easternList = bigList[3]
print("eastern average happiness: ", easternList[0])
print("eastern keyword tweet count: ", easternList[1])
print("eastern tweet count: ", easternList[2])
