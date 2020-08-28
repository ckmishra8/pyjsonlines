from io import StringIO
from json import dumps, loads

from src.utility import Utility


def json2jsonl(in_take, file=None):
    """
    Method to write json data as jsonlines files. This method
    returns as Jsonlines if no output file path is passed else
    returns None but creates a file with Jsonlines content.

    Args:
        in_take: Input json data. A Json file or Json data.
        file: Jsonlines Output file path.

    Returns:
        Jsonlines content.

    """
    output_content = StringIO()
    in_take = loads(Utility.get_file_content(in_take))
    if not isinstance(in_take, dict):
        for line in in_take:
            output_content.write(dumps(line) + '\n')
    else:
        output_content.write(dumps(in_take) + '\n')
    return Utility.writer(output_content.getvalue(), file=file) if \
        file else output_content.getvalue()


def jsonl2json(in_take, file=None):
    """
    Method to read jsonlines data as json files.

    Args:
        in_take: Input json data. A Json file or Json data.
        file: Jsonlines Output file path.

    Returns:
        None

    """
    content = [loads(line) for line in
               Utility.get_file_content(in_take).split('\n') if line]
    return Utility.writer(content, file=file) if file else content
