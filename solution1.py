import string
from nltk import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

porter = PorterStemmer()
stop_words = stopwords.words('english')
curse_words = ["bitch", "fuck"]

# load data
filename = 'sample.txt'
file = open(filename, 'r')
text = file.read()
file.close()
sentences = text.split("\n")
file = open("answer.txt", "w")
print(sentences)
for sentence in sentences:
    # split into words
    tokens = word_tokenize(sentence)
    # convert to lower case
    tokens = [w.lower() for w in tokens]
    # remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    # remove remaining tokens that are not alphabetic
    words = [word for word in stripped if word.isalpha()]
    # filter out stop words
    words = [w for w in words if not w in stop_words]

    stemmed = [porter.stem(word) for word in words]
    total = len(stemmed)
    count = 0
    for w in stemmed:
        if w in curse_words:
            count+=1
    file.write(str(count/total) + "\n")

file.close()


