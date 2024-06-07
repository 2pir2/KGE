from pykeen.triples import TriplesFactory
from pykeen.pipeline import pipeline
from pykeen.datasets.nations import NATIONS_TRAIN_PATH
import pandas as pd

tf = TriplesFactory.from_path(
    r"C:\Users\hanxu\Desktop\KGE\PrepRelation\Di_Sy_res_triples.tsv")
training, testing = tf.split()

result = pipeline(
    model='TransE',
    training=training,
    testing=testing,
    training_kwargs=dict(
        num_epochs=100,
        batch_size=256,
    ),
    model_kwargs=dict(
        embedding_dim=64,

    ),
    optimizer_kwargs=dict(
        lr=0.01,
    ),
    regularizer_kwargs=dict(
        weight=0.0001,
    ),
)

result.save_to_directory('doctests/TransE')
print(result.get_metric('hits_at_k'))
