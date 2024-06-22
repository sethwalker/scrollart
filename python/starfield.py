import random, time, os
from pythonosc import udp_client


DELAY = 0.02


def main():
    buf = []
    # ip = "10.100.7.28"
    ip = "10.100.5.129"
    port = 5005
    client = udp_client.SimpleUDPClient(ip, port)

    change_amount = 0.5
    density = 0.0
    while True:
        width = 96
        if density < 0 or density > 70:
            change_amount *= -1
        density = density + change_amount

        line = ""
        for i in range(width):
            if random.randint(0, 100) < density:
                line = line + "1"
            else:
                line = line + "0"

        buf.append(line)
        if len(buf) > 38:
            buf.pop(0)
            if len("".join(buf)) == 3648:
                client.send_message("/aggregate", "".join(buf))
            else:
                print(buf, len("".join(buf)))
                exit("you suck")

        #        osc.send("".join(buf)
        print("\n".join(buf))

        time.sleep(DELAY)


try:
    main()
except KeyboardInterrupt:
    print("Starfield, by Al Sweigart al@inventwithpython.com 2022")
