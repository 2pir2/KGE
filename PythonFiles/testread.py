import pykeen
from pykeen.triples import TriplesFactory
from pykeen.pipeline import pipeline
from pykeen.datasets.nations import NATIONS_TRAIN_PATH
import pandas as pd
import torch
from torch.optim import Adam
from pykeen.training import SLCWATrainingLoop
from pykeen import predict
from typing import List
from pykeen.datasets import Nations
import pykeen.nn
from pykeen.pipeline import pipeline
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

model = torch.load(
    r"C:\Users\hanxu\Desktop\KGE\TestResult\test_unstratified_transe\trained_model.pkl")
model.plot()
entity_representation_modules: List['pykeen.nn.Representation'] = model.entity_representations
relation_representation_modules: List['pykeen.nn.Representation'] = model.relation_representations

entity_embeddings: pykeen.nn.Embedding = entity_representation_modules[0]
relation_embeddings: pykeen.nn.Embedding = relation_representation_modules[0]

entity_embedding_tensor: torch.FloatTensor = entity_embeddings()
relation_embedding_tensor: torch.FloatTensor = relation_embeddings()

entity_embedding_tensor: torch.FloatTensor = entity_embeddings(indices=None)
relation_embedding_tensor: torch.FloatTensor = relation_embeddings(
    indices=None)

entity_embedding_tensor = entity_embedding_tensor.detach().cpu().numpy()
relation_embedding_tensor = relation_embedding_tensor.detach().cpu().numpy()
