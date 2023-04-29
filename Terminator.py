import time, threading, requests, fade, sys, asyncio, os, random, threading, json, websocket
from colorama import Back, Fore, Style
from websocket import WebSocket

w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
lm = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
m = Fore.MAGENTA
bb = Fore.BLUE



lock = threading.Lock()
os.system('mode 120,30')
threads = 3


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

def Spinner():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		time.sleep(0.1)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')           
    print('')
    print('')
    text = """
████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ████████╗ ██████╗ ██████╗     ██╗   ██╗██████╗ 
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    ██║   ██║╚════██╗
   ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║   ██║   ██║   ██║██████╔╝    ██║   ██║ █████╔╝
   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║   ██║   ██║   ██║██╔══██╗    ╚██╗ ██╔╝██╔═══╝ 
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║   ██║   ╚██████╔╝██║  ██║     ╚████╔╝ ███████╗
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝      ╚═══╝  ╚══════╝
                                                                                                         
    """
    faded_title = fade.purplepink(text)
    print(faded_title)
    credits = """
      __  __             _           ___          _      ___   _   _        _        
     |  \/  |  __ _   __| |  ___    | _ )  _  _  (_)    / __| | | (_)  __  | |__  ___
     | |\/| | / _` | / _` | / -_)   | _ \ | || |  _    | (__  | | | | / _| | / / (_-<
     |_|  |_| \__,_| \__,_| \___|   |___/  \_, | (_)    \___| |_| |_| \__| |_\_\ /__/
                                           |__/                                      
    """
    faded_credits = fade.water(credits)
    print(faded_credits)
    print(f'''
    {bb}[{w}1{bb}] {w}Server Joiner   {b}|{Fore.RESET}{bb}[{w}9{Fore.RESET}{bb}]{w}   Channel Spammer  
    {bb}[{w}2{bb}] {w}Server Leaver   {b}|{Fore.RESET}{bb}[{w}10{Fore.RESET}{bb}]{w}  Dm Spammer 
    {bb}[{w}3{bb}] {w}Webhook Spammer {b}|{Fore.RESET}{bb}[{w}11{Fore.RESET}{bb}]{w}  Friend Spammer  
    {bb}[{w}4{bb}] {w}Token Grabber   {b}|{Fore.RESET}{bb}[{w}12{Fore.RESET}{bb}]{w}  Reaction Spammer  
    {bb}[{w}5{bb}] {w}Token Checker   {b}|{Fore.RESET}{bb}[{w}13{Fore.RESET}{bb}]{w}  Nickname Changer  
    {bb}[{w}6{bb}] {w}Token Onliner   {b}|{Fore.RESET}{bb}[{w}14{Fore.RESET}{bb}]{w}  Webhook Spammer  
    {bb}[{w}7{bb}] {w}Server Nuker    {b}|{Fore.RESET}{bb}[{w}15{Fore.RESET}{bb}]{w}  Status Changer
    {bb}[{w}8{bb}] {w}Account Nuker   {b}|{Fore.RESET}{bb}[{w}16{Fore.RESET}{bb}]{w}{lr}  EXIT{Fore.RESET}
    ''')

    choice = input(f'{bb}[{w}>{bb}]{w} What would you like to do?: ')

    if choice == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        Spinner()
        title1 = """       
███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗          ██╗ ██████╗ ██╗███╗   ██╗███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗         ██║██╔═══██╗██║████╗  ██║██╔════╝██╔══██╗
███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝         ██║██║   ██║██║██╔██╗ ██║█████╗  ██████╔╝
╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗    ██   ██║██║   ██║██║██║╚██╗██║██╔══╝  ██╔══██╗
███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║    ╚█████╔╝╚██████╔╝██║██║ ╚████║███████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝     ╚════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝                                                                                                
        """
        faded_title1 = fade.purplepink(title1)
        #print (faded_title1)
        cs = """        
  /$$$$$$                          /$$                            /$$$$$$                               
 /$$__  $$                        |__/                           /$$__  $$                              
| $$  \__/  /$$$$$$  /$$$$$$/$$$$  /$$ /$$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$$ 
| $$       /$$__  $$| $$_  $$_  $$| $$| $$__  $$ /$$__  $$      |  $$$$$$  /$$__  $$ /$$__  $$| $$__  $$
| $$      | $$  \ $$| $$ \ $$ \ $$| $$| $$  \ $$| $$  \ $$       \____  $$| $$  \ $$| $$  \ $$| $$  \ $$
| $$    $$| $$  | $$| $$ | $$ | $$| $$| $$  | $$| $$  | $$       /$$  \ $$| $$  | $$| $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$/| $$ | $$ | $$| $$| $$  | $$|  $$$$$$$      |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$  | $$
 \______/  \______/ |__/ |__/ |__/|__/|__/  |__/ \____  $$       \______/  \______/  \______/ |__/  |__/
                                                 /$$  \ $$                                              
                                                |  $$$$$$/                                              
                                                 \______/                                               
        """
        faded_cs = fade.purpleblue(cs)
        print(faded_cs)
        exitleave = input(f'{bb}[{w}>{bb}]{w} Press ENTER: ')
        continue

    # Server Leaver
    if choice == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        Spinner()
        title2 = """
███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗     ██╗     ███████╗ █████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗    ██║     ██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝    ██║     █████╗  ███████║██║   ██║█████╗  ██████╔╝
╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗    ██║     ██╔══╝  ██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║    ███████╗███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝                                                                                                 
    """
        faded_title2 = fade.purplepink(title2)
        print(faded_title2)
        ID = input(f'{bb}[{w}>{bb}]{w} Server ID:')

        apilink = "https://discord.com/api/v9/users/@me/guilds/" + str(ID)
        with open('tokens.txt', 'r') as file:
            for line in file:
                tokens = line.strip()
                headers = {
                    "Authorization": tokens
                }

                leave_url = f"https://discord.com/api/v8/users/@me/guilds/{ID}"

                response = requests.delete(leave_url, headers=headers)

                if response.status_code == 204:
                    print(f"Successfully left server with ID {ID}")
                elif response.status_code == 401:
                    print(f"Failed to leave server with ID {ID}. Please make sure you are using valid tokens.")
                else:
                    print(f"Failed to leave server with ID {ID}. Status code: {response.status_code}")

        print(f'{bb}[{w}>{bb}]{w} Done')
        time.sleep(1)
        exitleave = input(f'{bb}[{w}>{bb}]{w} Press ENTER: ')
        continue

