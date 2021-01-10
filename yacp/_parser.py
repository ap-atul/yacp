""" Parsers for the serialisation and deserialisation"""


class Parser:

    def __init__(self, file=None, data=None, syntax=None):
        self.__name__ = "parser"

        self._file = file
        self._data = data
        self._syntax = syntax

    def __str__(self):
        return "@%s" % self.__name__

    @property
    def file(self):
        return self._name

    @property
    def data(self):
        return self._data

    @property
    def syntax(self):
        return self._syntax

    def set_file(self, file: str):
        self._file = file


class JsonParser(Parser):

    def __init__(self, file: str):
        super().__init__()
        self.__name__ = "Jsonparser"

        self._file = file
        self._syntax = "json"

    def get_dict(self):
        import json

        data = ""
        with open(self._file, "r") as f:
            for line in f.readlines():
                data += line

            f.close()

        self._data = json.loads(data)

        return self._data

    def write_dict(self, data):
        import json

        with open(self._file, "w") as f:
            string = json.dumps(data)
            f.write(string)

            f.close()


class YamlParser(Parser):

    def __init__(self, file: str):
        super().__init__()
        self.__name__ = "Yamlparser"

        self._file = file
        self._syntax = "yaml"

    def get_dict(self):
        import yaml

        data = ""

        with open(self._file, "r") as f:
            for line in f.readlines():
                data += line

            f.close()

        self._data = yaml.load(data, yaml.FullLoader)

        return self._data

    def write_dict(self, data: dict):
        import yaml

        with open(self._file, "w") as f:
            string = yaml.dump(data)
            f.write(string)

            f.close()

