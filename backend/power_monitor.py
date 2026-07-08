#!/usr/bin/env python3

"""
BakeMe Power Monitor
--------------------

Monitors GPIO89.

Detects

ONLINE
OFFLINE

Logs every transition.

"""

import os
import csv
import time

from datetime import datetime


GPIO = 89

GPIO_PATH = "/sys/class/gpio"

LOG_DIR = "data"

LOG_FILE = os.path.join(

    LOG_DIR,

    "power.log"

)


class PowerMonitor:

    def __init__(self):

        os.makedirs(

            LOG_DIR,

            exist_ok=True

        )

        self.export_gpio()

        self.set_input()

        self.previous = self.read_gpio()

        self.create_log_file()


    # -------------------------
    # Export GPIO
    # -------------------------

    def export_gpio(self):

        if not os.path.exists(

            f"{GPIO_PATH}/gpio{GPIO}"

        ):

            with open(

                f"{GPIO_PATH}/export",

                "w"

            ) as f:

                f.write(str(GPIO))


    # -------------------------
    # Direction
    # -------------------------

    def set_input(self):

        with open(

            f"{GPIO_PATH}/gpio{GPIO}/direction",

            "w"

        ) as f:

            f.write("in")


    # -------------------------
    # Read GPIO
    # -------------------------

    def read_gpio(self):

        with open(

            f"{GPIO_PATH}/gpio{GPIO}/value",

            "r"

        ) as f:

            return f.read().strip()


    # -------------------------
    # Create CSV
    # -------------------------

    def create_log_file(self):

        if os.path.exists(LOG_FILE):

            return

        with open(

            LOG_FILE,

            "w",

            newline=""

        ) as file:

            writer = csv.writer(file)

            writer.writerow(

                [

                    "Timestamp",

                    "Status"

                ]

            )
