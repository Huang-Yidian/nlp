import numpy as np

class DataLoader(object):
    
    def __init__(self,type,label_type):
        super(DataLoader, self).__init__()
        self.type = type
        self.label_type = label_type
        self.label = []
        if type in ["msra","MSRA"]:
            self.msra = True
        else:
            raise Exception("DataLoader Error: Init with unknown type")

    def load_msra(self,batch_size,path):
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
                    if target not in self.label:
                        self.label.append(target)
                    targets.append(target)
                else:
                    data['chars'].append(chars)
                    data['targets'].append(targets)
                    chars = []
                    targets = []

            dataset = Dataset(data,batch_size)
            self.label.sort()
            return dataset
        except FileNotFoundError:
            print("FileNotFoundError : File not found in",path)


class Dataset(object):
    def __init__(self,data : dict,batch, keys=['chars','targets']):
        super(Dataset, self).__init__()
        self.dataset = data
        self.data_len = len(data.keys())
        self.keys = keys
        self.index = 0
        self.batch = batch


    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.data_len:
            res = [[]]
            for i in range(self.batch):
                for key in self.keys:
                    if key not in self.dataset.keys():
                        raise Exception("Key %s of Dataset is wrong！" % (key))
                    res[i].append(self.dataset[key][self.index])
                res.append([])

            self.index += 1
            return res,False
        else:
            res = [[]]
            for i in range(self.batch):
                for key in self.keys:
                    if key not in self.dataset.keys():
                        raise Exception("Key %s of Dataset is wrong！" % (key))
                    res[i].append(self.dataset[key][self.index])
                res.append([])
            return res, True
