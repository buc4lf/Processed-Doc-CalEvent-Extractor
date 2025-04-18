import os
from event_extractor_llm import extract_event_with_llm
from calendar_api import add_event_to_google_calendar

WATCHED_DIR = "watched_dir"

def main():
    for filename in os.listdir(WATCHED_DIR):
        if filename.endswith(".md"):
            filepath = os.path.join(WATCHED_DIR, filename)
            with open(filepath, 'r') as f:
                text = f.read()
                events = extract_event_with_llm(text)
                for event in events:
                    add_event_to_google_calendar(event)

if __name__ == "__main__":
    main()
