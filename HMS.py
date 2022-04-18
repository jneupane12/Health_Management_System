clientList={1:"John",2:"Jack",3:"Jason"}
logList={1:"Exercise",2:"Food"}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Select Client name")
    for key,value in clientList.items():
        print("Press",key,"for",value,'\n',end="")
    clientName=int(input())

    print("Selected Client: ",clientList[clientName],'\n',end="")
    print("Press 1 to log")
    print("Press 2 to retrieve")
    option=int(input())


    if option==1:
        for key,value in logList.items():
            print("Press",key,"to log",value,"\n",end="")
        logName=int(input())
        print("Selected Job:",logList[logName])
        f=open(clientList[clientName]+"_"+logList[logName]+".txt","a")
        k="y"
        while(k is not "n"):
            print("Enter",logList[logName],"\n",end="")
            myText=input()
            f.write("["+str(getdate())+"]:"+ myText+"\n")
            k= input("Add more? y/n")
            continue
        f.close()
    elif option==2:
        for key,value in logList.items():
            print("Press",key,"to retrieve",value,"\n",end="")
        logName=int(input())
        print(clientList[clientName]+"_"+logList[logName],"Report:","\n",end="")
        f=open(clientList[clientName]+"_"+logList[logName]+".txt","rt")
        contents=f.readlines()
        for lines in contents:
            print(lines,end="")
        f.close()
    else:
        print("Invalid Input")
except Exception as e:
    print("Wrong input")




