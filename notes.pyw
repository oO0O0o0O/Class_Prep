'''
Simple program to open up correct class notes by time of day and week.
'''

import os
import time

# Configs
filePath = 'MASKED'
classes = {
    'className': ['Hour:Min:Sec', 'Day1', 'Day2'],
    'className': ['Hour:Min:Sec', 'Day1', 'Day2']
}

# Get current day/time
day = time.asctime()[0:3]
time = time.asctime()[11:19]

# Loop to correct class
nextClass = ''

for k, v in classes.items():
    # Check if class is next
    if (day in v and time < v[0]):
        nextClass = k
        break

# Open notes file
path = os.path.join(filePath, nextClass, 'filename"')
os.popen(path)