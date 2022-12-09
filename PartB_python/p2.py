'''
Python File Handling & List Comprehension: Write a python program to read the contents
of a file (filename as argument) and store the number of occurrences of each word in a
dictionary. Display the top 10 words with most number of occurrences in descending order.
Store the length of each of these words in a list and display the list. Write a one-line reduce
function to get the average length and one-line list comprehension to display squares of all
odd numbers and display both. 
'''

import functools
import string

# def sort_dict_values(d,reverse):
#     return dict(sorted((d.items()), key = lambda item:item[1],reverse=reverse))

def sort_dict_values(d,reverse):
    return dict(sorted(d.items()),key= lambda item:item[1],reverse=reverse)

# Open the file in read mode
text = open("sample.txt", "r")
d = dict()
for line in text:
    line=line.strip()
    line = line.lower()
    words = line.split(" ")
    for word in words:
        if word in d:
            d[word] = d[word]+1
        else:
            d[word] = 1
sd = sort_dict_values(d,True)
i = 0
ls = []

for key in list(sd.keys()):
    if i<10:
        ls.append(len(key))
        i=i+1
    else:
        break
print(ls)
len_sum = functools.reduce(lambda a,b:a+b,ls)
avg = len_sum/10
sq = [i*i for i in ls ]

# # Create an empty dictionary
# d = dict()
  
# # Loop through each line of the file
# for line in text:
#     # Remove the leading spaces and newline character
#     line = line.strip()
  
#     # Convert the characters in line to
#     # lowercase to avoid case mismatch
#     line = line.lower()
  
#     # Remove the punctuation marks from the line
#     line = line.translate(line.maketrans("", "", string.punctuation))
  
#     # Split the line into words
#     words = line.split(" ")
  
#     # Iterate over each word in line
#     for word in words:
#         # Check if the word is already in dictionary
#         if word in d:
#             # Increment count of word by 1
#             d[word] = d[word] + 1
#         else:
#             # Add the word to dictionary with count 1
#             d[word] = 1
# dd = sort_dict_values(d,True)
# # Print the contents of dictionary
# l =[]
# # wl = []
# i=0
# for key in list(dd.keys()):
#     if i<10:
#         l.append(len(key))
#         print(key, " ", d[key])
#         i=i+1
#     else:
#         break
# sum = functools.reduce(lambda a,b:a+b,l)
# avg = sum/10
# print(avg)
# ls = [i*i for i in l if i%2!=0]
# print(ls)
# # # d.values()
# # for key in list(d.values()):
# #     sorted()