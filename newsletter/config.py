from __future__ import annotations

import os
from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # LLM
    llm_provider: str = Field("openai", description="openai or anthropic")
    llm_model: str = Field("gpt-4o-mini", description="Model name for chosen provider")
    openai_api_key: str | None = Field(default=None)
    anthropic_api_key: str | None = Field(default=None)

    # Tavily
    tavily_api_key: str | None = Field(default=None)
    tavily_endpoint: str = Field("https://api.tavily.com/search")
    tavily_max_results: int = 3

    # Output & limits
    max_words: int = 1000
    per_section_word_target: int = 180

    # Email (SMTP)
    smtp_host: str | None = None
    smtp_port: int = 587
    smtp_username: str | None = None
    smtp_password: str | None = None
    smtp_from: str | None = None

    # Misc
    log_level: str = Field("INFO")
    output_dir: str = Field("output")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    def validate_provider_keys(self) -> None:
        if self.llm_provider.lower() == "openai" and not self.openai_api_key:
            self.openai_api_key = os.getenv("OPENAI_API_KEY")
        if self.llm_provider.lower() == "anthropic" and not self.anthropic_api_key:
            self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

