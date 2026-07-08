#!/usr/bin/env python3

import subprocess


BAKEON = "/usr/local/bin/bakeon"
BAKEOFF = "/usr/local/bin/bakeoff"


def relay_on():

    try:

        subprocess.run(
            [BAKEON],
            check=True
        )

        return True

    except Exception as e:

        print(e)

        return False


def relay_off():

    try:

        subprocess.run(
            [BAKEOFF],
            check=True
        )

        return True

    except Exception as e:

        print(e)

        return False


if __name__ == "__main__":

    print("Testing Relay")

    relay_on()

    relay_off()
