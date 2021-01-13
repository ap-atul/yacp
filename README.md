# yacp
Yet Another Config Parser. Convert YAML, JSON, and Custom files to python objects and back.

## Parsers
* JsonParser uses  inbuilt json module
* YamlParser uses inbuilt yaml module
* CustomParser uses a simple parser which requires a syntax to be passed.


## Get the package

1. Install using pip
```console
pip3 install git+https://github.com/AP-Atul/yacp
```

2. Clone and install
```console
git clone https://github.com/AP-Atul/yacp
python3 setup.py install
```

## Usage
1. Buid a class with members (or without)
```python
class Settings:
    def __init__(self):
        self._name = None
        self._age = None

settings = Settings()
```

2. Loading a file into the object
```python
## the parser type will be determined using the file name
settings = yacp.load(filename=YOUR_FILE, cls=OBJECT)
```

3. Dumping an object
```python
yacp.dump(filename=YOUR_FILE, cls=OBJECT)
```

* For custom files use syntax attribute
[NOTE: Primitive data types are preserved using regexps]
```python
# syntax should contain two strings (key, val)
object = yacp.load(filename=FILE, cls=OBJECT, syntax="%s:%s")
yacp.dump(filename=FILE, cls=OBJECT, syntax="%s:%s")
```

* Use override for class with no members
[This will add attributes to the object that are not declared
in the class but available in the file]
```python
object = yacp.load(filename, cls, override=True)
```

