from easydict import EasyDict as edict

config = edict()
config.dataset = "msra"
config.embedding_size = 50
config.hidden_size = 512
config.sample_rate = 1
config.fp16 = False
config.momentum = 0.9
config.weight_decay = 5e-4
config.batch_size = 2
config.lr = 1e-3
config.output = "./params/msra_NER"

if config.dataset == "msra":
    config.train_path= "./datasets/MSRA/train.bmes"
    config.test_pah= "./datasets/MSRA/test.bmes"
    config.char_embedding = "./embedding/gigaword_chn.all.a2b.uni.ite50.vec"
    config.bigram_embedding = "./embedding/gigaword_chn.all.a2b.bi.ite50.vec"
    config.word_embedding = "./embedding/ctb.50d.vec"
    config.all_embeddings = "./embedding/hyd_mix_embedding.vec"
    config.diction = "./embedding/dictions.json"
    config.indexing ="./embedding/indexing.json"