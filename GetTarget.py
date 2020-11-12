# import twint
# from datetime import datetime

# def startTwint()
#     c = twint.Config()

#     while True:
#         startTime = input("enter a date to start looking from (Fromat: %y-%m-%\d)\n>")

#         try:
#             datetime.strptime(startTime, '%Y-%m-%d')
#         except ValueError:
#             print("Format is wrong, try again")

#     c.Since = startTime
#     c.Search = "Last night a DJ saved my life"
#     c.Username = "karimkohel"
#     delayTime = pass
#     filePath = input("File to encrypt if switch fires?\n>")
#     encryptPass = input("Password to encrypt file?\n>")
#     targetTime = (time.time() + (int(input("How many minutes to run before firing?\n>"))*60))
#     c.Hide_output = True
#     c.Store_object = True
#     CheckKey(c, delayTime, filePath, encryptPass, targetTime)