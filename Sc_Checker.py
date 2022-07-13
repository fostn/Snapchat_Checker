import random
from TrackCobra import User
from colorama import Style,Fore
R = Fore.RED
G =Fore.GREEN
B = Fore.BLUE
Y = Fore.YELLOW
c = Fore.LIGHTMAGENTA_EX
b = Fore.LIGHTBLUE_EX
r = Fore.LIGHTRED_EX
w = Fore.WHITE
y = Fore.LIGHTYELLOW_EX
print(y+"""

   _____  _____    _____ _    _ ______ _____ _  ________ _____  
  / ____|/ ____|  / ____| |  | |  ____/ ____| |/ /  ____|  __ \ 
 | (___ | |      | |    | |__| | |__ | |    | ' /| |__  | |__) |
  \___ \| |      | |    |  __  |  __|| |    |  < |  __| |  _  / 
  ____) | |____  | |____| |  | | |___| |____| . \| |____| | \ \ 
 |_____/ \_____|  \_____|_|  |_|______\_____|_|\_\______|_|  \_\                                                              
 Checker Snapchat By fostn : Telegram Channel https://t.me/ifostn
        follow Mohammed : insta @dg5a , Telegram @QQQAQM
 ----------------------------------------------------------------

""")
thecount = int(input(w+"Enter The Count : "))
length = int(input("Enter The Length : "))
a = 0
valid = 0
not_valid = 0
user_index = {'1','2','3','4','5','6','7','8','9','0','.','-','_'}
chars = 'qwertyuiopasdfghjklzxcvbnm1234567890.-_'
#inp = input(" User ")
while a < thecount:
    users = str("".join(random.choice(chars)for i in range(length)))
    checker = User.Snapchat(users)

    if length < 5:
        print(R+'Length must be longer than 4 characters ! . ')
        break

    elif checker == False and length > 4 and users[0] not in user_index and users[-1] not in user_index  :
        print(G+"valid : "+ str(users))
        valid+=1
        with open('valid.txt','a') as f:
            f.write(users+'\n')
    elif checker == True and length > 4 or users[0] in user_index and users[-1] in user_index  :
        not_valid+=1
        print(R+"not valid : " + str(users))

    a =a +1
print('-------------------------------')
print(f"\r{G}valid [{valid}] {w}: {R}unvalid [{not_valid}] ",end="")

