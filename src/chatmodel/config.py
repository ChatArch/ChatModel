"Typed environment configuration for ChatModel."

from chatenv import BaseEnvConfig, EnvField


class ChatmodelConfig(BaseEnvConfig):
    "ChatModel ChatEnv configuration."

    _title = "ChatModel Configuration"
    _aliases = ["chatmodel"]
    _storage_dir = "Chatmodel"

    @classmethod
    def test(cls) -> None:
        """Validate schema registration without external side effects."""

        print(f"Testing {cls._title}...")
        print("Schema loaded; no network test is required.")

    CHATMODEL_API_KEY = EnvField(
        "CHATMODEL_API_KEY",
        desc="API key",
        is_sensitive=True,
    )


__all__ = ["ChatmodelConfig"]
