import re
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.collocations import BigramCollocationFinder
import operator

n = 2
test_sentence = "I love X"
sentence = ["I love you!","I love mom.","I love you so much","I love dog.","I love mom so much.","John love you so bad."]

tokens_list = []
for s in sentence:
    tokens = word_tokenize(s.lower())
    tokens = [toks for toks in tokens if re.match("^[a-zA-Z0-9]+$",toks)]
    # print(tokens)
    tokens_list.extend(tokens)
# print(tokens_list)
bigrams = ngrams(tokens_list, n)
print()
# print("Biagrams = ",list(bigrams))
bigram_list = []
for bigram in list(bigrams):
    if bigram[0] =='love'  :
        bigram_list.append(bigram)
    
# print("Biagram_list = ",(bigram_list))


finder = BigramCollocationFinder.from_documents(bigram_list)
bigram_measures = nltk.collocations.BigramAssocMeasures()
scored_bigrams = finder.score_ngrams(bigram_measures.raw_freq)


total_count = sum(frequency for bigram, frequency in scored_bigrams)
# print(total_count)
bigram_prob = {}
for bigram, frequency in scored_bigrams:
    if bigram[0] == "love":
        bigram_prob[bigram] = frequency / total_count

print("bigram prob:", bigram_prob)

# replace 'X' in test_sentence with the most probable word that follows 'I love'
prefix = "I love "
suffixes = [bi[1] for bi in scored_bigrams ]
most_probable_suffix = [bi for bi in scored_bigrams if bi[1] >= max(suffixes)]
result_sentence = test_sentence.replace("X", most_probable_suffix[0][0][1])
print("I love X:", result_sentence)
