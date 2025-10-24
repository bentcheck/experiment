# /infra/runtime.py
from __future__ import annotations
from typing import Optional

class Runtime:
    _base_url: Optional[str] = None

    _ENV_TO_URL = {
        "dev":  "https://dev.example.local",
        "qa":   "https://qa.example.local",
        "prod": "https://app.example.com",
    }

    @classmethod
    def set_env(cls, env: str) -> None:
        env = env.strip()
        if env.startswith(("http://", "https://")):
            url = env
        else:
            key = env.lower()
            if key not in cls._ENV_TO_URL:
                raise ValueError(
                    f"Unknown env '{env}'. Known: {list(cls._ENV_TO_URL)} "
                    f"or pass a full URL."
                )
            url = cls._ENV_TO_URL[key]
        cls._base_url = url.rstrip("/")

    @classmethod
    def base_url(cls) -> str:
        if not cls._base_url:
            raise RuntimeError(
                "Base URL not set. Call Runtime.set_env('<env or url>') first in your test."
            )
        return cls._base_url

    @classmethod
    def reset(cls) -> None:
        cls._base_url = None
