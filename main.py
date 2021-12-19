import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class OszFileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        osu_path = "/Applications/osu!.app/Contents/Resources/drive_c/osu!/Songs"
        if not event.is_directory:
            if event.src_path[-4:] == ".osz":
                zip_name = event.src_path[:-3] + "zip"
                os.system("mv \"" + event.src_path + "\" \"" + zip_name + "\"")
                os.system("unzip \"" + zip_name + "\" -d \"" + event.src_path[:-4] +"\"")
                os.system("mv \"" + event.src_path[:-4] + "\" \"" + osu_path + "\"")
                os.system("rm \"" + zip_name + "\"")

if __name__ == "__main__":
    path = "."
    def event_handler():
        pass
    observer = Observer()
    osz_event = OszFileEventHandler()
    observer.schedule(osz_event, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
