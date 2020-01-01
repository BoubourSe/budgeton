from pathlib import Path
import json


class Conf:

    _directory = Path.home().joinpath('.svsoft')
    _name = 'budgeton.cfg'

    def __init__(self, directory=None, name=None):
        self._f = None

        if name is not None:
            self._name = name

        # init directory path
        if directory is not None:
            self._directory = directory

        self.init_directory()
        self.init_file()
        self.read_conf()

    def init_directory(self):
        if self._directory.exists() is False:
            self._directory.mkdir()

    def open_file(self):
        """Open file and return if created"""

        created = False

        if self._f is not None and self._f.closed is False:
            pass

        try:
            # open for read
            self._f = open(
                self._directory.joinpath(self._name),
                'r+',
                encoding='utf-8')
        except FileNotFoundError:
            # create if not exist
            self._f = open(
                self._directory.joinpath(self._name),
                'w',
                encoding='utf-8')
            created = True
        finally:
            if created:
                self._f.close()
                self._f = open(
                    self._directory.joinpath(self._name),
                    'r+',
                    encoding='utf-8')

        return created

    def init_file(self):

        if self.open_file():
            self._conf = {
                "last_opened": False,
            }
            self.save()

        self._f.close()

    def save(self):
        self.open_file()
        conf_dumped = json.dumps(self._conf)
        self._f.write(conf_dumped)
        self._f.close()

    def read_conf(self):
        self.open_file()
        content = self._f.read()
        self._conf = json.loads(content)
        self._f.close()

    def get(self, key):
        """return key if present in self._conf also return None"""
        try:
            return self._conf[key]
        except KeyError:
            return None

    def set(self, key, value):
        """set key in conf and write on file"""
        self._conf[key] = value
        self.save()
