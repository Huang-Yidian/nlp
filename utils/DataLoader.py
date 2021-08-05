import numpy as np

class DataLoader(object):
    
    def __init__(self,type):
        super(DataLoader, self).__init__()
        self.type = type

        if type in ["msra","MSRA"]:
            self.msra = True
        else:
            raise Exception("DataLoader Error: Init with unknown type")


    def load_msra(self,path):
        try:
            data = {}
            data['chars'] = []
            data['targets'] = []
            f = open(path, 'r', encoding='utf-8')
            lines = f.readlines()
            chars = []
            targets = []
            for line in lines:
                if len(line) > 2:
                    char,target = line.strip().split()
                    chars.append(char)
                    targets.append(target)
                else:
                    data['chars'].append(chars)
                    data['targets'].append(targets)
                    chars = []
                    targets = []

            return data
        except FileNotFoundError:
            print("FileNotFoundError : File not found in",path)


