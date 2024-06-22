import time, os
from pythonosc import udp_client


WIDTH = 96
DELAY = 0.002


EMPTY_CHAR = "0"
SWEEP_CHAR = "1"

ip = "10.100.7.28"
port = 12000
client = udp_client.SimpleUDPClient(ip, port)

os.system("cls | clear")
buf = []

try:
    pos = 0

    columns = [EMPTY_CHAR] * WIDTH
    sweepOn = True
    while True:
        if sweepOn:
            columns[pos] = SWEEP_CHAR
        else:
            columns[pos] = EMPTY_CHAR

        pos += 1
        if pos >= WIDTH:
            pos = 0
            sweepOn = not sweepOn

        buf.append("".join(columns))
        if len(buf) > 38:
            buf.pop(0)
            client.send_message("/diagonalsweep", "".join(buf))
        print("".join(columns))
        time.sleep(DELAY)

except KeyboardInterrupt:
    print("Diagonal Sweep, by Al Sweigart al@inventwithpython.com 2024")
