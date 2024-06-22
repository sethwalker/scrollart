import random, os, time, math
from pythonosc import udp_client

ip = "10.100.5.129"
port = 5005
# ip = "10.100.7.28"
# port = 12000
client = udp_client.SimpleUDPClient(ip, port)

os.system("cls | clear")  # Clear the screen

EMPTY = "0"
DELAY = 0.03

CHARS = ["1", "1", "1", "1", "1"]
SINE_STEP_INCS = []
sine_steps = []
for i in range(random.randint(7, 15)):
    # CHARS.append(random.choice('@O0o*.,vV'))
    SINE_STEP_INCS.append(random.random() * 0.1 + 0.0001)
    sine_steps.append(random.random() * math.pi)

WIDTH = 96  # os.get_terminal_size()[0] - 1

buf = []

try:
    while True:
        row = [EMPTY] * WIDTH

        for i in range(len(CHARS)):
            row[int((math.sin(sine_steps[i]) + 1) / 2 * WIDTH)] = CHARS[i]
            sine_steps[i] += SINE_STEP_INCS[i]

        print("".join(row))
        buf.append("".join(row))
        if len(buf) > 38:
            buf.pop(0)
            client.send_message("/aggregate", "".join(buf))

        time.sleep(DELAY)
except KeyboardInterrupt:
    print("Helix Travels, by Al Sweigart al@inventwithpython.com 2024")
