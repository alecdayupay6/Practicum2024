from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()

# configure OpenAI with the API key
connection = OpenAI()

# configure our Flask app
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# main route in our code, loading our index.html page
@app.route("/")
def index():
    return render_template("index.html")

# handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # get the message from the POST request
    message = request.json.get("message")
    if not message:
        return jsonify({"error": "No message provided"}), 400
    
    initial_prompts = [
        {
            "role": "system",
            "content": "You are a 26-year-old man from the Philippine slums. Use Filipino slang to communicate your medical history."
        },
        {
            "role": "user",
            "content": "Sige po, doc. Ready na po ako mag-usap."
        },
        {
            "role": "assistant",
            "content": "Hi, doc. Kamusta po? Ako nga pala si Jun, 26 years old. May mga nararamdaman kasi akong kakaiba lately kaya pumunta ako dito."
        },
        {
            "role": "user",
            "content": message
        }
    ]
    completion = connection.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=initial_prompts
    )
    response = completion.choices[0].message.content
    return jsonify({"content": response})

if __name__ == '__main__':
    app.run(debug=True)
