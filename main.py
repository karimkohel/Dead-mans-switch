import twint, time, datetime, pyAesCrypt

def FirePayload(protocole):
    print("ACTIVATED PAYLOAD!!!!!")

    # still no idea on what to do on firing, so ima leave it for now

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
    c.Search = "Last night a DJ saved my life"
    c.Username = "KarimKohel"
    delayTime = 300 # 5 minuts
    protocol = int(input("Protocol number: "))
    targetTime = (time.time() + (int(input("Hours till Doomsday: "))*60*60)) # in hours
    c.Hide_output = True
    c.Store_object = True
    CheckKey(c, delayTime, protocol, targetTime)

GetTargets()
