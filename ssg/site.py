from pathlib import Path


class Site:
    def __init__(self, source=None, dest=None):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        print(f'path: {path}')
        print(f'dest: {self.dest}')
        print(f'directory: {directory}')

        Path.mkdir(directory, parents=True, exist_ok=True)

    def build(self):
        self.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                path.create_dir()
