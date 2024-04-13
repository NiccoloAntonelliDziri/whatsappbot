import pyautogui as pg
from pyperclip import copy
from time import sleep, time, localtime

class WhatsappBot:
    """
    Represents a WhatsApp bot that can send messages to a specific contact
    at a specified time.

    Attributes
    ----------
    contact : str
        The name of the contact. The contact must be in the list of contacts.
        Can also be the name of a group.
    pos_contact : int, optional
        The position of the contact in the list of contacts when it is displayed.
        (The default is 1, which means that the contact is the first in the list.)
    hour : int
        The hour at which the message should be sent.
    min : int
        The minute at which the message should be sent.
    emoji_split_symbol : str
        The symbol that encloses the text of emojis.
    sleep_time : int
        The waiting time between each action.
    sleep_time_whatsapp : int
        The waiting time for WhatsApp to load.
    whatsapp_button_x : int
        The x coordinate of the WhatsApp button on the taskbar.
    whatsapp_button_y : int
        The y coordinate of the WhatsApp button on the taskbar.

    Methods
    -------
    __init__(contact, hour, minute, pos_contact=1, emoji_split_symbol='@',
            sleep_time=1, sleep_time_whatsapp=15)
        Initializes a new instance of the WhatsappBot class.
    __str__()
        Returns a string representation of the WhatsappBot object.
    set_time(hour, minute)
        Sets the hour and minute at which the message should be sent.
    set_contact(contact)
        Sets the contact to whom the message should be sent.
    set_emoji_split_symbol(emoji_split_symbol)
        Sets the symbol that encloses the text of emojis.
    time_before_send()
        Returns the duration in seconds to wait before sending the message.
    wait_before_send()
        Waits for the duration returned by the time_before_send() method.
    go_to_chat()
        Navigates to the chat with the specified contact.
    select_emoji(emoji, pos_emoji=0)
        Selects the specified emoji to write it in the chat. `pos_emoji` is the
        position of the emoji in the list of emojis when it is displayed. (The default
        is 0, which means that the emoji is the first in the list.)
    write(text)
        Writes the specified `text` including emojis in the chat.
    split_message(message)
        Splits the `message` into a list of text and emojis.

    Examples
    --------
    I this example, the bot will send a message to the contact "Contact" at 12:45.
    It will open WhatsApp and go to the chat with "Contact" before sending the message.
    'smile2' is the name of the emoji followed by the position of the emoji in the list.
    The position is optional. If not specified, the first emoji in the list is selected.
    
    >>> bot = WhatsappBot("Contact", 12, 45)
    >>> bot.send("Hello @smile2@ World!")
    """

    def __init__(self, contact, hour, minute, pos_contact=1,
                    emoji_split_symbol='@', newline_split_symbol='\\n',sleep_time=1, sleep_time_whatsapp=15,
                    whatsapp_button_x=991, whatsapp_button_y=1043):
        """
        Initialize the Bot class.

        Parameters
        ----------
        contact : str
            The contact name or number to send messages to.
        hour : int
            The hour at which the message should be sent.
        minute : int
            The minute at which the message should be sent.
        pos_contact : int, optional
            The position of the contact in the chat list (default is 1).
        emoji_split_symbol : str, optional
            The symbol used to split emojis in the message (default is '@').
        sleep_time : int, optional
            The time to sleep between sending messages (default is 1).
        sleep_time_whatsapp : int, optional
            The time to sleep after opening WhatsApp (default is 15).
        whatsapp_button_x : int, optional
            The x coordinate of the WhatsApp button on the taskbar.
        whatsapp_button_y : int, optional
            The y coordinate of the WhatsApp button on the taskbar.
        """
        self.contact = contact
        self.pos_contact = pos_contact
        self.hour = hour
        self.min = minute
        self.emoji_split_symbol = emoji_split_symbol
        self.sleep_time = sleep_time
        self.sleep_time_whatsapp = sleep_time_whatsapp
        self.whatsapp_button_x = whatsapp_button_x
        self.whatsapp_button_y = whatsapp_button_y
        self.newline_split_symbol = newline_split_symbol

    def __str__(self):
        """
        Returns a string representation of the WhatsappBot object.

        Returns
        -------
        str
            A string representation of the WhatsappBot object.
        """
        return ("Contact: " + self.contact + "\n"
                + "Hour: " + str(self.hour) + "\n"
                + "Minute: " + str(self.min) + "\n"
                + "Emoji split symbol: " + self.emoji_split_symbol + "\n"
                + "Sleep time: " + str(self.sleep_time) + "\n"
                + "Sleep time WhatsApp: " + str(self.sleep_time_whatsapp) + "\n"
                + "Position contact: " + str(self.pos_contact) + "\n")
      
    def set_time(self, hour, minute):
        """
        Set the time at which the message should be sent.

        Parameters
        ----------
        hour : int
            The hour at which the message should be sent.
        minute : int
            The minute at which the message should be sent.
        """
        self.hour = hour
        self.min = minute

    def set_contact(self, contact):
        """
        Set the contact to whom the message should be sent.

        Parameters
        ----------
        contact : str
            The contact name of the contact to send messages to.
            It should be in the list of contacts. If not, it has to be a name which
            can be found in the search bar.
        """
        self.contact = contact
    
    def set_emoji_split_symbol(self, emoji_split_symbol):
        """
        Set the symbol that encloses the text of emojis.

        Parameters
        ----------
        emoji_split_symbol : char
            The symbol that encloses the text of emojis.
        """
        self.emoji_split_symbol = emoji_split_symbol
        
    # Retourne une durée en secondes
    # Correspond au temps qu'il faut attendre avant d'envoyer le message
    def time_before_send(self):
        """
        Calculates the duration in seconds to wait before sending the message.
        This method is subject to change in order to be more accurate.
        
        Returns
        -------
        int
            The duration in seconds to wait before sending the message.
        """
        temps = time()
        date = localtime(temps)
        h = date.tm_hour
        m = date.tm_min
        if (self.hour == h):
            if (self.min >= m):
                return self.min - m
        offset = 0
        if (h > self.hour):
            offset = 24 - h
            h = 0

        cpt = 0
        while (h < self.hour):
            if (h == 24):
                h = 0
            while (m < 60):
                m += 1
                cpt += 1
            h += 1
            m = 0
        m = 0
        while (m < self.min):
            m += 1
        #print(h + offset, m)
        return (60 * offset + cpt + m) * 60

    def wait_before_send(self):
        """
        Waits for the duration returned by the time_before_send() method.
        """
        sec = self.time_before_send()
        print("The message will be sent in", sec, "seconds")
        sleep(sec)

    # Go to chat with contact
    def go_to_chat(self):
        """
        Navigates to the chat with the specified contact.
        """
        pg.hotkey('ctrl','f')
        sleep(self.sleep_time)
        copy(self.contact)
        pg.hotkey('ctrl','v')
        sleep(self.sleep_time * 2)
        [pg.press('down') for _ in range(self.pos_contact)]
        pg.press('enter')
    
    # emojis handling
    def select_emoji(self, emoji, pos_emoji=0):
        """
        Selects the specified emoji to write it in the chat.
        
        Parameters
        ----------
        emoji : str
            A text representation of the emoji.
        pos_emoji : int, optional
            The position of the emoji in the list of emojis.
            (The default is 0, which means that the emoji is the first in the list that
            is displayed.)
        """
        copy(":")   # Raccourci whatsapp pour écrire des emojis
        pg.hotkey('ctrl', 'v')
        sleep(self.sleep_time)
        copy(emoji)
        pg.hotkey('ctrl', 'v')
        sleep(self.sleep_time)
        for _ in range(pos_emoji):
            pg.press('right')
            sleep(self.sleep_time)
        pg.press('enter')
    
    # Ecris texte
    def write(self, text):
        """
        Writes the specified `text` whereever the cursor is. The text can contain newlines, specified by `self.newline_split_symbol`.
        
        Parameters
        ----------
        text : str
            The text to be written.
        """
        split_text = text.split(self.newline_split_symbol)
        for i in range(len(split_text)):
            copy(split_text[i])
            pg.hotkey('ctrl', 'v')
            if (i < len(split_text) - 1):
                pg.hotkey('shift', 'enter')

    def split_message(self, message, split_symbol):
        """
        Splits the `message` into a list of text and emojis.
        
        Parameters
        ----------
        message : str
            The message to be split.

        Returns
        -------
        list
            The list of text and emojis. The text and emojis are alternated. (Empty
            strings are possible.)
        """
        liste_split = message.split(split_symbol)
        return liste_split
    
    # Retire le chiffre situé à la toute fin d'une chaine de caractères
    # Retourne ce chiffre
    def extract_last_digit(self, text):
        """
        Extracts the last digit from the specified `text`.
        
        Parameters
        ----------
        text : str
            The text from which the last digit should be extracted.

        Returns
        -------
        int
            The last digit of the text.
        str
            The text without the last digit.
        """
        last_char = text[-1]
        if (last_char.isdigit()):
            text = text[:-1]
            print("text: " + text)
            return int(last_char), text
        # Si pas de chiffre a la fin, par défaut c'est 0 (on appuie pas sur fleche droite pour changer d'emoji)
        return 0, text

    def write_message(self, split_message):
        """
        Writes a message in the chat. The message is split into text and emojis.
        Newlines are handled but should not be used in the middle of an emoji.
        
        Parameters
        ----------
        split_message : list
            The list of text and emojis. The text and emojis are alternated. (Empty
            strings are possible.)
        """
        for i in range(len(split_message)):
            # Si i est pair, alors c'est un texte
            if i % 2 == 0:
                # split (dans split_message) met des caractères vides quand deux emojis se suivent donc c'est toujours alterné
                sleep(self.sleep_time)
                self.write(split_message[i])
            # Sinon c'est un emoji
            else:
                sleep(self.sleep_time)
                pos_emoji, emoji = self.extract_last_digit(split_message[i])
                self.select_emoji(emoji, pos_emoji)

    def send_message(self, message):
        """
        Sends the specified `message` to the contact.
        Use this method only if you are already in the chat with the contact.
        
        Parameters
        ----------
        message : str
            The message to be sent to the contact.
        """
        list_msg = self.split_message(message, self.emoji_split_symbol) # Sépare les emojis et les textes
        self.write_message(list_msg)
        sleep(self.sleep_time)
        pg.press('enter')
        sleep(self.sleep_time)
    
    def open_whatapp(self):
        """
        Opens WhatsApp. The WhatsApp button should be on the taskbar on a fixed position.
        If the position of the button changes, the coordinates should be updated. No check
        is done to verify that the correct button is clicked.
        """
        pg.moveTo(self.whatsapp_button_x, self.whatsapp_button_y)
        pg.leftClick()
        sleep(self.sleep_time_whatsapp)

    def quit_whatsapp(self):
        """
        Quits Whatsapp with alt+F4.
        """
        pg.hotkey('alt', 'f4')
        sleep(self.sleep_time)

    def send(self, message, open_whatsapp = True, quit_whatsapp = True, send_now = False, go_to_chat = True):
        """
        Sends the specified `message` to the contact. It is a wrapper around the other
        methods of the class.
        
        Parameters
        ----------
        message : str
            The message to be sent to the contact.
        open_whatapp : bool, optional
            Whether to open WhatsApp before sending the message (default is True).
        quit_whatsapp : bool, optional
            Whether to quit WhatsApp after sending the message (default is True).
        send_now : bool, optional
            Whether to send the message immediately (default is False).
        go_to_chat : bool, optional
            Whether to go to the chat with the contact before sending the message
            (default is True).
        """
        if not send_now:
            self.wait_before_send()
        if open_whatsapp:
            self.open_whatapp()
        if go_to_chat:
            self.go_to_chat()
        #sleep(self.sleep_time)
        self.send_message(message)
        if quit_whatsapp:
            self.quit_whatsapp()