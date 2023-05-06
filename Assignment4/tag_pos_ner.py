from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags
import re
from termcolor import colored

with open('text.txt', 'r') as f:
    paragraphs = f.read()

def convert_POS_NER(paragraphs):
    # Tokenize the paragraph into words
    words = word_tokenize(paragraphs)
    # Perform POS tagging on the words
    pos_tags = pos_tag(words)

    # Display POS tags
    print("\nPOS: ")
    for word, pos in pos_tags:
        if pos.startswith('NN'):
            print(colored(word, 'red'), end=' ')
        elif pos.startswith('VB'):
            print(colored(word, 'green'), end=' ')
        else:
            print(word, end=' ')

    # Perform NER on the POS tagged words
    ne_tags = ne_chunk(pos_tags)
    
    # Convert the NER tags to IOB format
    iob_tags = tree2conlltags(ne_tags)

    # Display NER tags
    print("\n\nNER: ")
    for iob_tag in iob_tags:
        word, pos, ne = iob_tag
        if ne == 'B-PERSON':
            print(colored(word, 'yellow'), end=' ')
        elif ne == 'B-ORGANIZATION':
            print(colored(word, 'blue'), end=' ')
        elif ne == 'B-GPE':
            print(colored(word, 'green'), end=' ')
        else:
            print(word, end=' ')
    print()

convert_POS_NER(paragraphs)