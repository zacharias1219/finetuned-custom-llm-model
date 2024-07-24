# Intel Final Project

This project is a Flask-based web application that integrates a fine-tuned language model to provide conversational AI capabilities. The application uses HTML, CSS, and JavaScript for the front-end, and Python for the back-end, leveraging the `transformers` library for model handling.

## Features

- Interactive chat interface with a chatbot.
- Fine-tuned language model for generating responses.
- Dockerized deployment for easy setup and scaling.
- Dark-themed UI with responsive design.

## Prerequisites

- Python 3.7 or higher
- Docker (optional, for containerized deployment)
- NVIDIA GPU with CUDA (optional, for faster inference)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/zacharias1219/finetuned-custom-llm-model.git
cd finetuned-custom-llm-model
```

### 2. Set Up the Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install the Required Packages

```bash
pip install -r requirements.txt
```

### 4. Download and Place the Fine-Tuned Model

Place your fine-tuned model files in a directory named `finetuned_model` within the project directory. Ensure the directory contains the following files:

- `config.json`
- `generation_config.json`
- `model-00001-of-00006.safetensors`
- `model-00002-of-00006.safetensors`
- `model-00003-of-00006.safetensors`
- `model-00004-of-00006.safetensors`
- `model-00005-of-00006.safetensors`
- `model-00006-of-00006.safetensors`
- `model.safetensors.index.json`
- `special_tokens_map.json`
- `tokenizer_config.json`
- `tokenizer.json`
- `tokenizer.model`

### 5. Run the Application

```bash
python app.py
```

Open your web browser and navigate to `http://127.0.0.1:5000` to interact with the chatbot.

## Docker Deployment

### 1. Build the Docker Image

```bash
docker build -t chatbot-app .
```

### 2. Run the Docker Container

```bash
docker run -p 5000:5000 chatbot-app
```

Open your web browser and navigate to `http://127.0.0.1:5000` to interact with the chatbot.

## Usage

1. Start the application by running `python app.py` or using Docker as described above.
2. Open your web browser and go to `http://127.0.0.1:5000`.
3. Type your message in the chat interface and press the send button to interact with the chatbot.

## Project Structure

```bash
├── app.py                     # Main application file
├── Dockerfile                 # Dockerfile for containerized deployment
├── requirements.txt           # Python dependencies
├── templates
│   └── chat.html              # HTML template for the chat interface
├── static
│   ├── styles.css             # CSS file for styling
│   └── images                 # Directory for image assets
└── finetuned_model            # Directory containing the fine-tuned model files
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)

There are some file that are missing as it is too big to upload on github so here are the photos

![Screenshot 2024-07-14 223850](https://github.com/user-attachments/assets/1a38ffa4-5825-4f8f-8e6e-a1055fdcde8d)

![Screenshot 2024-07-14 223857](https://github.com/user-attachments/assets/61f6b0b3-dd31-48ad-aeca-b66f3febc072)
