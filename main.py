from config import config
from utils.DataLoader import DataLoader
import torch
from torch import nn
import torchvision
from utils.Tokenizer import *

import os
if __name__ == "__main__":
    if not os.path.exists(config.all_embeddings):
        concate_file(config)
    if not os.path.exists(config.diction) and not os.path.exists(config.indexing):
        process_embedding(config)

    dataloader = DataLoader('msra','bmeso')
    train_data = dataloader.load_msra(config.batch_size,config.train_path)
    print(dataloader.label)
    for i,(batch,is_next_epoch) in enumerate(train_data):
        print(batch[0][1])
        exit()
