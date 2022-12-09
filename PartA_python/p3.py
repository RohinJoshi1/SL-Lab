'''
Python: Write a temperature converter python program, which is menu driven. Each such
conversion logic should be defined in separate functions. The program should call the
respective function based on the user’s requirement. The program should run as long as the
user wishes so. Provide an option to view the conversions stored as list of tuples with attributes
- from unit value, to unit value sorted by the user’s choice (from-value or to-value).
'''

ls= []
def CtoF(cel):
    F = 9/5*cel+32
    res = (cel,F)
    ls.append(res)

def FtoC(F):
    C = 5/9*(F-32)
    res = (F,C)
    ls.append(res)

def CtoK(cel):
    K = cel + 273
    res = (cel,K)
    ls.append(res)

def KtoC(K):
    C = K -273
    res = (K,C)
    ls.append(res)

one = CtoF(10)
two = FtoC(10)
three = KtoC(39)
print(ls)
#sort based on from
ls = sorted(ls,key= lambda x:x[1])
print(ls)

