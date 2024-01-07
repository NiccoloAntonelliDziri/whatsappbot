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
    open_file(filename)
        Opens the file in `filename` and returns the list of all the messages.
    add_message_to_file(message)
        Adds the message to the file in `filename`.
    """

    def __init__(self):
        """
        Initializes an instance of the class with the given filename.

        """
        
    def open_file(self, filename):
        """
        Opens the file and returns the list of all the messages.

        Parameters
        ----------
        filename : str
            The name of the file to read.

        Returns
        -------
        list
            The list of all the messages in the file.
        
        Raises
        ------
        FileNotFoundError
            If the file does not exist.
        """
        if not path.isfile(filename):
            raise FileNotFoundError("The file " + filename + " does not exist")
        with open(filename, 'r', encoding="UTF-8") as f:
            messages = f.read().splitlines()
        return messages
    
    def add_message_to_file(self, filename, message):
        """
        Adds the message `message` to the file.

        Parameters
        ----------
        filename : str
            The name of the file to write.
        message : str
            The message to be added to the file.
        
        Raises
        ------
        FileNotFoundError
            If the file does not exist.
        """
        if not path.isfile(filename):
            raise FileNotFoundError("The file " + filename + " does not exist")
        with open(filename, 'a', encoding="UTF-8") as f:
            f.writelines("\n" + message + "\n")
