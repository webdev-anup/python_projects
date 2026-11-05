# 🤖 Gemini ChatBot

A simple command-line chatbot built with Python and the Google Gemini API. Type a question in the terminal and get an AI response instantly.

## ✨ Features

- Chat with Gemini directly from your terminal
- Automatic retry with exponential backoff when the server is busy (503)
- Clear error messages instead of crashes (invalid key, model not found, quota exceeded)
- API key stored safely in a `.env` file
- Type `quit` to exit

## 🛠️ Tech Stack

- Python 3.10+
- [google-genai](https://pypi.org/project/google-genai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## 📁 Project Structure

```
Gemini ChatBot/
├── main.py
├── .env
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd "Gemini ChatBot"
```

### 2. Install dependencies

```bash
pip install google-genai python-dotenv
```

### 3. Get a Gemini API key

Create a free API key from [Google AI Studio](https://aistudio.google.com/apikey).

### 4. Create a `.env` file

In the project folder, create a file named `.env`:

```
GEMINI_API_KEY="your-api-key-here"
```

> ⚠️ Never share your API key or commit `.env` to GitHub. Add `.env` to your `.gitignore`.

### 5. Run the chatbot

```bash
python main.py
```

## 💬 Usage

```
You: hey, can you help me with Python?
Gemini: Of course! What do you need help with?
You: quit
```

## 🔧 How It Works

1. `load_dotenv()` reads the API key from `.env`.
2. The user's question is sent to the Gemini model using `client.models.generate_content()`.
3. If the server returns a `503` error, the request is retried up to 4 times, waiting 1s, 2s, 4s and 8s.
4. Other errors (such as `404` or `429`) are caught and printed as a readable message.

## 🐛 Troubleshooting

| Error | Meaning | Fix |
|-------|---------|-----|
| `503 UNAVAILABLE` | Google's servers are busy | Wait a bit and try again |
| `404 NOT_FOUND` | Model name is wrong or retired | Update `MODEL` in `main.py` |
| `KeyError: GEMINI_API_KEY` | `.env` not loaded or key missing | Check `.env` and that `load_dotenv()` is called |
| `429` | Quota exceeded | Wait or check your usage limits |

## 🔮 Future Improvements

- Remember chat history (multi-turn conversation)
- Streaming responses
- Simple web UI

## 📄 License

This project is open source and free to use for learning.