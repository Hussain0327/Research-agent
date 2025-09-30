Project: Newsletter AI Agent (Python)

What it does
- Plans a table of contents, researches with Tavily, drafts sections with inline citations, renders HTML via Jinja2, and can email the newsletter.

Quickstart
- Python 3.10+ recommended
- Create a venv and install deps:
  - python -m venv .venv
  - . .venv/bin/activate  # Windows: .venv\Scripts\activate
  - pip install -r requirements.txt
- Copy .env.example to .env and add keys
- Run:
  - python -m newsletter --topic "AI/ML/AGI" --tone "Professional" --audience "Dentist Offices"
- Outputs: `output/subject.txt`, `output/newsletter.html`

Environment variables (.env)
- OPENAI_API_KEY (if provider=openai)
- ANTHROPIC_API_KEY (if provider=anthropic)
- TAVILY_API_KEY (optional; improves research)
- LLM_PROVIDER=openai | anthropic (default openai)
- LLM_MODEL=gpt-4o-mini (or any supported model)
- MAX_WORDS=1000
- PER_SECTION_WORD_TARGET=180
- SMTP_HOST, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, SMTP_FROM (optional; for sending email)

CLI options
- --topic, --tone, --audience (required)
- --to (list of emails), --send-email (optional)
- --provider, --model, --output-dir (optional overrides)

Notes
- Tavily is optional; without a key, the pipeline runs but may cite fewer sources.
- The agent enforces concise sections and a global word cap.
- Use `python -m newsletter` as the entry point.

