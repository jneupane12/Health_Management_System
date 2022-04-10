def getdate():
    import datetime
    return str(datetime.datetime.now())

dateTime = [getdate()]

def wrongSelection():
    print("Wrong Selection, Try again")


def logJohnDiet():
    x=input("Enter diet for John")
    logfile = open("logJohnDiet.txt","a")
    logfile.write("\n{} {}".format(dateTime,x))

    logfile.close()
    print("File logged successfully.")



def logJackDiet():
    x=input("Enter diet for Jack")
    logfile = open("logJackDiet.txt","a")
    logfile.write("\n{} {}".format(dateTime,x))
    logfile.close()
    print("File logged successfully.")



def logJasonDiet():
    x=input("Enter diet for Jason")
    logfile = open("logJasonDiet.txt","a")
    logfile.write("\n{} {}".format(dateTime,x))
    logfile.close()
    print("File logged successfully.")


def logJohnExercise():
    x=input("Enter exercise for John")
    logfile = open("logJohnExercise.txt","a")
    logfile.write("\n{} {}".format(dateTime,x))
    logfile.close()
    print("File logged successfully.")



def logJackExercise():
    x=input("Enter exercise for Jack")
    logfile = open("logJackExercise.txt","a")
    logfile.write("\n{} {}".format(dateTime,x))
    logfile.close()
    print("File logged successfully.")



def logJasonExercise():
    x=input("Enter exercise for Jason")
    logfile = open("logJasonExercise.txt","a")
    logfile.write("\n{} {}".format(dateTime,x))
    logfile.close()
    print("File logged successfully.")


def retrieveJohnDiet():

    logfile = open("logJohnDiet.txt")
    content = logfile.read()
    print(content)
    logfile.close()


def retrieveJohnExercise():
    logfile = open("logJohnExercise.txt")
    content =logfile.read()
    print(content)
    logfile.close()


def retrieveJackDiet():

    logfile = open("logJackDiet.txt")
    content = logfile.read()
    print(content)
    logfile.close()


def retrieveJackExercise():
    logfile = open("logJackExercise.txt")
    content =logfile.read()
    print(content)
    logfile.close()

def retrieveJasonDiet():

    logfile = open("logJasonDiet.txt")
    content = logfile.read()
    print(content)
    logfile.close()


def retrieveJasonExercise():
    logfile = open("logJasonExercise.txt")
    content =logfile.read()
    print(content)
    logfile.close()


try:
    prompt1 =int(input("Enter 1 for log and 2 to retrieve health information"))
    choices = [1,2]
    if prompt1 not in choices:
        print("Please input carefully")
    if prompt1==1:
        logPrompt1 = int(input("Which client information you want to log?\n Press 1 for John, 2 for Jack and 3 for Jason"))
        if logPrompt1==1:
            logPrompt2 =int(input("Which log you want to insert for John?\n Press 1 to log diet and press 2 for exercise"))
            if logPrompt2==1:
                logJohnDiet()
            elif logPrompt2==2:
                logJohnExercise()
            else:
                wrongSelection()

        elif(logPrompt1==2):

                logPrompt2=int(input("Which log you want to insert for Jack?\n Press 1 to log diet and press 2 for exercise"))
                if logPrompt2==1:
                    logJackDiet()
                elif logPrompt2==2:
                    logJackExercise()
                else:
                    wrongSelection()

        elif(logPrompt1==3):

                logPrompt2=int(input("Which log you want to insert for Jason?\n Press 1 to log diet and press 2 for exercise"))
                if logPrompt2==1:
                    logJasonDiet()
                elif logPrompt2==2:
                    logJasonExercise()
                else:
                    wrongSelection()
        else:
            wrongSelection()


    elif(prompt1==2):
        logPrompt1 = int(input("Which client information you want to retrieve?\n Press 1 for John, 2 for Jack and 3 for Jason"))
        if logPrompt1==1:
            logPrompt2 =int(input("retrieve for John?\n Press 1 to retrieve diet and press 2 for exercise"))
            if logPrompt2==1:
                retrieveJohnDiet()
            elif logPrompt2==2:
                retrieveJohnExercise()
            else:
                wrongSelection()


        elif logPrompt1==2:
            logPrompt2 =int(input("retrieve for Jack?\n Press 1 to retrieve diet and press 2 for exercise"))
            if logPrompt2==1:
                retrieveJackDiet()
            elif logPrompt2==2:
                retrieveJackExercise()
            else:
                wrongSelection()

        elif logPrompt1==3:
            logPrompt2 =int(input("retrieve for Jason?\n Press 1 to retrieve diet and press 2 for exercise"))
            if logPrompt2==1:
                retrieveJasonDiet()
            elif logPrompt2==2:
                retrieveJasonExercise()
            else:
                wrongSelection()
    else:
        wrongSelection()

except Exception as e:
    print(e)
    print("Please enter carefully")
