import nltk
import requests

# Downloading the dictionary file
# url = 'https://gist.githubusercontent.com/deekayen/4148741/raw/9522857cdbe197c207b61ec9957c9d1f3e3ff462/1.txt'
# req = requests.get(url)

# dictionary = set(req.text.lower().split('\n')) # split() =>splits the sentence into a list of words

with open('dictionary.txt', 'r') as f:
    dictionary = f.read()
dictionary = dictionary.split('\n')

def correct_word(word):
    new_words = []
    for w in dictionary:
        distance = nltk.edit_distance(word, w)
        # print(f"{word} vs {w}= {distance}")
        if distance <= 1:
            new_words.append(w)
    if len(new_words) == 0:
        return word
    else:
        new_word = min(new_words, key=lambda w: nltk.edit_distance(word, w))
        print(f"{word} can be replaced by ('{new_word}',{nltk.edit_distance(word, new_word)})")
        return new_word


sentence = "I opan a bax ant reed a leter"
corrected_sentence = ' '.join(correct_word(word) for word in sentence.split())

print("Mispelled sentence is  >> ", sentence)
print("New sentence is        >> ", corrected_sentence)