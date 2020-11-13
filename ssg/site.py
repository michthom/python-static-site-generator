from pathlib import Path


class Site:
    def __init__(self, source=None, dest=None):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path=None):
        directory = self.dest / Path.relative_to(path)
        print(f'path: {path}')
        print(f'dest: {self.dest}')
        print(f'directory: {directory}')

        Path.mkdir(directory, parents=True, exist_ok=True)

    def build(self):
        Path.mkdir(self, parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if Path.is_dir(path):
                self.create_dir(path)
