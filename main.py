import os 

scandir = 'C:\\'


class Tree:

    def __init__(self, path):
        
        self.path = path
        self.dirs = []
        self.files = []
        for i in os.listdir(path):
            if os.path.isdir(path + os.sep + i):
                self.dirs.append(i)
            else: self.files.append(i)

    def checkdirs(self):

        homedir = Tree(scandir)
        basespaces = homedir.path.count('\\') + homedir.path.count('/')

        def setspace(self, basespaces):

            space = '   ' * (self.path.count('\\') + self.path.count('/') - basespaces)
            if len(space) > 0: 
                space = space[:-3]
                space += '|--'
            return space

        for i in self.files:
            print(f"{setspace(self, basespaces)}*{i}")

        for i in self.dirs:
            print(f"{setspace(self, basespaces)}#{i}")
            dir = Tree(self.path + os.sep + i)
            dir.checkdirs()

    def checksize(self):
        
        for i in self.files:
            print(f'*{self.path + os.sep + i} {round(os.path.getsize(self.path + os.sep + i) / 1024 / 1024)} MB')

        for i in self.dirs: 
            size = 0
            
            for path, dirs, files in os.walk(self.path + os.sep + i):
                for f in files:
                    fp = os.path.join(path, f)
                    size += os.stat(fp).st_size

            print(f'#{self.path + os.sep + i} {round(size / 1024 /1024)} MB')
 

def main():

    while True:

        scandir = input('Directory: ')
        action = input('Scan or get size: ')

        if action == 'scan':
            a = Tree(scandir)
            a.checkdirs()
            input('Done. Press Enter to continue...')

        elif action == 'size': 
            a = Tree(scandir)
            a.checksize()
            input('Done. Press Enter to continue...')

        elif action == 'exit': break

        else: print('Incorrect input')

if __name__ == '__main__': 
    main()