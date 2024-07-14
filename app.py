<<<<<<< HEAD
from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Path to the fine-tuned model
model_path = "./finetuned_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

# Add a padding token
tokenizer.pad_token = tokenizer.eos_token

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get", methods=["POST"])
def chat():
    try:
        msg = request.form["msg"]
        logging.debug(f"Received message: {msg}")
        response = get_chat_response(msg)
        logging.debug(f"Generated response: {response}")
        return response
    except Exception as e:
        logging.error(f"Error in chat endpoint: {str(e)}")
        return "Error: " + str(e), 500

def get_chat_response(text):
    try:
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        outputs = model.generate(inputs.input_ids, max_length=100)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    except Exception as e:
        logging.error(f"Error in get_chat_response: {str(e)}")
        return "Error: " + str(e)

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False
=======
from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Path to the fine-tuned model
model_path = "./finetuned_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

# Add a padding token
tokenizer.pad_token = tokenizer.eos_token

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get", methods=["POST"])
def chat():
    try:
        msg = request.form["msg"]
        logging.debug(f"Received message: {msg}")
        response = get_chat_response(msg)
        logging.debug(f"Generated response: {response}")
        return response
    except Exception as e:
        logging.error(f"Error in chat endpoint: {str(e)}")
        return "Error: " + str(e), 500

def get_chat_response(text):
    try:
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        outputs = model.generate(inputs.input_ids, max_length=100)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    except Exception as e:
        logging.error(f"Error in get_chat_response: {str(e)}")
        return "Error: " + str(e)

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False
>>>>>>> 6000d4c4d433697fd933fc82e125af8c55b5fed5
