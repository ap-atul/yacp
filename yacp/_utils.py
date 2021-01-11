import os
from._parser import JsonParser, YamlParser, CustomParser


def get_parser_for_file(filename):
    basename = os.path.basename(filename)

    if basename.endswith('.json'):
        return JsonParser

    if basename.endswith('.yaml'):
        return YamlParser

    return CustomParser


def setmembers(data, cls):
    for key, val in data.items():
        if key in cls.__dict__:
            setattr(cls, key, val)

    return cls


def getmembers(cls):
    data = dict()

    for key, val in cls.__dict__.items():
        data[key] = val

    return data
