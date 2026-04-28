import os
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#Config
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WATCH_DIR = os.path.join(os.path.expanduser("~"), "Downloads")
ORGANIZE_DIR = os.path.join(WATCH_DIR, "organized")

#File Categories 
CATEGORIES = {
    "PDFs" : [".pdf"],
    "IMAGES" : [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Videos" : [".mp4", ".mov", ".avi", ".mkv"],
    "Excel"  : [".xlsx", ".xls", ".csv"],
    "Word"   : [".doc", ".docx"],
    "Music"  : [".mp3", ".wav", ".flac"],
    "Code"   : [".py", ".js", ".html", ".css", ".json"],
    "Others" : []
}

#Create Folders

def create_folders():
    for folder in CATEGORIES:
        path = os.path.join(ORGANIZE_DIR, folder)
        os.makedirs(path, exist_ok=True)
    print("Folder Organized.")



#Move File
def move_file(file_path):
    filename = os.path.basename(file_path)
    extension = os.path.splitext(filename)[1].lower()

    destination_folder = "Others"
    for folder, extensions in CATEGORIES.items():
        if extension in extension:
            destination_folder = folder
            break

    destination = os.path.join(ORGANIZE_DIR, destination_folder, filename)

    if not os.path.exists(destination):
        shutil.move(file_path, destination)
        print(f"Moved {filename} → {destination_folder}")
        logging.info(f"Moved {filename} → {destination_folder}")
    else:
        print(f"Skipped {filename} — already exists in {destination_folder}")
        logging.info(f"Skipped {filename} — already exists in {destination_folder}")


#File Watcher
class FileHandler (FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            filename = os.path.basename(file_path)

            if not filename.startwith(".") and "organized" not in file_path:
                print(f"New file detected: {filename}")
                import time
                time.sleep(1)
                move_file(file_path)

#Observer
observer = Observer()
observer.schedule(FileHandler(), path=WATCH_DIR, recursive=False)
observer.start()

print(f"Watching: {WATCH_DIR}")
print("Drop any file in Downloads to organize it automatically.")

try:
    while True:
        import time
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()

#Logging
logging.basicConfig(
    filename=os.path.join(BASE_DIR, "organizer.log"),
    level=logging.INFO,
    format="%(asctime)s — %(message)s"
)

#Organize Existing Files
def organize_existing():
    print("Organizing existing files...")
    count=0
    for filename in os.listdir(WATCH_DIR):
        file_path = os.path.join(WATCH_DIR, filename)
        if os.path.isfile(file_path) and not filename.startswith(".") and "organized" not in file_path:
            move_file(file_path)
            count += 1
        print(f"Done. {count} files organized.")

create_folders()
organize_existing()