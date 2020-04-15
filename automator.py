from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        #Make sure destination folder exists
        try:
            os.makedirs(folder_to_place)
        except FileExistsError:
            pass
        #Distributes different file types into correct folders
        for filename in os.listdir(folder_to_track):
            if(filename.endswith('.pdf')):
                try:
                    os.makedirs(pdf_destination)
                except FileExistsError:
                    pass
                src = folder_to_track + "/" + filename
                new_destination = pdf_destination + "/" + filename
                os.rename(src, new_destination)
            elif(filename.endswith('.jpg') or filename.endswith('.png')):
                try:
                    os.makedirs(pic_destination)
                except FileExistsError:
                    pass
                src = folder_to_track + "/" + filename
                new_destination = pic_destination + "/" + filename
                os.rename(src, new_destination)
            elif(filename.endswith('.py')):
                try:
                    os.makedirs(py_destination)
                except FileExistsError:
                    pass
                src = folder_to_track + "/" + filename
                new_destination = py_destination + "/" + filename
                os.rename(src, new_destination)
            elif(filename.endswith('.mp4')):
                try:
                    os.makedirs(mp4_destination)
                except FileExistsError:
                    pass
                src = folder_to_track + "/" + filename
                new_destination = mp4_destination + "/" + filename
                os.rename(src, new_destination)


folder_to_track = "<insert folder name that you will track>"
folder_to_place = "<insert destination folder name>"
pdf_destination = "<insert PDF file destination folder name>"
pic_destination = "<insert image file destination folder name>"
py_destination = "<insert Python file destination folder name>"
mp4_destination = "<insert mp4 file destination folder name>"


#Make sure folder exists
try:
    os.makedirs(folder_to_track)
except FileExistsError:
    pass

#Begin handler
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

#Stop observer on error
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
