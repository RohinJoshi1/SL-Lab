'''
Python Classes: Write a python class to reverse a sentence (initialized via constructor) word
by word. Example: “I am here” should be reversed as “here am I”. Create instances of this
class for each of the three strings input by the user and display the reversed string for each, in
descending order of number of vowels in the string.
'''
class Reverse:
    vowels = ['a','e','i','o','u']
    def __init__(self,sentence):
        self.sentence = sentence
        self.reverse = " ".join(reversed(self.sentence.split(" ")))
        self.vowel_count = sum(i in self.vowels for i in self.sentence.lower())
        

ob = Reverse("here am I")
print(ob.reverse)

revArr = []
for i in range (3):
    reverse = Reverse(input())
    revArr.append(reverse)
    print(reverse.reverse)

ls = sorted(revArr,key=lambda item:item.vowel_count,reverse=True)
for i in ls:
    print(i.sentence,"\t",i.reverse,"\t",i.vowel_count)
