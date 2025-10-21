# Newsletter AI Agent

Generate research-backed newsletters from a topic. Plans sections, pulls citations from Tavily, and renders clean HTML.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

cp .env.example .env
# Add your OPENAI_API_KEY or ANTHROPIC_API_KEY
```

## Usage

```bash
python -m newsletter \
  --topic "AI/ML developments" \
  --tone "Professional" \
  --audience "Researchers"
```

Outputs `newsletter.html` and `subject.txt` to the `output/` folder.

### CLI Options

```bash
--topic TEXT                   # Required
--tone TEXT                    # Required  
--audience TEXT                # Required
--provider {openai,anthropic}  # Default: openai
--model TEXT                   # Default: gpt-4o-mini
--output-dir PATH             # Default: ./output
--to EMAIL [EMAIL ...]        # Email recipients
--send-email                  # Actually send (needs SMTP config)
```

Full options: `python -m newsletter -h`

## Configuration

Edit `.env`:

```ini
# LLM (pick one)
OPENAI_API_KEY=sk-...
# ANTHROPIC_API_KEY=...

LLM_PROVIDER=openai
LLM_MODEL=gpt-4o-mini

# Optional - adds inline citations
TAVILY_API_KEY=tvly-...

# Content limits
MAX_WORDS=1000
PER_SECTION_WORD_TARGET=180

# Email (optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=you@gmail.com
SMTP_PASSWORD=your-app-password
SMTP_FROM=Your Name <you@gmail.com>
```

## View Output

```bash
# Local server
python -m http.server --directory output 8000
# Open http://127.0.0.1:8000/newsletter.html

# Or just open it
open output/newsletter.html        # macOS
xdg-open output/newsletter.html    # Linux
start output\newsletter.html       # Windows
```

## Customize

Edit `newsletter/templates/newsletter.html.j2` for branding, colors, and layout.

Tune content limits in `.env`:
- `MAX_WORDS` - global cap
- `PER_SECTION_WORD_TARGET` - per section

For email clients (Gmail/Outlook), convert to MJML or inline-CSS tables before sending at scale.

## Email Sending

Configure SMTP in `.env`, then:

```bash
python -m newsletter \
  --topic "Weekly Update" \
  --tone "Professional" \
  --audience "Subscribers" \
  --to alice@example.com bob@example.com \
  --send-email
```

For Gmail, use an [app password](https://support.google.com/accounts/answer/185833).

### Test Locally (No Real Emails)

```bash
pip install aiosmtpd
python -m aiosmtpd -n -l 127.0.0.1:1025 &

export SMTP_HOST=127.0.0.1 SMTP_PORT=1025 SMTP_USERNAME=test SMTP_PASSWORD=test SMTP_FROM="Test <test@example.com>"

python -m newsletter --topic "Test" --tone "Casual" --audience "Testing" \
  --to test@example.com --send-email

# Kill the test server when done
```

## GitHub Pages

```bash
mkdir -p docs
cp output/newsletter.html docs/index.html
git add docs/
git commit -m "Publish newsletter"
git push

# Settings → Pages → Source: main branch /docs folder
```

Or use `gh-pages` branch:

```bash
git checkout --orphan gh-pages
git rm -rf .
cp output/newsletter.html index.html
git add index.html
git commit -m "Publish newsletter"
git push -u origin gh-pages

# Settings → Pages → Source: gh-pages branch
```

## Project Structure

```
.
├── .cache/
│   └── tavily/           # Cached search results
├── newsletter/
│   ├── __main__.py       # CLI entry
│   ├── config.py         # Load .env
│   ├── pipeline.py       # Main orchestration
│   ├── llm.py           # OpenAI/Anthropic client
│   ├── search.py        # Tavily integration
│   ├── emailer.py       # SMTP sender
│   ├── models.py        # Data models
│   └── templates/
│       └── newsletter.html.j2
└── output/
    ├── newsletter.html
    └── subject.txt
```

## Troubleshooting

**ModuleNotFoundError**  
You're not in the virtualenv: `source .venv/bin/activate`

**Tavily 401**  
Bad API key. Fix it or `unset TAVILY_API_KEY` to skip research.

**WARNING: No TAVILY_API_KEY set**  
Expected if you didn't set one. Research is optional.

**Files not created**  
API call probably failed. Check the error output.

**404 on local server**  
Make sure you're in the repo root and serving the `output/` directory.

**Virtualenv confusion**  
Check you're using the right Python: `which python` should show `.venv/bin/python`

## Development

```bash
black newsletter/
ruff check newsletter/
mypy newsletter/
```

---
