import os.path as path

class FileManager:
    """
    A class that manages file operations for reading and writing messages.
    There is one message per line in the file. The file must be encoded in UTF-8.

    ...

    Attributes
    ----------
    filename : str
        The name of the file to read or write.

    Methods
    -------
    set_filename(filename)
        Changes the name of the file.
    open_file()
        Opens the file in `filename` and returns the list of all the messages.
    add_message_to_file(message)
        Adds the message to the file in `filename`.
    """

    def __init__(self, filename):
        """
        Initializes an instance of the class with the given filename.

        Parameters
        ----------
        filename : str
            The name of the file to read or write.
        """
        self.filename = filename

    def set_filename(self, filename):
        """
        Changes the name of the file.

        Parameters
        ----------
        filename : str
            The new name of the file.
        """
        self.filename = filename
    
    def open_file(self):
        """
        Opens the file and returns the list of all the messages.

        Returns
        -------
        list
            The list of all the messages in the file.
        
        Raises
        ------
        FileNotFoundError
            If the file does not exist.
        """
        if not path.isfile(self.filename):
            raise FileNotFoundError("The file " + self.filename + " does not exist")
        with open(self.filename, 'r', encoding="UTF-8") as f:
            messages = f.read().splitlines()
        return messages
    
    def add_message_to_file(self, message):
        """
        Adds the message `message` to the file.

        Parameters
        ----------
        message : str
            The message to be added to the file.
        
        Raises
        ------
        FileNotFoundError
            If the file does not exist.
        """
        if not path.isfile(self.filename):
            raise FileNotFoundError("The file " + self.filename + " does not exist")
        with open(self.filename, 'a', encoding="UTF-8") as f:
            f.writelines("\n" + message + "\n")
