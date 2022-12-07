class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

    def __str__(self):
        return f"* {self.name} {self.size}\n"


class Folder:
    def __init__(self, name="/", parent=None, level=0) -> None:
        self.parent = parent
        self.name = name
        self.child = []
        self.depth = level

    def add_dir(self, name, level):
        self.child.append(Folder(name, self, level))

    def add_file(self, name, size):
        self.child.append(File(name, size))

    def cd(self, name):
        for el in self.child:
            if el.name == name:
                return el
        return None

    def get_size(self):
        S = 0
        for c in self.child:
            if isinstance(c, File):
                S += c.size
            else:
                S += c.get_size()
        return S

    def get_dir_sizes(self):
        S = []
        for c in self.child:
            if isinstance(c, Folder):
                S.append(c.get_size())
                S = S + c.get_dir_sizes()
        return S

    def __str__(self):
        s = f"- {self.name}\n"
        for c in self.child:
            _ = "  " * (self.depth + 1)
            s += f"{_}{c.__str__()}"

        return s


def load_txt(filename):
    root = Folder()
    current = root
    add = False
    depth = 0
    with open(filename) as f:
        for L in f:
            line = L.replace("\n", '')
            if line.startswith("$ cd"):
                add = False
                name = line.split(" ")[-1]

                if name not in ["/", ".."]:
                    current = current.cd(name)
                    depth += 1

                if name == '..':
                    current = current.parent
                    depth -= 1

            if line.startswith("$ ls"):
                add = True
                continue

            if add:
                t, name = line.split(" ")
                if t == "dir":
                    current.add_dir(name, depth + 1)
                else:
                    current.add_file(name, int(t))
    return root


tree = load_txt("input.txt")

# Part One
S = [x for x in tree.get_dir_sizes() if x <= 100000]
print(f"Sum of total sizes less or equal than 100000 is {sum(S)}")

# Part Two
unused = 70000000 - tree.get_size()
required = 30000000 - unused
S = [x for x in tree.get_dir_sizes() if x >= required]
print(f"You must delete {min(S)} of space")