# Processed Document Calendar Event Extractor

Process to extract calendar events from unstructured {loose) marked down files using a local LLM (via Ollama), and push them to Google Calendar.

## Setup

1. Clone the repo
2. Install dependencies:

```bash
pip install -r requirements.txt

Enable Google Calendar API and place your credentials.json in the root.
Drop .md files into the watched_dir/ folder.

python process_events.py

or run the real-time watcher:
python watcher.py