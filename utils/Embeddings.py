import numpy as np
import torch.nn as nn

class Embeddings(object):
    def __init__(self):
        self.embeddings = nn.Parameter()

