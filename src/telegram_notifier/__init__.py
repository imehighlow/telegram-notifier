import requests
from datetime import datetime


class TelegramNotifier:
    def __init__(self, token, chat_id, service_name=None):
        self.token = token
        self.chat_id = chat_id
        self.service_name = service_name

    def send_message(self, message, chat_id=None):
        target_chat_id = chat_id or self.chat_id
        if not target_chat_id:
            raise ValueError(
                "chat_id must be provided either in __init__ or send_message method")

        # Handle username format (only for non-numeric strings)
        if isinstance(target_chat_id, str) and not target_chat_id.startswith('@') and not target_chat_id.lstrip('-').isdigit():
            target_chat_id = f"@{target_chat_id}"

        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        data = {
            "chat_id": target_chat_id,
            "text": message
        }
        response = requests.post(url, json=data)
        return response.json()

    def send_log_message(self, level, log_message, chat_id=None, sender=None):
        sender = sender or self.service_name
        if not sender:
            sender = ""

        level = level.lower()
        level_emojis = {
            "debug": "🔍",
            "info": "ℹ️",
            "warning": "⚠️",
            "error": "❌",
            "critical": "‼️"
        }
        emoji = level_emojis.get(level, "📝")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"{emoji} [{level.upper()}] {sender}\n{timestamp}\n{log_message}"
        return self.send_message(formatted_message, chat_id=chat_id)

    def critical(self, message, chat_id=None, sender=None):
        return self.send_log_message("critical", message, chat_id=chat_id, sender=sender)

    def debug(self, message, chat_id=None, sender=None):
        return self.send_log_message("debug", message, chat_id=chat_id, sender=sender)

    def error(self, message, chat_id=None, sender=None):
        return self.send_log_message("error", message, chat_id=chat_id, sender=sender)

    def info(self, message, chat_id=None, sender=None):
        return self.send_log_message("info", message, chat_id=chat_id, sender=sender)

    def warning(self, message, chat_id=None, sender=None):
        return self.send_log_message("warning", message, chat_id=chat_id, sender=sender)
