from json import dump
from os.path import exists


class Utility:
    @staticmethod
    def reader(file, mode='r'):
        """
        Method to load json file content.
        Args:
            file: Json file path.
            mode: Mode in which file has to open. Default mode is 'r'

        Returns:
            Returns file content as Json.

        """
        with open(file, mode) as read_file:
            return read_file.read()

    @staticmethod
    def writer(content, file, mode='w'):
        """
        Method to write content to a file.
        Args:
            content: Content to be written in file.
            file: Output file path.
            mode: Mode in which file has to open. Default mode is 'w'

        Returns:
            None

        """
        with open(file, mode) as write_file:
            if isinstance(content, list):
                dump(content, write_file, indent=2)
            else:
                write_file.write(content)

    @staticmethod
    def get_file_content(in_take):
        """
        Method to check file existence and return file content.
        Args:
            in_take: Json file path or dict or list object.

        Returns:
            Returns file content as json if file found else False.

        """
        if isinstance(in_take, dict):
            return [in_take]
        elif exists(in_take):
            return Utility.reader(in_take)
        elif isinstance(in_take, list) or isinstance(in_take, str):
            return in_take
        raise ValueError('Input type is not valid.')
