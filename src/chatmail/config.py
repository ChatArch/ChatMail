"Typed environment configuration for ChatMail."

from chatenv import BaseEnvConfig, EnvField


class ChatmailConfig(BaseEnvConfig):
    "ChatMail ChatEnv configuration."

    _title = "ChatMail Configuration"
    _aliases = ["chatmail"]
    _storage_dir = "Chatmail"

    @classmethod
    def test(cls) -> None:
        """Validate schema registration without external side effects."""

        print(f"Testing {cls._title}...")
        print("Schema loaded; no network test is required.")

    CHATMAIL_API_KEY = EnvField(
        "CHATMAIL_API_KEY",
        desc="API key",
        is_sensitive=True,
    )


__all__ = ["ChatmailConfig"]
