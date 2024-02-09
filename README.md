# WhatsApp Bot

This simple script uses the whatsapp desktop application to automatically send messages to either contacts or groups.

## Dependencies

The bot works with the desktop application and uses whatsapp keyboard shortcuts. It uses the `pyautogui` to interface whatsapp with the keyboard and the mouse. You also need the 'copy' function from `pyperclip` in order to copy messages onto the clipboard.

Versions that worked for me:
- pyautogui v0.9.54
- pyperclip v1.8.2

See https://pypi.org/project/PyAutoGUI/ and https://pypi.org/project/pyperclip/ for installation.

Note that I only tested it on Windows 10 with version 2.2403.10.0 - at the time of writing this - of whatsapp but it should also work with some previous and future versions and on macos. Linux doesn't have an official whatsapp app.

## How to use

You only have to include the files in your project and include them using:
```python
import WhateverDirectoryYouPutThisIn.bot as bot
import WhateverDirectoryYouPutThisIn.filemanager as fm
```

## A simple example

The following exemple randomly choses a message in the file `m̀essages.txt` (one message per line) and sends it at 9h56 to `contact`.
```python
from random import choice

b = bot.WhatsappBot("contact", 9, 56)# Bot configuration
f = fm.FileManager()                 # FileManger object 
list = f.open_file("messages.txt")   # Opening the file and putting the messages in `list`
msg = choice(list)                   # Random selection of a message

b.send(msg)                          # Sending the message
```
