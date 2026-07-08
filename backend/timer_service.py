#!/usr/bin/env python3

import time
import threading
from datetime import datetime, timedelta

from relay import relay_on
from relay import relay_off

from state import StateManager


class BakeTimer:

    def __init__(self):

        self.state = StateManager()

        self.running = False

        self.remaining_seconds = 0

        self.thread = None


    # ----------------------------
    # Load Previous State
    # ----------------------------

    def load_state(self):

        data = self.state.load()

        self.running = data["running"]

        self.remaining_seconds = data["remaining_seconds"]

        return data


    # ----------------------------
    # Save Current State
    # ----------------------------

    def save_state(self):

        data = self.state.load()

        data["running"] = self.running

        data["remaining_seconds"] = self.remaining_seconds

        self.state.save(data)


    # ----------------------------
    # Format Time
    # ----------------------------

    @staticmethod
    def format_time(seconds):

        hours = seconds // 3600

        minutes = (seconds % 3600) // 60

        secs = seconds % 60

        return f"{hours:02}:{minutes:02}:{secs:02}"    # ----------------------------
    # Start Bake
    # ----------------------------

    def start_bake(self, hours, minutes):

        if self.running:
            return

        self.remaining_seconds = (hours * 3600) + (minutes * 60)

        self.running = True

        relay_on()

        data = self.state.load()

        data["running"] = True
        data["relay"] = True
        data["hours"] = hours
        data["minutes"] = minutes
        data["remaining_seconds"] = self.remaining_seconds

        data["started_time"] = datetime.now().strftime("%H:%M:%S")

        finish = datetime.now() + timedelta(seconds=self.remaining_seconds)

        data["finish_time"] = finish.strftime("%H:%M:%S")

        self.state.save(data)

        print("Bake Started")


    # ----------------------------
    # Stop Bake
    # ----------------------------

    def stop_bake(self):

        if not self.running:
            return

        relay_off()

        self.running = False

        self.remaining_seconds = 0

        data = self.state.load()

        data["running"] = False
        data["relay"] = False
        data["remaining_seconds"] = 0

        self.state.save(data)

        print("Bake Stopped")


    # ----------------------------
    # Resume After Reboot
    # ----------------------------

    def resume_after_reboot(self):

        data = self.load_state()

        if not data["running"]:
            return

        if data["remaining_seconds"] <= 0:
            return

        self.running = True

        self.remaining_seconds = data["remaining_seconds"]

        relay_on()

        print(

            "Resuming Bake",

            self.format_time(self.remaining_seconds)    # ----------------------------
    # Countdown Engine
    # ----------------------------

    def countdown(self):

        while self.running:

            if self.remaining_seconds <= 0:

                print("Bake Completed")

                relay_off()

                self.running = False

                data = self.state.load()

                data["running"] = False
                data["relay"] = False
                data["remaining_seconds"] = 0

                self.state.save(data)

                break

            time.sleep(1)

            self.remaining_seconds -= 1

            data = self.state.load()

            data["remaining_seconds"] = self.remaining_seconds

            self.state.save(data)

            print(

                "Remaining:",

                self.format_time(self.remaining_seconds)

            )


    # ----------------------------
    # Start Countdown Thread
    # ----------------------------

    def start_thread(self):

        if self.thread is not None:

            if self.thread.is_alive():

                return

        self.thread = threading.Thread(

            target=self.countdown,

            daemon=True

        )

        self.thread.start()    # ----------------------------
    # Run Timer
    # ----------------------------

    def run(self):

        print("Bake Timer Service Started")

        self.resume_after_reboot()

        if self.running:

            self.start_thread()

        try:

            while True:

                time.sleep(1)

        except KeyboardInterrupt:

            print("Timer Service Stopped")


# --------------------------------
# Main Entry
# --------------------------------

if __name__ == "__main__":

    timer = BakeTimer()

    timer.run()

        )
      
      
      
