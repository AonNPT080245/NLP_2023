import nltk

str1 = "baby"
str2 = "ruby"

distance = nltk.edit_distance(str1, str2,substitution_cost = 2)

# print("The edit distance of {} and {} is {}".format(str1,str2,distance))
print(f"The edit distance of {str1} and {str2} is {distance}")

