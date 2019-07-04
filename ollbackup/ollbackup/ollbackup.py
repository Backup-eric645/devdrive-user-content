import os
class BackupModeError(Exception):
    pass
def RecurFolderTree(path):
    try:
        listOfFile = os.listdir(path)
    except PermissionError:
        return []
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(path, entry)
        if os.path.isdir(fullPath):
            allFiles.extend(FolderTree(fullPath))
        else:
            try:
                allFiles.append([fullPath, open(fullPath, 'rb').read()])
                print("Successful :", allFiles[-1][0])
            except PermissionError:
                print("Permission denied")
    return allFiles
def FolderTree(path):
    try:
        listOfFile = os.listdir(path)
    except PermissionError:
        return []
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(path, entry)
        if os.path.isdir(fullPath):
            allFiles.extend(RecurFolderTree(fullPath))
        else:
            try:
                allFiles.append([fullPath, open(fullPath, 'rb').read()])
                print("Successful :", allFiles[-1][0])
            except PermissionError:
                print("Permission denied")
    return allFiles
class Backup:
    def __init__(self, **kwargs):
        try:
            self.stream = open(kwargs['oll'], 'w')
        except FileNotFoundError:
            self.stream = open(kwargs['oll'], 'w+')
        files = FolderTree(kwargs['root'])
        mode = kwargs['backupType']
        t = []
        if mode == "dec":
            for mk in str(files):
                t.append(str(ord(mk)))
        elif mode == "hex":
            for mk in str(files):
                t.append(hex(ord(mk)))
        elif mode == "oct":
            for mk in str(files):
                t.append(oct(ord(mk)))
        elif mode == "bin":
            for mk in str(files):
                t.append(bin(ord(mk)))
        else:
            raise BackupModeError("Backup mode not supported")
        self.lm = t
    def st(self):
        self.stream.write('&'.join(self.lm))
class Restore:
    def __init__(self, **kwargs):
        self.root = kwargs['root']
        oll = kwargs['oll']
        p = ''
        for ep in open(oll).read().split("&"):
            p += chr(eval(ep))
        self.p = eval(p)
    def st(self):
        for zi in self.p:
            open(os.path.join(self.root, zi[0]), 'wb').write(zi[1])
import sys
try:
    if sys.argv[1].lower() == "backup":
        Backup(backupType=sys.argv[2], root=sys.argv[3], oll=sys.argv[4]).st()
    elif sys.argv[1].lower() == "restore":
        Restore(root=sys.argv[2], oll=sys.argv[3]).st()
    elif sys.argv[1].lower() == "-h" or '/?' or '?' or "help" or "--help" or "hlp" or "--hlp":
        print("""OLL Backup
Arg Commands:
BACKUP - backup with arg 1 as type (bin, hex, oct, or dec), arg 2 as backup root, and arg 3 as oll
RESTORE - restore with arg 1 as backup root, and arg 2 as oll
Commands are case-insensitive.""")
    else:
        print("Unrecognized command", sys.argv[1:])
except IndexError:
    print("""OLL Backup
Arg Commands:
BACKUP - backup with arg 1 as type (bin, hex, oct, or dec), arg 2 as backup root, and arg 3 as oll
RESTORE - restore with arg 1 as backup root, and arg 2 as oll
Commands are case-insensitive.""")
except BackupModeError:
    print("Backup mode not supported")
