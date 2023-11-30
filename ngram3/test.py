import nltk
from nltk.collocations import BigramAssocMeasures, BigramCollocationFinder
from nltk.util import ngrams
# สร้างข้อความตัวอย่าง
text = "This is an example sentence containing bigrams"

# แยกคำในข้อความเป็นโทเค็น (tokens)
tokens = nltk.word_tokenize(text)

# สร้าง bigrams
bigrams = nltk.bigrams(tokens)
bigrams2 = ngrams(tokens, 2)
print(list(bigrams))
print(list(bigrams2))
# สร้าง BigramCollocationFinder object จาก bigrams
finder = BigramCollocationFinder.from_documents([bigrams])
