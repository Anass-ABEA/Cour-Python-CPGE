import datetime
print("Hello User!")
while True :
    a = input("Type something to show the date / keep empty ")
    if len(a) == 0:
        break
    now = datetime.datetime.now()
    print ("Current date and time : ", end = "\t")
    print (now.strftime("%Y-%m-%d %Hsc:%M:%S"))
