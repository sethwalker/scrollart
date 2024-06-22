import random, math, os, time
from pythonosc import udp_client

# ip = "10.100.7.28"
# port = 12000
ip = "10.100.5.129"
port = 5005
client = udp_client.SimpleUDPClient(ip, port)

WIDTH = 96
DELAY = 0.03
THORN_CHAR = "1"

LEVELS = [1, 1, 1, 1, 1, 1, 1, 3, 6]
MULTIPLIER = 10

buf = []

try:
    while True:
        line_length = int(random.choice(LEVELS) * ((random.random() + 1) * MULTIPLIER))
        line = THORN_CHAR * line_length

        if len(line) > WIDTH:
            line = THORN_CHAR * WIDTH

        buf.append(line.center(WIDTH, "0"))
        if len(buf) > 38:
            buf.pop(0)
            client.send_message("/aggregate", "".join(buf))
        print(line.center(WIDTH))
        time.sleep(DELAY)

except KeyboardInterrupt:
    print("Thorns, by Al Sweigart al@inventwithpython.com 2024")
