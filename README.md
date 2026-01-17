# Telegram Bot Using Python 🤖

A beginner-friendly Telegram Bot built using Python and the **python-telegram-bot** library.  
This project demonstrates how to create a Telegram bot, connect it with BotFather, handle commands, reply to users, and manage unknown inputs.

---

## 📌 Features

- Create a Telegram bot using BotFather
- Handle commands like `/start`, `/help`
- Send predefined links (YouTube, LinkedIn, Gmail, GeeksforGeeks)
- Handle unknown commands and random messages
- Simple and easy-to-understand Python code

---

## 📂 Project Structure

```
telegram-bot-python-basic/
│
├── main.py
├── requirements.txt
├── README.md
└── screenshot.png
```

---

## 🧰 Requirements

- Telegram Account
- Python 3.6.8 or higher
- python-telegram-bot library

---

## 📥 Installation

### Install using pip
```bash
pip install python-telegram-bot
```

### Or using conda
```bash
conda install -c conda-forge python-telegram-bot
```

---

## 🤖 Create Your Telegram Bot

1. Open **Telegram**
2. Search for **BotFather**
3. Start BotFather and type:
   ```
   /newbot
   ```
4. Enter:
   - Bot Name (any name)
   - Bot Username (must end with `bot`)
5. Copy the **API Token** provided by BotFather

---

## ⚙️ Setup Instructions

1. Clone this repository
```bash
git clone https://github.com/your-username/telegram-bot-python-basic.git
cd telegram-bot-python-basic
```

2. Open `main.py`
3. Replace this line:
```python
updater = Updater("YOUR_BOT_API_TOKEN", use_context=True)
```
with your **actual BotFather token**

---

## ▶️ Run the Bot

```bash
python main.py
```

Once running, your bot will start responding to messages on Telegram.

---

## 🧠 Available Commands

| Command | Description |
|-------|-------------|
| /start | Start the bot |
| /help | Show available commands |
| /youtube | Get YouTube URL |
| /linkedin | Get LinkedIn profile URL |
| /gmail | Get Gmail info |
| /geeks | Get GeeksforGeeks URL |

---

## 🛑 Handling Errors

- Unknown commands → Bot sends an error message
- Random text → Bot replies politely

---

## 📸 Screenshot

![Bot Screenshot](screenshot.png)

---

## 🚀 Technologies Used

- Python
- python-telegram-bot
- Telegram Bot API
