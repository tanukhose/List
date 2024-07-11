
questions=["Q.1 -:what is a capital of india","Q.2 -:what is a national animal of india","Q.3 -:what is a national bird of india ","Q.4 -:what is a capital of maharastra"]
options=[["A - new delhi","B - koLkata","C -chandigarh","D - pune"],
            ["A - lion","B - elephant","C - tiger","D - dog"],
            ["A - parrot","B - peacock","C - duck","D - crow"],
            ["A - mumbai","B - pune","C - ahmednagar","D - beed"]]
line=[["A - new delhi","B - koLkata"],
            ["C - tiger","A - lion"],
            ["B - peacock","A - parrot"],
            ["A - mumbai","B - pune"]]
answer=["A","C","B","A"]
i=0
c=0
s=0
while i<len(questions):
    print(questions[i])
    j=0
    while j<len(options[i]):
        print(j+1,options[i][j])
        j+=1
    life_line=input(" do you want to take lifeline yes/no")
    if life_line=="yes":
        if c==0:
            k=0
            while k<len(line[i]):
                print(line[i][k])
                s+=1000
                k+=1
            ans=input("enter your answer")
            if answer[i]==ans:
                print("correct option")
                s+=1000
            else:
                print("incorrect answer")
                break
            c+=1
        else:
            print("you can use lifeline once")
            ans=input("enter your answer")
            if answer[i]==ans:
                print("correct answer")
                s+=1000
            else:
                print("incorrect answer")
                break
    else:
        ans=input("enter your answer")
        if answer[i]==ans:
            print("correct answer")
            s+=1000
        else:
            print("incorrect answer")
            break
    i+=1
