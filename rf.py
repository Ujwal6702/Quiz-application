j0=0
k100=0
y0=0
user_score=0
cream=0
chroma=0
ughh=0
w0=open("Quiz storage.txt", "a")
w0.close()
w0=open("Quiz storage.txt", "r")
e0=0
h0=w0.read()
u0=h0.split("\n")
for v0 in u0:
    if v0:
        e0+=1
w0.close()
t0=range(int(e0))
if e0==0:
    print()
    print("There's no user created quiz yet. Please create a quiz to see this menu.")
    print()
if e0>0:
    w0=open("Quiz storage.txt", "r")
    l0=w0.read().split(",")
    print()
    print("                                              *User Quiz menu*")
    for r0 in t0:
        r0=r0+1
        print()
        print(str(l0[(r0*4)-3])+".",str(l0[(r0*4)-1]))
        k0=int(l0[(r0*4)-3])
    w0.close()
    print()
    d0=int(input("Enter the selected number here: "))
    while j0<k0:
        j0=j0+1
        if j0==d0:
            o0=open("User quiz "+str(j0)+".txt", "r")
            l100=o0.read().split("\n")
            o0.close()
            if int(l100[0])==0:
                print()
                print("                            *Welcome to",str(l0[(j0*4)-1]),"Quiz*")
                print()
                for k100 in range(int(l100[1])):
                    print(l100[(k100*2)+2])
                    print()
                    m100=input("Enter your answer here: ")
                    print()
                    if m100.split() == l100[(k100*2)+3].split():
                        print("Your answer is correct.")
                        user_score=user_score+3
                        print()
                    else:
                        print("Your answer is incorrect")
                        print("The correct answer was",str(l100[(k100*2)+3]))
                        print()
                    input("Press enter to continue")
                    print()
                print("Your score is", user_score)
                print()
                print("                             *Thank your for using the program*")
                print()
            if int(l100[0]) > 0:
                print()
                print("                            *Welcome to",str(l0[(j0*4)-1]),"Quiz*")
                print()
                print(l100[2])
                print()
                for options in range(int(l100[3])):
                    print(l100[3+options+1])
                print()
                number=int(l100[3])+1+3
                blah=int(input("Enter the correct option number(if a=1, b=2...): "))
                print()
                if int(l100[3+int(l100[3])+1]) == blah:
                    print("Your answer is correct")
                    print()
                    user_score=user_score+1
                else:
                    print("Your answer is incorrect.")
                    print()
                    print("The correct option was",int(l100[3+int(l100[3])+1]))
                    print()
                cream=number
                input("Press enter to continue")
                print()
                if int(int(l100[0])-int(1)) > int(0):
                    for k100 in range(int(int(l100[0])-int(1))):
                        print(l100[int(cream)+1])
                        print()
                        cream=cream+1
                        ughh=int(l100[int(cream)+1])
                        for game in range(ughh):
                            print(l100[cream+game+2])
                        print()
                        ahh=int(input("Enter the correct option number(if a=1, b=2...): "))
                        if int(l100[cream+ughh+2]) == ahh:
                            print()
                            print("Your answer is correct.")
                            user_score=user_score+1
                        else:
                            print()
                            print("Your answer is incorrect.")
                            print("The correct option was",int(l100[cream+ughh+2]))
                            print()
                        cream=cream+2+ughh
                        input("Press enter to continue")
                        print()
                for k100 in range(int(l100[1])):
                    print(l100[cream+chroma+1])
                    print()
                    m100=input("Enter your answer here: ")
                    print()
                    if m100.split() == l100[cream+chroma+2].split():
                        print()
                        print("Your answer is correct.")
                        user_score=user_score+3
                        print()
                    else:
                        print()
                        print("Your answer is incorrect")
                        print("The correct answer was",str(l100[cream+chroma+2]))
                        print()
                    chroma=chroma+2
                    input("Press enter to continue")
                    print()
                print("Your score is", user_score)
                print()
                print("                             *Thank your for using the program*")
                