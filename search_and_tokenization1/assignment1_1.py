from nltk.tokenize import word_tokenize
import re
from nltk.corpus import gutenberg,nps_chat
import nltk

# print(nltk.__version__)
# nltk.download('gutenberg')
moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
# for w in moby: print(w, end = '')

# # Item 1
# data1 = []
# for w in moby:
#     if(re.search("ess$",w)):
#         data1.append(w)
# mylist = list(dict.fromkeys(data1))
# print(sorted(mylist))
# print(len(mylist))

# # Item 2
# data2 = []
# for w in moby:
#     if(re.search("pen|men",w)):
#         data2.append(w)
# mylist = list(dict.fromkeys(data2)) 
# print(sorted(mylist))
# print(len(mylist))


# # Item 3
# data3 = []
# for w in moby:
#     if(re.search("^(un|pre)",w)):
#         data3.append(w)
# mylist = list(dict.fromkeys(data3)) 
# print(sorted(mylist))
# print(len(mylist))

# # Item 4
# data4 = []
# for w in moby:
#     if(re.search("^\d{2}$",w)):
#         data4.append(w)
# mylist = list(dict.fromkeys(data4))
# print(sorted(mylist))
# print(len(mylist))


# # Test 5.1
# data5 = []
# for w in moby:
#     if(re.search("^\w{4}$",w)):
#         data5.append(w)
# mylist = list(dict.fromkeys(data5))
# print(sorted(mylist))
# print(len(mylist))

# # Test 5.2
# data5 = []
# for w in moby:
#     if(len(w) == 4):
#         data5.append(w)
# mylist = list(dict.fromkeys(data5))
# print(sorted(mylist))
# print(len(mylist))

# # Test 5.3
# data5 = []
# for w in moby:
#     if(re.search("^\D{4}$",w)):
#          if(re.search("^\w{4}$",w)):
#             data5.append(w)
# mylist = list(dict.fromkeys(data5))
# print(sorted(mylist))
# print(len(mylist))

# Item 5
data5 = []
for w in moby:
    if(len(w) == 4):
        data5.append(w)
mylist = list(dict.fromkeys(data5))
print(sorted(mylist))
print(len(mylist))





