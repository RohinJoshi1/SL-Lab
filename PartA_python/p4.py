'''
Python: Write Python code to do the following operations:
• Create a dictionary that contains the atomic element symbol and its name.
• Add a unique & duplicate element into this dictionary by interacting with the user.
Observe the output and justify it.
• Display the number of atomic elements in this dictionary
• Ask user to enter an element to search in the dictionary. Display appropriate results.
Rewrite this program so that these operations are inside a function called ‘AtomicDictionary’.
Create another python file called “Atomic.py” and execute this function in it.
'''

d = {
    "O":"Oxygen",
    "H" :"Hydrogen",
    "He" :"Helium",
    "C" :"Carbon"
}
x = input("enter element to search")
try:
    if(x in d.keys()):
        print("YEs")
        print(d.get(x))
except:
    print("Not found")

d.update({"B":"Boron"})
print(d)

