Newsletter Generator (Python)

What this does
- Recreates your n8n flow in Python with a cleaner, configurable pipeline.
- Plans a table of contents, researches each section (Tavily), drafts sections with inline citations, assembles HTML, generates a title, and can email it.

Key improvements
- Modular architecture (LLM, search, email, templates).
- Config via .env and CLI flags.
- On-disk caching for Tavily queries.
- HTML templating with Jinja2 for consistent output.
- Word caps (<= 1000 words) with per-section targets.
- Pluggable LLM provider (OpenAI or Anthropic).

Quick start
1) Create and activate a Python 3.10+ env.
2) Install deps: `pip install -r requirements.txt`.
3) Copy `.env.example` to `.env` and fill your keys.
4) Run:
   `python -m newsletter --topic "AI/ML/AGI" --tone "Professional" --audience "Dentist Offices"`
5) Outputs written to `output/subject.txt` and `output/newsletter.html`.

Email sending (optional)
- Provide SMTP settings in `.env` and pass `--send-email --to you@example.com`.
- Works with Gmail via App Passwords (or any SMTP server).

Environment variables (.env)
- OPENAI_API_KEY=...
- ANTHROPIC_API_KEY=...
- TAVILY_API_KEY=...
- LLM_PROVIDER=openai | anthropic
- LLM_MODEL=gpt-4o-mini
- MAX_WORDS=1000
- PER_SECTION_WORD_TARGET=180
- SMTP_HOST=smtp.gmail.com
- SMTP_PORT=587
- SMTP_USERNAME=your@gmail.com
- SMTP_PASSWORD=app_password_or_smtp_password
- SMTP_FROM=Daily Newsletter <your@gmail.com>

Notes
- Tavily is optional; without a key the pipeline still runs but will cite fewer sources.
- The pipeline enforces brevity per section to help keep under 1000 words.
- You can switch providers/models with CLI flags, e.g. `--provider anthropic --model claude-3-5-sonnet-latest`.

