# WhatsApp Bot

This simple script uses the whatsapp desktop application to automatically send messages to either contacts or groups.

## Dependencies

The bot works with the desktop application and uses whatsapp keyboard shortcuts. It uses the `pyautogui` to interface whatsapp with the keyboard and the mouse. You also need the 'copy' function from `pyperclip` in order to copy messages onto the clipboard.

Versions that works for me:
- pyautogui v...
- pyperclip v...

It can be installed using `command`

Note that I only tested it on Windows 10 with version ... of whatsapp but it should also work on macos. Ubuntu doesn't have an official whatsapp app and the various shorcuts don't work on whatsapp web.

## How to use

You only have to include the files in your project and include them using:
```python
import WhateverDirectoryYouPutThis.bot as bot
import WhateverDirectoryYouPutThis.filemanager as fm
```

## A simple example

The following exemple randomly choses a message in the file `m̀essages.txt` (one message per line) and sends it at 9h56 to `contact`.
```python
from random import choice

b = bot.WhatsappBot("contact", 9, 56)  # Bot configuration
f = fm.FileManager()                 # FileManger object 
list = f.open_file("messages.txt")   # Opening the file and putting the messages in `list`
msg = choice(list)                   # Random selection of a message

b.send(msg)                          # Sending the message
```
