from io import StringIO
from json import dump, dumps, loads, load
from os.path import exists


def json2jsonl(in_take, file=None):
    """
    Method to write json data as Jsonlines/ndjson files. This method
    returns as Jsonlines/ndjson if no output file path is passed else
    returns None but creates a file with Jsonlines/ndjson content.

    Args:
        in_take: Input json data. A Json file or Json data.
        file: Jsonlines/ndjson Output file path.

    Returns:
        Jsonlines/ndjson content.

    """
    output_content = StringIO()
    in_take = Utility.get_json(in_take)
    if not isinstance(in_take, dict):
        for line in in_take:
            output_content.write(dumps(line) + '\n')
    else:
        output_content.write(dumps(in_take) + '\n')
    return Utility.writer(output_content.getvalue(), file=file) if \
        file else output_content.getvalue()


def jsonl2json(in_take, file=None):
    """
    Method to read Jsonlines/ndjson data as json files.

    Args:
        in_take: Input json data. A Json file or Json data.
        file: Jsonlines/ndjson Output file path.

    Returns:
        None

    """
    content = [loads(line) for line in
               Utility.get_jsonlines(in_take).split('\n') if line]
    return Utility.writer(content, file=file) if file else content


class Utility:
    @staticmethod
    def get_json(in_take):
        """
        Method to load Json from Json file or object.
        Args:
            in_take: Content. It can be a Json file or Json object or
            json string.

        Returns:
            Returns loaded Json.

        """
        if exists(str(in_take)):
            with open(in_take, 'r') as read_file:
                return load(read_file)
        elif isinstance(in_take, dict):
            return [in_take]
        elif isinstance(in_take, list):
            return in_take
        elif isinstance(in_take, str):
            return loads(in_take)
        raise ValueError('Input type is not valid.')

    @staticmethod
    def get_jsonlines(in_take):
        """
        Method to read jsonlines/ndjson file or string.
        Args:
            in_take: Content. It can be a Jsonlines file or string
            object.

        Returns:
            Returns loaded content as string.

        """
        if exists(str(in_take)):
            with open(in_take, 'r') as read_file:
                return read_file.read()
        return in_take

    @staticmethod
    def writer(content, file, mode='w'):
        """
        Method to write content to a file.
        Args:
            content: Content to be written in file.
            file: Output file path.
            mode: Mode in which file has to open. Default mode is 'w'

        """
        with open(file, mode) as write_file:
            if isinstance(content, list):
                dump(content, write_file, indent=2)
            else:
                write_file.write(content)
