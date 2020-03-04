# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
PhoneBook={}
querry=[]
if (n>=1 and n<=pow(10,5)):
    for i in range (0,n):
        name_phone=input()
        b=name_phone.split(' ')
        PhoneBook[b[0]]=b[1]
    #print(PhoneBook)    

try:
    while(True):
        a=input()
        querry.append(a)
    
except EOFError:
    pass    
for i in range(0,len(querry)): # will run till the number of elements in list
    try:
        print(  querry[i] + "=" + PhoneBook[querry[i]]) # Searching the key in dictonary if found will retun its value otherwise will throw KeyError
    except KeyError:
        print("Not found")