#   WEBHOOK SPAMMER
    if choice == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
        Spinner()
        title3 = """           
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗  
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝  
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝   
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗   
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗  
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝  
███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                              
                                                                                                                                                                                  
            """
        fade_title3 = fade.purplepink(title3)
        print(fade_title3)
        session = requests.Session()
        webhook = input(f"{bb}[{w}>{bb}]{w} Webhook URL: ")
        message = input(f"{bb}[{w}>{bb}]{w} Message: ")
        username = input(f"{bb}[{w}>{bb}]{w} Webhook Username?: ")

        def term():
            session.post(webhook, json={"content": message, "username": username})
            if requests.exceptions.MissingSchema:
                print("ERROR invalid url please use valid url")
                
            while True:
                for i in range(15):
                    threading.Thread(target=term).start()
        
        time.sleep(1)
        exitleave = input(f'{bb}[{w}>{bb}]{w} Press ENTER: ')
        continue
    
    if choice == '4':
        os.system('cls' if os.name == 'nt' else 'clear')
        Spinner()
        cs = """        
  /$$$$$$                          /$$                            /$$$$$$                               
 /$$__  $$                        |__/                           /$$__  $$                              
| $$  \__/  /$$$$$$  /$$$$$$/$$$$  /$$ /$$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$$ 
| $$       /$$__  $$| $$_  $$_  $$| $$| $$__  $$ /$$__  $$      |  $$$$$$  /$$__  $$ /$$__  $$| $$__  $$
| $$      | $$  \ $$| $$ \ $$ \ $$| $$| $$  \ $$| $$  \ $$       \____  $$| $$  \ $$| $$  \ $$| $$  \ $$
| $$    $$| $$  | $$| $$ | $$ | $$| $$| $$  | $$| $$  | $$       /$$  \ $$| $$  | $$| $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$/| $$ | $$ | $$| $$| $$  | $$|  $$$$$$$      |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$  | $$
 \______/  \______/ |__/ |__/ |__/|__/|__/  |__/ \____  $$       \______/  \______/  \______/ |__/  |__/
                                                 /$$  \ $$                                              
                                                |  $$$$$$/                                              
                                                 \______/                                               
        """
        faded_cs = fade.purpleblue(cs)
        print(faded_cs)
        exitleave = input(f'{bb}[{w}>{bb}]{w} Press ENTER: ')
        continue


