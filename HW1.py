from google.colab import drive
drive.mount('/content/drive/')

f = open("/content/drive/My Drive/tweets/20000_tweets.txt", "r")

line_count = 0
top_tweets = []
for tweet in f:
  print("### Tweet", line_count, "#####")
  print(tweet)
  
  top_tweets.append(tweet)
  line_count += 1
  if line_count >= 10:
    break
f.close(

# import any relevant libraries here
import re
# a function to tokenize text into words
def tokenize(text):
  text = re.sub('([A-Za-z]+)\s?[\'’]\s?([A-Za-z]+)', r'\1'' ’'r'\2', text)
  text = re.sub('([!.:?-])+\s', ' 'r'\1'' ', text)
  text = re.sub('wouldn\s’t', 'would n’t', text)
  text = re.sub('shouldn\s’t', 'should n’t', text)
  text = re.sub('couldn\s’t', 'could n’t', text)
  text = re.sub('won\s’t', 'wo n’t', text)
  text = re.sub('can\s’t', 'ca n’t', text)
  text = re.sub('don\s’t', 'do n’t', text)
  text = re.sub('([([])', r'\1'' ', text)
  text = re.sub('([\)\]])', ' 'r'\1', text)
  words = text.split()  
  return list(filter(None, words))

tokenized_top_tweets = [tokenize(tweet) for tweet in top_tweets]
for tokenized_tweet in tokenized_top_tweets:
  print(tokenized_tweet)

# function to clean a tweet
def clean_a_tweet(tokenized_tweet):
  tokenized_tweet = list(filter(None, tokenized_tweet))
  for i in range(len(tokenized_tweet)):
    tokenized_tweet[i] = tokenized_tweet[i].lower()
    tokenized_tweet[i] = tokenized_tweet[i].replace('...','.')
    if (len(tokenized_tweet[i]) == 1):
      tokenized_tweet[i] = re.sub('([!.:?-])', '', tokenized_tweet[i])
    if "http" in tokenized_tweet[i]:
      tokenized_tweet[i] = "URL"
    if "@" in tokenized_tweet[i]:
      tokenized_tweet[i] = "@USER"
    

  clean_tokenized_tweet = list(filter(None, tokenized_tweet))
  return(clean_tokenized_tweet)

anonymized_top_tweets = [clean_a_tweet(tokenized_tweet) for tokenized_tweet in tokenized_top_tweets]
for tokenized_tweet in anonymized_top_tweets:
  print(tokenized_tweet)


# Write your code to build top 10 unigrams and bigrams
# Hint: You can use python dictionary or collections.Counter().
file = open("/content/drive/My Drive/tweets/20000_tweets.txt", "r")

unigrams = {}
bigrams = {}

for tweet in file:
  tokenized = tokenize(tweet)
  cleaned = clean_a_tweet(tokenized)
  for i in range(len(cleaned)):
    if cleaned[i] not in unigrams:
      unigrams[cleaned[i]] = 1
    else:
      unigrams[cleaned[i]] += 1

  for i in range(len(cleaned) - 1):
    if (cleaned[i] + ' ' + cleaned[i + 1]) not in bigrams:
      bigrams[cleaned[i] + ' ' +  cleaned[i + 1]] = 1
    else:
      bigrams[cleaned[i] + ' ' +  cleaned[i + 1]] += 1

unigramsList = sorted(unigrams.items(), key=lambda kv: kv[1], reverse=True)
reverseList = sorted(unigrams.items(), key=lambda kv: kv[1])
bigramsList = sorted(bigrams.items(), key=lambda kv: kv[1], reverse=True)

print("Top 10 Unigrams")
for i in range(10):
  print(str(unigramsList[i][0]) + '\t' + str(unigramsList[i][1]))
print("\n \nTop 10 Bigrams")
for i in range(10):
  print(str(bigramsList[i][0]) + '\t' + str(bigramsList[i][1]))

# Write your code to print the frequencies of the above unigrams and bigrams
# Hint: reuse the dictionaries you built in the previous cell
uniList = ["covid", "coronavirus", "republicans", "democrats"]
biList = ["social distancing", "wear mask", "no mask", "donald trump", "joe biden"]
for word in uniList:
  print(word + '\t' + str(unigrams[word]))
for word in biList:
  print(word + '\t' + str(bigrams[word]))
