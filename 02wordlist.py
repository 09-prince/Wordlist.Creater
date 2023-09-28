from itertools import product
import time
allist=[]
print("Welcome to Wordlist maker")
print("Please select ")
start=int(input("Enter start value: "))
end=int(input("Enter end value: "))
intname=int(input("How many words you want to enter in this wordlist:::   "))
for i in range(intname):
    names=input(f"Enter names {i+1} ? ")
    allist.append(names)
rank=""
for l in allist:
    rank+=l


for i in range(start,end+1):
    for f in product(rank,repeat=i):
        word="".join(f)
        p=open("passsword.txt","+a")
        p.write(word)
        p.write("\n")


for i in range(3):
    time.sleep(1)
    print("Saving your file ....")
print("Thank you, Your wordlist is ready.")













