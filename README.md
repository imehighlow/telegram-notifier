# telegram-notifier

## Minimal helper to send Telegram messages.

Install

```bash
pip install git+https://github.com/imehighlow/telegram-notifier.git
```

Usage

```python
import os
from telegram_notifier import TelegramNotifier

token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

# default service name
notifier = TelegramNotifier(token=token, chat_id=chat_id, service_name="my-service")

# plain message
notifier.send_message("Hello from my script")

# log-style with default sender (service_name)
notifier.send_log_message("info", "Started successfully")

# log-style with custom sender override
notifier.send_log_message("warning", "Something happened", sender="another-sender")
```

