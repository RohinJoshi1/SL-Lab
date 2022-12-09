'''
Python: Write Python code to do the following:
i. Create list with inputs from user
ii. Determine minimum and maximum elements in the list
iii. Insert new element into the list
iv. Delete an element from the list
v. Determine if an element is present in the list
'''

ls = []
x=int(input("Enter no.of items to enter"))
for i in range (int(x)) :
    ls.append(int(input()))

while 1:
    c = int(input("1.Enter new element\n2.Find min and max \n3.Delete an element\n 4.Find an element\n5.print list\n6.Exit\n"))
    
    if(c==1):
        ls.append(int(input("Enter element")))
    elif(c==2):
        print("Max: ",max(ls)," Min: ",min(ls))
    elif(c==3):
        try:
            ls.remove(int(input("enter element to delete")))
        except:
            print("Element does not exist")
    elif(c==4):
        try:
            s = int(input("enter element to search for"))
            if s in ls:
                print("Element found at index ",ls.index(s))
        except:
            print("element not found")
    elif(c==5):
        print(ls)
    else:
        break
print("Exited")

