# Chatbot (Django + Ollama)

This repository contains a small Django-based chatbot that communicates with a locally-hosted LLM via Ollama. The app demonstrates how to call a local model from Django, keep data private on your machine, and add basic safety/hardening around prompts and outputs.

**Quick overview**
- **Framework:** Django
- **Local LLM host:** Ollama (HTTP API at `http://localhost:11434/api/chat`)
- **Example model identifier used:** `llama3.2:3b` (changeable in `chat/ai_service.py`)

**Files of interest**
- `chat/ai_service.py`: wrapper that posts messages to the Ollama HTTP API.
- `chat/views.py`, `chat/templates/chat.html`: minimal UI and view code (chat page).
- `.gitignore`: ignores `myenv/`, `.env`, `db.sqlite3`, and editor files.

**Prerequisites**
- Python 3.10+ (project's virtualenv uses Python 3.14 in this workspace)
- Ollama installed and running locally (see Ollama docs)
- Recommended: a Python virtual environment

Getting started
---------------

1. Create and activate a virtualenv (if you haven't already):

```bash
python -m venv myenv
source myenv/bin/activate
```

2. Install required Python packages (this project uses `requests`):

```bash
pip install -r requirements.txt
# or, if you don't have requirements.txt:
pip install requests
```

3. Start Ollama locally and ensure the server is reachable at `http://localhost:11434`.
   - Use `ollama list` to see available/installed models.
   - Pull or install a model that you trust (for example: `llama3.2:3b`) according to Ollama docs.

4. Configure environment variables (optional):

Create a `.env` file or export env vars in your shell (this repo ignores `.env` by default):

```bash
export OLLAMA_URL="http://localhost:11434/api/chat"
export MODEL="llama3.2:3b"
```

5. Run migrations and start the Django dev server:

```bash
python manage.py migrate
python manage.py runserver
```

Usage
-----

- The `ask_ai(prompt)` helper in `chat/ai_service.py` demonstrates how to format a chat payload and POST it to the Ollama API. Update the `MODEL` constant there if you want to use a different model identifier.
- The web UI is available at the URL served by Django (check `chat/urls.py` and `ChatBot/urls.py`).

Safety and privacy notes
------------------------

- Download Ollama only from official sources and verify checksums/signatures when available.
- Running models locally improves privacy because prompts don't leave your machine; however, models can still produce unsafe content — add moderation.
- Add moderation and input validation:
  - Use a moderation API or a local classifier to inspect outputs for disallowed content.
  - Use restrictive system prompts, set lower `temperature` and limit `max_tokens`.
- Keep sensitive data out of logs and use secure storage for secrets.

Model selection guidance
------------------------

- A model labeled `3b` is relatively small and may hallucinate more than larger, instruction-tuned models. For higher-quality and safer outputs prefer a well-tested, instruction-tuned model.
- Verify model license and provenance before production use.