# Token Checker
    if choice == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            Spinner()
            title5 = """           
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                                                                                                                                                                          
            """
            fade_title5 = fade.purplepink(title5)
            print(fade_title5)
            print(f'{bb}[{w}>{bb}]{w} Loading Tokens:\n')
            time.sleep(0.5)
            def success(text): lock.acquire(); print(f"{g}[{Fore.GREEN}>{g}] {Fore.GREEN}Valid {g}{text}{g}"); lock.release()
            def invalid(text): lock.acquire(); print(f"{lr}[{Fore.RED}>{lr}] {Fore.RED}Invalid {Fore.RED} {text}{lr}"); lock.release()

            with open("tokens.txt", "r") as f: tokens = f.read().splitlines()
            def save_tokens():
                with open("tokens.txt", "w") as f: f.write("")
                for token in tokens:
                    with open("tokens.txt", "a") as f: f.write(token + "\n")
            def removeDuplicates(file):
                lines_seen = set()
                with open(file, "r+") as f:
                    d = f.readlines(); f.seek(0)
                    for i in d:
                        if i not in lines_seen: f.write(i); lines_seen.add(i)
                    f.truncate()
            def check_token(token:str):
                response = requests.get('https://discord.com/api/v9/users/@me/library', headers={"accept": "*/*","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9","authorization": token,"cookie": "__dcfduid=88221810e37411ecb92c839028f4e498; __sdcfduid=88221811e37411ecb92c839028f4e498dc108345b16a69b7966e1b3d33d2182268b3ffd2ef5dfb497aef45ea330267cf; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jun+03+2022+15%3A36%3A59+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __stripe_mid=3a915c95-4cf7-4d27-9d85-cfea03f7ce829a88e5; __stripe_sid=b699111a-a911-402d-a08a-c8801eb0f2e8baf912; __cf_bm=nEUsFi1av6PiX4cHH1PEcKFKot6_MslL4UbUxraeXb4-1654285264-0-AU8vy1OnS/uTMTGu2TbqIGYWUreX3IAEpMo++NJZgaaFRNAikwxeV/gxPixQ/DWlUyXaSpKSNP6XweSVG5Mzhn/QPdHU3EmR/pQ5K42/mYQaiRRl6osEVJWMMtli3L5iIA==","referer": "https://discord.com/channels/967617613960187974/981260247807168532","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","sec-gpc": "1","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "en-US","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwNDEwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}, timeout=5)
                if response.status_code == 200: success(f"| {token[:63]}*********")
                else: tokens.remove(token); invalid(f"| {token}")
            def check_tokens():
                threads=[]
                for token in tokens:
                    try:threads.append(threading.Thread(target=check_token, args=(token,)))
                    except Exception as e: pass
                for thread in threads: thread.start()
                for thread in threads: thread.join()
            def start():
                removeDuplicates("tokens.txt")
                check_tokens()
                save_tokens()

            start()
            print(f'{bb}[{w}>{bb}]{w} All Tokens have been Checked! (tokens.txt has been updated with only vaild tokens!)')
            time.sleep(1)
            exitleave = input(f'{bb}[{w}>{bb}]{w} Press ENTER: ')
            continue
             
