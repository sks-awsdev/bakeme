#!/usr/bin/env python3

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/status", methods=["GET"])
def status():

    return jsonify({

        "relay": "OFF",
        "power": "ONLINE",
        "bake": "STOPPED",
        "remaining": "00:00:00"

    })


@app.route("/start", methods=["POST"])
def start():

    data = request.get_json()

    hours = data.get("hours", 0)
    minutes = data.get("minutes", 0)

    print(f"Start Bake : {hours}h {minutes}m")

    return jsonify({

        "success": True

    })


@app.route("/stop", methods=["POST"])
def stop():

    print("Stop Bake")

    return jsonify({

        "success": True

    })


@app.route("/powerlogs", methods=["GET"])
def powerlogs():

    return jsonify({

        "logs":[

            "11:10 ONLINE",

            "11:05 OFFLINE"

        ]

    })


if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )
