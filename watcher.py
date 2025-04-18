import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from event_extractor_llm import extract_event_with_llm
from calendar_api import add_event_to_google_calendar

class MarkdownHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".md"):
            with open(event.src_path, 'r') as f:
                text = f.read()
                events = extract_event_with_llm(text)
                for event in events:
                    add_event_to_google_calendar(event)

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(MarkdownHandler(), path="watched_dir", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
