
import subprocess
import time
import json
import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class RestartOnChangeHandler(FileSystemEventHandler):
    def __init__(self, runner):
        self.runner = runner

    def on_modified(self, event):
        if self.runner.should_watch(event.src_path):
            print(f"[Watcher] Detected change in {event.src_path}")
            self.runner.restart()

class DevRunner:
    def __init__(self, entry='main.py', watch_exts=['.py'], exclude=[], debounce=0.5, verbose=True):
        self.entry = entry
        self.watch_exts = watch_exts
        self.exclude = exclude
        self.debounce = debounce
        self.verbose = verbose
        self.process = None

    def should_watch(self, path):
        if any(excl in path for excl in self.exclude):
            return False
        return any(path.endswith(ext) for ext in self.watch_exts)

    def run(self):
        if self.verbose:
            print(f"[Runner] Launching {self.entry}")
        self.process = subprocess.Popen([sys.executable, self.entry])

    def restart(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
        time.sleep(self.debounce)
        self.run()

    def start(self):
        self.run()
        observer = Observer()
        handler = RestartOnChangeHandler(self)
        observer.schedule(handler, path=os.getcwd(), recursive=True)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            if self.process:
                self.process.terminate()
        observer.join()

def load_config(path):
    with open(path) as f:
        return json.load(f)