# Token Onliner
    if choice == '6':
        os.system('cls' if os.name == 'nt' else 'clear')
        Spinner()
        title6 = """
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗     ██████╗ ███╗   ██╗██╗     ██╗███╗   ██╗███████╗██████╗ 
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔═══██╗████╗  ██║██║     ██║████╗  ██║██╔════╝██╔══██╗
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║   ██║██╔██╗ ██║██║     ██║██╔██╗ ██║█████╗  ██████╔╝
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║   ██║██║╚██╗██║██║     ██║██║╚██╗██║██╔══╝  ██╔══██╗
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ╚██████╔╝██║ ╚████║███████╗██║██║ ╚████║███████╗██║  ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        """
        fade_title6 = fade.purplepink(title6)
        print(fade_title6)

        with open("tokens.txt", "r") as f:
            tokens = f.read().splitlines()

        # Use the Discord API to set the user's presence to the desired status
        for token in tokens:
            print(f"{bb}Current token: {w}{token}")
            headers = {
                "Authorization": token,
                "Content-Type": "application/json"
            }
            payload = {
                "status": "online",
                "activities": [{
                    "type": 0,
                    "name": "Terminator V2"
                }]
            }
            r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)
            if r.status_code == 200:
                print(f"{g}[{Fore.GREEN}>{g}] {Fore.GREEN}Success {g}{text}{g}")
            else:
                print(f"{lr}[{Fore.RED}>{lr}] {Fore.RED}Invalid with error {lr}{r.status_code}{Fore.RED} {lr}")
            time.sleep(1)

        input(f'{bb}[{w}>{bb}]{w} Press ENTER to continue: ')

    if choice == '7':
        os.system('cls' if os.name == 'nt' else 'clear')
        Spinner()
        cs = """        
  /$$$$$$                          /$$                            /$$$$$$                               
 /$$__  $$                        |__/                           /$$__  $$                              
| $$  \__/  /$$$$$$  /$$$$$$/$$$$  /$$ /$$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$$ 
| $$       /$$__  $$| $$_  $$_  $$| $$| $$__  $$ /$$__  $$      |  $$$$$$  /$$__  $$ /$$__  $$| $$__  $$
| $$      | $$  \ $$| $$ \ $$ \ $$| $$| $$  \ $$| $$  \ $$       \____  $$| $$  \ $$| $$  \ $$| $$  \ $$
| $$    $$| $$  | $$| $$ | $$ | $$| $$| $$  | $$| $$  | $$       /$$  \ $$| $$  | $$| $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$/| $$ | $$ | $$| $$| $$  | $$|  $$$$$$$      |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$  | $$
 \______/  \______/ |__/ |__/ |__/|__/|__/  |__/ \____  $$       \______/  \______/  \______/ |__/  |__/
                                                 /$$  \ $$                                              
                                                |  $$$$$$/                                              
                                                 \______/                                               
        """
        faded_cs = fade.purpleblue(cs)
        print(faded_cs)
        exitleave = input(f'{bb}[{w}>{bb}]{w} Press ENTER: ')
        continue

    if choice == '8':
        os.system('cls' if os.name == 'nt' else 'clear')
        Spinner()
        cs = """        
  /$$$$$$                          /$$                            /$$$$$$                               
 /$$__  $$                        |__/                           /$$__  $$                              
| $$  \__/  /$$$$$$  /$$$$$$/$$$$  /$$ /$$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$$ 
| $$       /$$__  $$| $$_  $$_  $$| $$| $$__  $$ /$$__  $$      |  $$$$$$  /$$__  $$ /$$__  $$| $$__  $$
| $$      | $$  \ $$| $$ \ $$ \ $$| $$| $$  \ $$| $$  \ $$       \____  $$| $$  \ $$| $$  \ $$| $$  \ $$
| $$    $$| $$  | $$| $$ | $$ | $$| $$| $$  | $$| $$  | $$       /$$  \ $$| $$  | $$| $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$/| $$ | $$ | $$| $$| $$  | $$|  $$$$$$$      |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$  | $$
 \______/  \______/ |__/ |__/ |__/|__/|__/  |__/ \____  $$       \______/  \______/  \______/ |__/  |__/
                                                 /$$  \ $$                                              
                                                |  $$$$$$/                                              
                                                 \______/                                               
        """
        faded_cs = fade.purpleblue(cs)
        print(faded_cs)
        exitleave = input(f'{bb}[{w}>{bb}]{w} Press ENTER: ')
        continue

    if choice == '9':
        os.system('cls' if os.name == 'nt' else 'clear')
        Spinner()
        cs = """        
  /$$$$$$                          /$$                            /$$$$$$                               
 /$$__  $$                        |__/                           /$$__  $$                              
| $$  \__/  /$$$$$$  /$$$$$$/$$$$  /$$ /$$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$$ 
| $$       /$$__  $$| $$_  $$_  $$| $$| $$__  $$ /$$__  $$      |  $$$$$$  /$$__  $$ /$$__  $$| $$__  $$
| $$      | $$  \ $$| $$ \ $$ \ $$| $$| $$  \ $$| $$  \ $$       \____  $$| $$  \ $$| $$  \ $$| $$  \ $$
| $$    $$| $$  | $$| $$ | $$ | $$| $$| $$  | $$| $$  | $$       /$$  \ $$| $$  | $$| $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$/| $$ | $$ | $$| $$| $$  | $$|  $$$$$$$      |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$  | $$
 \______/  \______/ |__/ |__/ |__/|__/|__/  |__/ \____  $$       \______/  \______/  \______/ |__/  |__/
                                                 /$$  \ $$                                              
                                                |  $$$$$$/                                              
                                                 \______/                                               
        """
        faded_cs = fade.purpleblue(cs)
        print(faded_cs)
        exitleave = input(f'{bb}[{w}>{bb}]{w} Press ENTER: ')
        continue    


    if choice == '10':
        os.system('cls' if os.name == 'nt' else 'clear')
        Spinner()
        cs = """        
  /$$$$$$                          /$$                            /$$$$$$                               
 /$$__  $$                        |__/                           /$$__  $$                              
| $$  \__/  /$$$$$$  /$$$$$$/$$$$  /$$ /$$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$$ 
| $$       /$$__  $$| $$_  $$_  $$| $$| $$__  $$ /$$__  $$      |  $$$$$$  /$$__  $$ /$$__  $$| $$__  $$
| $$      | $$  \ $$| $$ \ $$ \ $$| $$| $$  \ $$| $$  \ $$       \____  $$| $$  \ $$| $$  \ $$| $$  \ $$
| $$    $$| $$  | $$| $$ | $$ | $$| $$| $$  | $$| $$  | $$       /$$  \ $$| $$  | $$| $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$/| $$ | $$ | $$| $$| $$  | $$|  $$$$$$$      |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$  | $$
 \______/  \______/ |__/ |__/ |__/|__/|__/  |__/ \____  $$       \______/  \______/  \______/ |__/  |__/
                                                 /$$  \ $$                                              
                                                |  $$$$$$/                                              
                                                 \______/                                               
        """
        faded_cs = fade.purpleblue(cs)
        print(faded_cs)
        exitleave = input(f'{bb}[{w}>{bb}]{w} Press ENTER: ')
        continue     

    if choice == '11':
        os.system('cls' if os.name == 'nt' else 'clear')
        Spinner()
        cs = """        
  /$$$$$$                          /$$                            /$$$$$$                               
 /$$__  $$                        |__/                           /$$__  $$                              
| $$  \__/  /$$$$$$  /$$$$$$/$$$$  /$$ /$$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$$ 
| $$       /$$__  $$| $$_  $$_  $$| $$| $$__  $$ /$$__  $$      |  $$$$$$  /$$__  $$ /$$__  $$| $$__  $$
| $$      | $$  \ $$| $$ \ $$ \ $$| $$| $$  \ $$| $$  \ $$       \____  $$| $$  \ $$| $$  \ $$| $$  \ $$
| $$    $$| $$  | $$| $$ | $$ | $$| $$| $$  | $$| $$  | $$       /$$  \ $$| $$  | $$| $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$/| $$ | $$ | $$| $$| $$  | $$|  $$$$$$$      |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$  | $$
 \______/  \______/ |__/ |__/ |__/|__/|__/  |__/ \____  $$       \______/  \______/  \______/ |__/  |__/
                                                 /$$  \ $$                                              
                                                |  $$$$$$/                                              
                                                 \______/                                               
        """
        faded_cs = fade.purpleblue(cs)
        print(faded_cs)
        exitleave = input(f'{bb}[{w}>{bb}]{w} Press ENTER: ')
        continue

    if choice == '12':
        os.system('cls' if os.name == 'nt' else 'clear')
        Spinner()
        cs = """        
  /$$$$$$                          /$$                            /$$$$$$                               
 /$$__  $$                        |__/                           /$$__  $$                              
| $$  \__/  /$$$$$$  /$$$$$$/$$$$  /$$ /$$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$$ 
| $$       /$$__  $$| $$_  $$_  $$| $$| $$__  $$ /$$__  $$      |  $$$$$$  /$$__  $$ /$$__  $$| $$__  $$
| $$      | $$  \ $$| $$ \ $$ \ $$| $$| $$  \ $$| $$  \ $$       \____  $$| $$  \ $$| $$  \ $$| $$  \ $$
| $$    $$| $$  | $$| $$ | $$ | $$| $$| $$  | $$| $$  | $$       /$$  \ $$| $$  | $$| $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$/| $$ | $$ | $$| $$| $$  | $$|  $$$$$$$      |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$  | $$
 \______/  \______/ |__/ |__/ |__/|__/|__/  |__/ \____  $$       \______/  \______/  \______/ |__/  |__/
                                                 /$$  \ $$                                              
                                                |  $$$$$$/                                              
                                                 \______/                                               
        """
        faded_cs = fade.purpleblue(cs)
        print(faded_cs)
        exitleave = input(f'{bb}[{w}>{bb}]{w} Press ENTER: ')
        continue

    if choice == '13':
        os.system('cls' if os.name == 'nt' else 'clear')
        Spinner()
        cs = """        
  /$$$$$$                          /$$                            /$$$$$$                               
 /$$__  $$                        |__/                           /$$__  $$                              
| $$  \__/  /$$$$$$  /$$$$$$/$$$$  /$$ /$$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$$ 
| $$       /$$__  $$| $$_  $$_  $$| $$| $$__  $$ /$$__  $$      |  $$$$$$  /$$__  $$ /$$__  $$| $$__  $$
| $$      | $$  \ $$| $$ \ $$ \ $$| $$| $$  \ $$| $$  \ $$       \____  $$| $$  \ $$| $$  \ $$| $$  \ $$
| $$    $$| $$  | $$| $$ | $$ | $$| $$| $$  | $$| $$  | $$       /$$  \ $$| $$  | $$| $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$/| $$ | $$ | $$| $$| $$  | $$|  $$$$$$$      |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$  | $$
 \______/  \______/ |__/ |__/ |__/|__/|__/  |__/ \____  $$       \______/  \______/  \______/ |__/  |__/
                                                 /$$  \ $$                                              
                                                |  $$$$$$/                                              
                                                 \______/                                               
        """
        faded_cs = fade.purpleblue(cs)
        print(faded_cs)
        exitleave = input(f'{bb}[{w}>{bb}]{w} Press ENTER: ')
        continue

    if choice == '14':
        os.system('cls' if os.name == 'nt' else 'clear')
        Spinner()
        cs = """        
  /$$$$$$                          /$$                            /$$$$$$                               
 /$$__  $$                        |__/                           /$$__  $$                              
| $$  \__/  /$$$$$$  /$$$$$$/$$$$  /$$ /$$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$$ 
| $$       /$$__  $$| $$_  $$_  $$| $$| $$__  $$ /$$__  $$      |  $$$$$$  /$$__  $$ /$$__  $$| $$__  $$
| $$      | $$  \ $$| $$ \ $$ \ $$| $$| $$  \ $$| $$  \ $$       \____  $$| $$  \ $$| $$  \ $$| $$  \ $$
| $$    $$| $$  | $$| $$ | $$ | $$| $$| $$  | $$| $$  | $$       /$$  \ $$| $$  | $$| $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$/| $$ | $$ | $$| $$| $$  | $$|  $$$$$$$      |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$  | $$
 \______/  \______/ |__/ |__/ |__/|__/|__/  |__/ \____  $$       \______/  \______/  \______/ |__/  |__/
                                                 /$$  \ $$                                              
                                                |  $$$$$$/                                              
                                                 \______/                                               
        """
        faded_cs = fade.purpleblue(cs)
        print(faded_cs)
        exitleave = input(f'{bb}[{w}>{bb}]{w} Press ENTER: ')
        continue

    if choice == '15':
        os.system('cls' if os.name == 'nt' else 'clear')
        Spinner()
        cs = """        
  /$$$$$$                          /$$                            /$$$$$$                               
 /$$__  $$                        |__/                           /$$__  $$                              
| $$  \__/  /$$$$$$  /$$$$$$/$$$$  /$$ /$$$$$$$   /$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$$ 
| $$       /$$__  $$| $$_  $$_  $$| $$| $$__  $$ /$$__  $$      |  $$$$$$  /$$__  $$ /$$__  $$| $$__  $$
| $$      | $$  \ $$| $$ \ $$ \ $$| $$| $$  \ $$| $$  \ $$       \____  $$| $$  \ $$| $$  \ $$| $$  \ $$
| $$    $$| $$  | $$| $$ | $$ | $$| $$| $$  | $$| $$  | $$       /$$  \ $$| $$  | $$| $$  | $$| $$  | $$
|  $$$$$$/|  $$$$$$/| $$ | $$ | $$| $$| $$  | $$|  $$$$$$$      |  $$$$$$/|  $$$$$$/|  $$$$$$/| $$  | $$
 \______/  \______/ |__/ |__/ |__/|__/|__/  |__/ \____  $$       \______/  \______/  \______/ |__/  |__/
                                                 /$$  \ $$                                              
                                                |  $$$$$$/                                              
                                                 \______/                                               
        """
        faded_cs = fade.purpleblue(cs)
        print(faded_cs)
        exitleave = input(f'{bb}[{w}>{bb}]{w} Press ENTER: ')
        continue



    #   EXIT
    if choice == '16':
        Spinner()
        exit_choice = input(f"\n{bb}[{w}>{bb}]{w} Are You Sure You Want To Exit Terminator V2? Y/N: ").lower()
        if exit_choice == "y":
            os.system('cls' if os.name == 'nt' else 'clear')        
            sys.exit(0)
    else:
        continue

