from abc import ABC
import re
from typing import Optional

threshold = 100000
totalMemory = 70000000
neededMemory = 30000000


def compute(file):
    f = open(file, "r")
    lines = f.readlines()

    root = RootDir()
    currentDir = root

    for line in lines:
        try:
            normLine = line.strip('\n')
            if (re.fullmatch(r'\$ cd /', normLine)):
                # Move to root
                currentDir = root
            elif (re.fullmatch(r'\$ cd (\w+)', normLine)):
                # Move to child dir
                dirName = re.findall(r'cd (\w+)', normLine)
                currentDir = currentDir.getChildDir(dirName[0])
            elif (re.fullmatch(r'\$ cd \.\.', normLine)):
                # Move to parent
                currentDir = currentDir.getParentDir()
            elif (re.fullmatch(r'\$ ls', normLine)):
                # do nothing just indicates a listing will follow
                _ = 42
            elif (re.fullmatch(r'dir (\w+)', normLine)):
                # Listing found dir, so add it to the current dir
                dirName = re.findall(r'dir (\w+)', normLine)
                currentDir.addDir(Directory(dirName[0], currentDir))
            elif (re.fullmatch(r'(\d+) (.+)', normLine)):
                # Listing found file, so add file with its size
                fileProps = re.findall(r'(\d+) (.+)', normLine)
                currentDir.addFile(File(int(fileProps[0][0]), fileProps[0][1]))
            else:
                print("ERROR, unknown line: ", normLine)

            # print("processed line: ", line)
        except StopIteration as e:
            print("ERROR, unknown dir: ", line)
            visit(root, lambda d: print("dir: ", d.name),
                  lambda f: print("file: ", f.name))
            raise e

    root.computeSize()

    totalUsed = root.size
    freeMemory = totalMemory - totalUsed
    toBeFreed = neededMemory - freeMemory
    potentialDirs = getAllPotentialDirs(root, toBeFreed)

    result1 = computeTotalStorageSize(root)
    result2 = sorted(potentialDirs, key=lambda d: d.size)[0].size

    return result1, result2


class File:
    def __init__(self, size: int, name: str):
        self.size = size
        self.name = name

    size: int
    name: str


class Directory:
    def __init__(self, name: str, parent: 'Directory'):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []
        self.size = 0

    name: str
    parent: Optional['Directory']
    files: list[File]
    dirs: list['Directory']
    size: int

    def addFile(self, file: File):
        self.files.append(file)

    def addDir(self, dir: 'Directory'):
        self.dirs.append(dir)

    def getParentDir(self):
        if (self.parent == None):
            raise ValueError("Not allowed to get parent of root folder")

        return self.parent

    def getChildDir(self, name: str):
        return next(d for d in self.dirs if d.name == name)

    def computeSize(self):
        fileSizes = 0
        totalDirSize = 0

        for f in self.files:
            fileSizes += f.size

        for d in self.dirs:
            d.computeSize()
            totalDirSize += d.size

        self.size = totalDirSize + fileSizes


class RootDir(Directory):
    def __init__(self):
        self.name = "root"
        self.parent = None
        self.dirs = []
        self.files = []


def visit(dir: Directory, lambdaFuncDir, lambdaFuncFile):
    lambdaFuncDir(dir)

    for f in dir.files:
        lambdaFuncFile(f)

    for d in dir.dirs:
        visit(d, lambdaFuncDir, lambdaFuncFile)


def computeTotalStorageSize(dir: Directory):
    totalSize = 0

    if (dir.size <= threshold):
        totalSize += dir.size

    for d in dir.dirs:
        sumDir = computeTotalStorageSize(d)
        totalSize += sumDir

    return totalSize


def getAllPotentialDirs(dir: Directory, neededSize: int):
    allPotentialDirs = []

    if (dir.size >= neededSize):
        allPotentialDirs.append(dir)

    for d in dir.dirs:
        allPotentialDirs.extend(getAllPotentialDirs(d, neededSize))

    return allPotentialDirs
