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