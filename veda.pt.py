import time
import pandas as pd
name=input("Enter your name please: ")
print("welcome ",name)
print("Program start's in: ")
for i in reversed(range(3)):
    print(i)
    time.sleep(1)
print("start the quizz")
data = {"Name": [], "Score": []}
questions = ("1.How many character in the english alphabets?:",
             "2.What is the smallest planet?: ",
             "3.What is the temperatue of the sun?: ")
options = (("A.22","B.23","C.25","D.26"),
           ("A.Sun","B.Mars","C.Mercury","D.Jupiter"),
           ("A.4000C","B.5000C","C.6000C","D.7000C"))
correct_answers = ["D","C","C"]
guess = []
next_question = 0
score=0
for i in questions:
    print("---------------------------------------------------------")
    print(i)
    for j in options[next_question]:
        print(j)
    seconds = 5 
    while seconds != 0:
        print(f"00:00:0{seconds}")
        seconds -= 1
        time.sleep(1)
    print("Time's up!")
    choosing = input("enter the options(a/b/c/d)?: ").upper()
    guess.append(choosing)

    if choosing == correct_answers[next_question]:
        print("Correct!")
        score+=1
    else:
        print("Incorrect!")
        print(f"{correct_answers[next_question]} is correct answer")
        score-=1
    next_question += 1
    print(f"Your Score: {score}")
if score<0:
        print("Don't worry.Prepare well")
elif score==0:
        print("Some hard word")
else:
        print("Excellent.Keep it up!")
data["Name"].append(name)
data["Score"].append(score)
df = pd.DataFrame(data)
df.to_csv("scores.csv", index=False)
df = pd.read_csv("scores.csv")
print("Your data has been stored ")
print(df)

        
    
