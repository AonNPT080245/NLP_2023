import re
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

text = "Cherry blossom represents the nature of life and a season of renewal in Japanese culture. Last year, the season attracted nearly five million people and boosted the economy by about $2.7 billion, according to figures from Bloomberg."

# word_tokenize เป็นโมดูลที่แยกข้อความออกเป็นรายการคำหรือโทเค็น
tokens = word_tokenize(text.lower())

def is_alphaNumeric(token,unigrams_list):
    if re.match('^[+-]?\d+\.+\d+$',token):
        decimal = re.findall('\d', token)
        unigrams_list = [unigrams_list.append(num) for num in list(decimal)]
    elif re.match('^[a-zA-Z0-9]+$', token) :
        unigrams_list.append(token)

unigrams = ngrams(tokens, n=1)

# unigrams_list = [unigram[0] for unigram in unigrams if is_alphanumeric(unigram[0])]
unigrams_list = []
for unigram in unigrams:
    is_alphaNumeric(unigram[0],unigrams_list)
     

Unigram = ['cherry', 'blossom', 'represents', 'the', 'nature', 'of', 'life', 'and', 'a', 'season', 'of', 'renewal', 'in', 
'japanese', 'culture', 'last', 'year', 'the', 'season', 'attracted', 'nearly', 'five', 'million', 'people', 'and', 'boosted', 
'the', 'economy', 'by', 'about', '2', '7', 'billion', 'according', 'to', 'figures', 'from', 'bloomberg']

# unig_list = [" ".join(unigram) for unigram in list(unig)]
# unigrams_list = []
# for unigram in unig:
#     unigrams_list.append(unigram[0])

print(unigrams_list)
print()
print(Unigram)
print(unigrams_list == Unigram)
