import os
import time
from datetime import datetime, timedelta

# Path to your Downloads folder (adjust if needed)
downloads_folder = "/Users/joeykim/Downloads"

# Get the current time and 24 hours ago adjust time if needed
now = time.time()
twenty_four_hours_ago = now - 24 * 60 * 60

recent_files = []

for filename in os.listdir(downloads_folder):
    
    #creating path to the file
    filepath = os.path.join(downloads_folder, filename)
    
    #checking if the path points to a file
    if os.path.isfile(filepath):
        
        #getting the last modification time for the file
            #last download or change
        mtime = os.path.getmtime(filepath)
        if mtime >= twenty_four_hours_ago:
            recent_files.append(filename)

print("Files downloaded in the last 24 hours:")
for f in recent_files:
    print(f)