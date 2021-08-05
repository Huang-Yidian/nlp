from config import config
import json
from easydict import EasyDict as edict


def process_embedding(config):
    json_dic = {}
    data = read_file(config.all_embeddings)
    for i in data:
        if i != '\n':
            i = i.strip().split()
            emb = i[1:]
            #[i[0]] = np.array(emb,dtype=float)
            json_dic[i[0]] = [float(item) for item in emb]

    print("load all embeddings!")
    indexing = {}
    index = 0
    for k in json_dic.keys():
        indexing[k] = index
        index += 1
    with open(config.diction,'w') as d:
        json.dump(json_dic,d)
    with open(config.indexing,'w') as i:
        json.dump(indexing,i)



def concate_file(config: edict()):
    all = open(config.all_embeddings,'w',encoding='utf-8')
    file_list = []
    for key in config.keys():
        if key.split('_')[-1] == "embedding":
            file_list.append(key)
            f = open(config[key],'r',encoding='utf-8')
            data = f.readlines()
            all.write("".join(data))
            f.close()
    print("concate vec file： "+", ".join(file_list))
    all.close()


def read_file(filepath):
    with open(filepath, 'r',encoding='utf-8') as f:
        for item in f:
            yield item

def load_json(config):
    with open(config.diction, "r", encoding='utf-8') as d:
        embeddings = json.load(d)
    with open(config.diction, "r", encoding='utf-8') as i:
        indexing = json.load(i)
    return embeddings,indexing

