from flask import Flask, jsonify
import random

app = Flask(__name__, static_folder='static')

prompts = [
    "A dreamy galaxy queen riding a dolphin through space",
    "An ancient tarot priestess floating above a waterfall",
    "Cosmic neon jungle with crystal wolves under a blood moon",
    "Art deco goddess in a golden temple, soft lighting",
    "Mystical forest oracle with glowing hair, cinematic shot"
]

@app.route("/spin")
def spin():
    prompt = random.choice(prompts)
    return jsonify({
        "prompt": prompt,
        "image_url": "/static/kitten.jpg"
    })

@app.route("/")
def index():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(debug=True)