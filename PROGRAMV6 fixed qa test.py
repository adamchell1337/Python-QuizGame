import time

quiz_topics = ["Animals","Space","Custom"]
my_dict = {}
quizamount = 0
quiztopic = ""
quizload = ""

def custom_topic():
    print("Please input a custom topic name.")
    customname= input("Topic:")
    quiz_topics[2] = customname
    #print("topics are now:",quiz_topics)

    with open("custom.txt","w") as custom:
        #print("file created")
        qcreated = 0
        while qcreated < 10:
            print("\nQuestion",qcreated+1,":")
            cquestion = input("Please enter the question")
            if cquestion == "":
                print("You cannot leave the question blank")
            else:    
                custom.write(str(cquestion).rstrip('\n'))
                ccolon = custom.write(":")
                canswer =(input("Now input the answer to this question"))
                if canswer == "":
                    print("You cannot leave the answer blank")
                else:
                    custom.write(str(canswer))
                    custom.write(str("\n"))
                    qcreated = qcreated + 1
        print("\nQUIZ CREATED\n")
        
    
def create_dictionary():
    with open(quizload) as quizfile:
    #For Loop for stripping newline and splitting values to convert to Dictionary
      for line in quizfile:
          line = line.strip("\n")
          key, value = line.split(":")
          my_dict[key] = value
    #print(my_dict)

def run_quiz():
    #Introduce Quiz
    time.sleep(1)
    print("\nWELCOME TO THE", quiztopic.upper(), "QUIZ!")
    time.sleep(1)
    global quizamount
    quizamount = int(input("\nHow many questions would you like to answer? (1-10)"))
    while (quizamount < 1) or (quizamount > 10):
            print("\nPlease input a number between 1 and 10")
            time.sleep(1)
            quizamount = int(input("\nHow many questions would you like to answer? (1-10)"))
    
    create_dictionary()
    quiz_loop()
    
def quiz_loop():
    score = 0
    q = int(0)
    qnumber = 0
    #while q != quizamount:
    for x in my_dict:
        q = q+1
        time.sleep(1)
        print("\nQuestion",q,"\n")
        time.sleep(1)
        print(x)
        time.sleep(0.5)
        answer = input("Answer:")
        if answer.lower() == my_dict[x].lower():
            print("Correct!")
            score = score + 1
        else:
            print("Incorrect!")
        if q == quizamount:
            break
        
        #print("q =",q,"quizamount=",quizamount,"score=",score)
        
    print("\nYou have answered",score,"out of the possible",quizamount,"questions correct")
    while True:
        retry = input("Enter R to retry this quiz, or enter M to return to the main menu.")
        if retry == "R":
            quiz_loop()
            break
        elif retry == "M":
            print("\n")
            my_dict.clear()
            welcome()
            break
        else:
            print("Please choose a valid option\n")

def choose_topic():
    while True:
        global quiztopic
        global quizload
        print("What topic would you like to answer questions on?")
        time.sleep(1)
        for topic in quiz_topics:
            print("-",topic)
            time.sleep(0.5)
        quiztopic = input("\nTopic:")
        if quiztopic.lower() == "animals":
            quizload = "animalsquiz.txt"
            run_quiz()
            break
        elif quiztopic.lower() == "space":
            quizload = "spacequiz.txt"
            run_quiz()
            break
        elif quiztopic.lower() == "custom":
            custom_topic()
            continue
        elif quiztopic.lower() == quiz_topics[2].lower():
            quizload = "custom.txt"
            run_quiz()
            break
        
        print("Please choose a valid option")

def welcome():
    print("Welcome to the QuizBot\n")
    time.sleep(1)
    choose_topic()


#PROGRAM START
welcome()

        
