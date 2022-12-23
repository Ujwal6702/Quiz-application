print()
print()
a=int(input("Enter the number of MCQ question you want to create: "))
c=int(input("Enter the number of questions you want to create with one word answers: "))
print()
x=0
y=0
z=0
k=0
quizo=0
r=0
j=0
w=open("Quiz storage.txt", "a")
w.close()
w=open("Quiz storage.txt", "r")
e=0
h=w.read()
u=h.split("\n")
for v in u:
    if v:
        e+=1
w.close()
quizo=(e)+1
t=range(int(e+1))
while j<1:
    d=input("Enter the topic of the quiz: ")
    w=open("Quiz storage.txt", "r")
    l=w.read().split(",")
    for r in t:
        r+1
        if e>0:
           if str(l[(r*4)-1])==str(d):
                j=0
                break
           elif str(l[(r*4)-1])!=str(d):
                j=1
        else:
            j=1
        w.close()
    if j==1:
       w=open("Quiz storage.txt", "a")
       w.write("\n"+","+str(quizo)+","+"User quiz "+str(quizo)+".txt"+","+str(d)+",")
       w.close()
    elif j==0:
        print()
        print("Enter a new topic")
        print()

print()
f=open("User quiz "+str(quizo)+".txt", "a")
f.write(str(a)+"\n"+str(c)+"\n")
f.close()
if a == 0:
  if c!=0:
    while x <c:
        x=x+1
        m=input("Enter your question (one word answer quiz) here: ")
        n=input("Enter the one word answer here: ")
        f=open("User quiz "+str(quizo)+".txt", "a")
        f.write(str(x)+"."+" "+str(m)+" "+"\n")
        f.write(str(n)+" "+"\n")
        f.close()
        print()
else:
    while y<a:
        y=y+1
        m=input("Enter your question (MCQ) here: ")
        f=open("User quiz "+str(quizo)+".txt", "a")
        f.write(str(y)+"."+" "+str(m)+" "+"\n")
        f.close()
        print()
        b=int(input("Enter the number of options you want to have for this MCQ: "))
        f=open("User quiz "+str(quizo)+".txt", "a")
        f.write(str(b)+"\n")
        print()
        while z<b:
            character=int(ord("a"))+int(z)
            character=chr(character)
            z=z+1
            n=input("Enter your "+str(z)+" option here: ")
            f=open("User quiz "+str(quizo)+".txt", "a")
            f.write(str(character)+"."+" "+str(n)+" "+"\n")
            f.close()
        print()
        o=int(input("Enter the correct option number here: "))
        f=open("User quiz "+str(quizo)+".txt", "a")
        f.write(str(o)+" "+"\n")
        f.close()
        z=0
        print()
    if c!=0:
        while k<c:
            k=k+1
            p=input("Enter your question (one word answer quiz) here: ")  
            q=input("Enter the one word answer here: ")
            f=open("User quiz "+str(quizo)+".txt", "a")
            f.write(str(k)+"."+" "+str(p)+" "+"\n")
            f.write(str(q)+" "+"\n")
            f.close()
            print()
print()
print("             *Thanks for using this program. Your created quiz has been updated in the user created quiz menu*")
print()