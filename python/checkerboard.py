import os
import time
from pythonosc import udp_client

ip = "10.100.5.129"
port = 5005
# ip = "10.100.7.28"
client = udp_client.SimpleUDPClient(ip, port)

DELAY = 0.025

buf = []


def main():
    while True:
        width = 96
        lineA = ("000000111111") * (width // 12)
        lineB = ("111111000000") * (width // 12)

        for i in range(3):
            buf.append(lineA)
            if len(buf) > 38:
                buf.pop(0)
                client.send_message("/aggregate", "".join(buf))
            print(lineA)
            time.sleep(DELAY)

        for i in range(3):
            buf.append(lineB)
            if len(buf) > 38:
                buf.pop(0)
                client.send_message("/aggregate", "".join(buf))
            print(lineB)
            time.sleep(DELAY)


try:
    main()
except KeyboardInterrupt:
    print("Checkerboard, by Al Sweigart al@inventwithpython.com")
