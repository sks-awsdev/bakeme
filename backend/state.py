#!/usr/bin/env python3

import json
import os

STATE_FILE = "data/bake_state.json"


DEFAULT_STATE = {
    "running": False,
    "relay": False,
    "power": "ONLINE",
    "hours": 0,
    "minutes": 0,
    "remaining_seconds": 0,
    "started_time": "",
    "finish_time": ""
}


class StateManager:

    def __init__(self):

        self.file = STATE_FILE

        os.makedirs(os.path.dirname(self.file), exist_ok=True)

        if not os.path.exists(self.file):
            self.save(DEFAULT_STATE)

    def load(self):

        try:

            with open(self.file, "r") as f:

                return json.load(f)

        except Exception:

            return DEFAULT_STATE.copy()

    def save(self, state):

        with open(self.file, "w") as f:

            json.dump(state, f, indent=4)

    def update(self, key, value):

        state = self.load()

        state[key] = value

        self.save(state)

    def reset(self):

        self.save(DEFAULT_STATE)


if __name__ == "__main__":

    manager = StateManager()

    print(manager.load())
