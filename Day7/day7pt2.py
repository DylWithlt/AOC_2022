import re


class Node:

    def __init__(self, name, parent=None):
        self.name = ""
        self.parent = None
        self.size = 0
        self.children = dict()
        self.files = dict()
        self.depth = 0
        self.name = name
        if parent:
            self.parent = parent
            self.depth = parent.depth + 1

    def get_parent(self):
        return self.parent

    def get_dir(self, name):
        return self.children[name] if name in self.children else self.add_dir(name)

    def add_dir(self, name):
        if name in self.children:
            return self.children[name]

        newNode = Node(name, self)
        self.children[name] = newNode
        return newNode

    def add_file(self, name, size):
        self.files[name] = size
        self.add_size(size)
        ancestor = self.parent
        while ancestor:
            ancestor.add_size(size)
            ancestor = ancestor.parent

    def get_full_name(self):
        stack = []
        stack.append(self)
        ancestor = self.parent
        while ancestor:
            stack.append(ancestor)
            ancestor = ancestor.parent
        path = ""
        while len(stack) > 0:
            path += stack.pop().name
            path += "."
        return path

    def get_children(self):
        return self.children.values()

    def add_size(self, n):
        self.size += n

    def get_size(self):
        return self.size

    def get_file_size(self):
        return sum(self.files.values())

    def __str__(self):
        return self.depth * " " + self.name + " " + str(self.size)


with open('./Day7/input.txt', 'r') as f:
    root = Node("/")
    nodes = [root]

    currDir = root
    readDir = None

    for line in f.readlines():
        words = line.strip().split(" ")
        # print(words, currDir.get_full_name())

        if words[0] == "$":
            if words[1] == "cd":
                if words[2] == "/":
                    currDir = root
                elif words[2] == "..":
                    currDir = currDir.get_parent()
                    # if not currDir:
                    #     currDir = root
                else:
                    currDir = currDir.get_dir(words[2])
            elif words[1] == "ls":
                readDir = currDir
        elif words[0] == "dir":
            readDir.add_dir(words[1])
        else:
            readDir.add_file(words[1], int(words[0]))

    queue = []
    stack = []
    final = []
    queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        stack.append(node)
        for child in node.get_children():
            queue.append(child)
    while len(stack) > 0:
        node = stack.pop()
        # size = node.get_file_size()

        final.append(node)

    directories = []
    while len(final) > 0:
        node = final.pop()
        print(node)
        size = node.get_size()
        if size >= 30000000 - (70000000 - 44804833):
            directories.append(size)

    print(min(directories))
