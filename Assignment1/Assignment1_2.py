from nltk.tokenize  import sent_tokenize,word_tokenize
from nltk.probability  import FreqDist
from nltk.corpus  import stopwords
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import re
import requests
from bs4 import BeautifulSoup

########## send a GET request to the web page
url = 'https://www.bbc.com/news/entertainment-arts-60939316'
response = requests.get(url)

########## parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

########## find the headline and article text elements
headline = soup.find('h1', class_='ssrcss-15xko80-StyledHeading e1fj1fc10').text.strip()
article_text = ''

for paragraph in soup.find_all('div', class_='ssrcss-7uxr49-RichTextContainer e5tfeyi1'):
    if(paragraph.find('p', class_='ssrcss-1q0x1qg-Paragraph eq5iqo00')):
        article_text += paragraph.find('p', class_='ssrcss-1q0x1qg-Paragraph eq5iqo00').text.strip() + '\n'
        # print(paragraph.find('p', class_='ssrcss-1q0x1qg-Paragraph eq5iqo00').text)
        # print()

######### print the headline and article text
print(headline)
# print(len(article_text))
print(article_text)

####### tokenize the text and filter out stop words
####### sent_tokenize => splits the article text into sentences.
####### word_tokenize =>  splits each sentence into words.
tokens = [word.lower() for sentence in sent_tokenize(article_text) for word in word_tokenize(sentence)] 
tokens = [token for token in tokens if re.search('^[a-zA-Z]{2,}$', token) and token not in stopwords.words('english')]

# compute the frequency of each token
# create a frequency distribution of the tokens
freqD = FreqDist(tokens)

# print the number of sentences and the top 10 most frequent tokens
print(f"The number of sentences: {len(sent_tokenize(article_text))}")
for word, frequency in freqD.most_common(10):
    print(word, frequency)



