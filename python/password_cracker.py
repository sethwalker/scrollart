import subprocess
from pathlib import Path

from PIL import Image

from pythonosc import udp_client

ip = "10.100.5.129"
port = 5005
client = udp_client.SimpleUDPClient(ip, port)


def greg_say(text_to_render):
    FONT_PATH = Path(
        "/Users/sethwalker/dev/rc/scrollart/python/font-undead-pixel-8.ttf"
    )
    TMP_OUT_PATH = Path("/tmp/out.png")

    subprocess.run(
        [
            "convert",
            "-background",
            "black",
            "-fill",
            "white",
            "-size",
            "96x38",
            "-pointsize",
            "8",
            "-font",
            # absolute path to font
            FONT_PATH.resolve(),
            f"caption:{text_to_render}",
            "/tmp/out.png",
        ]
    )

    im = Image.open(TMP_OUT_PATH)
    pixels = ["1" if pixel else "0" for pixel in im.getdata()]
    client.send_message("/aggregate", "".join(pixels))
    return "".join(pixels)


import random, time, os, sys

os.system("cls | clear")

MESSAGE = "           Recurse          Center        ALGORAVE           DANCE"
DELAY = 0.035
CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
UNLOCK_CHAR_PROBABILITY = 0.04
SPACER = " "

try:
    locked_columns = [False] * len(MESSAGE)

    while True:
        columns = [random.choice(CHARS) for i in range(len(MESSAGE))]

        if random.random() < UNLOCK_CHAR_PROBABILITY:
            while True:
                r = random.randint(0, len(MESSAGE) - 1)
                if locked_columns[r] == False:
                    locked_columns[r] = True
                    break  # Found an unlocked column, so break out of the loop.

        if all(locked_columns):
            # Done, print the message a few more times and then quit:
            for i in range(10):
                print(SPACER.join(MESSAGE))
                time.sleep(DELAY)
            print("Password Cracker, by Al Sweigart al@inventwithpython.com 2024")
            sys.exit()

        for i, is_locked in enumerate(locked_columns):
            if is_locked:
                columns[i] = MESSAGE[i]

        print(SPACER.join(columns))
        greg_say(SPACER.join(columns))
        time.sleep(DELAY)

except KeyboardInterrupt:
    print("Password Cracker, by Al Sweigart al@inventwithpython.com 2024")
