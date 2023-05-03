import re
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

text = "Cherry blossom represents the nature of life and a season of renewal in Japanese culture. Last year, the season attracted nearly five million people and boosted the economy by about $2.7 billion, according to figures from Bloomberg."

def is_alphaNumeric(token,token_list):
    if re.match('^[+-]?\d+\.+\d+$',token):
        decimal = re.findall('\d', token)
        token_list = [token_list.append(num) for num in list(decimal)]
    elif re.match('^[a-zA-Z0-9]+$', token) :
        token_list.append(token)


# word_tokenize เป็นโมดูลที่แยกข้อความออกเป็นรายการคำหรือโทเค็น
tokens = word_tokenize(text.lower())
tokens_new = []
for tok in tokens:
    is_alphaNumeric(tok,tokens_new)

unigrams = ngrams(tokens_new, n=1)
bigrams = ngrams(tokens_new, n=2)

# unigrams_list = [unigram[0] for unigram in unigrams if is_alphanumeric(unigram[0])]
unigrams_list = []
for unigram in unigrams:
    # is_alphaNumeric(unigram[0],unigrams_list)
    unigrams_list.append(unigram[0])

bigrams_list = []
for bigram in bigrams:
    bigrams_list.append(bigram)

print(f"Unigram = {unigrams_list}")
print()
print(f"The 2 -gram = {bigrams_list}")
print()
# print(f"Tokens = = {list(tokens)}")
# print()
# print(f"Tokens new = = {list(tokens_new)}")


