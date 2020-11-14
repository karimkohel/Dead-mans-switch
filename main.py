import twint, time, datetime, pyAesCrypt

def pay1():
    pass

def FirePayload(protocole):
    print("ACTIVATED PAYLOAD!!!!!")

    # if protocole == 1:
    #     pass
    # elif protocole == 2:
    #     pass
    # else:
    #     pass

    exit()

def CheckKey(c, delayTime, protocole, targetTime):
    try:
        twint.run.Search(c)
    except ValueError:
        print("Something bad happen")
        GetTargets()
    tweets = twint.output.tweets_list
    if not tweets:
        if (time.time() >= targetTime): FirePayload(protocole)
        else:
            print("No results, trying again after delay")
            time.sleep(delayTime)
            CheckKey(c, delayTime, protocole, targetTime)
    else:
        print("Deadswitch De-Activated, Entered Safe Mode")
        exit()

def GetTargets():
    c = twint.Config()
    c.Since = datetime.datetime.today().strftime('%Y-%m-%d')
    c.Search = "Testing tweet"
    c.Username = "KarimKohel"
    delayTime = 10 #300
    protocol = 1
    targetTime = (time.time() + (int(input("How many minuts to run before firing?\n>"))*60))
    c.Hide_output = True
    c.Store_object = True
    CheckKey(c, delayTime, protocol, targetTime)

GetTargets()
