print("enter file name:")
filename=input()
print("enter string:")
string=input()

file=open(filename,"r")

for x in file:
    if "Hi" in x:
        print(x)
    
