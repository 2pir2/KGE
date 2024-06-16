from pykeen.triples import TriplesFactory
from pykeen.pipeline import pipeline
from pykeen.datasets.nations import NATIONS_TRAIN_PATH
import pandas as pd

tf = TriplesFactory.from_path(
    r"C:\Users\hanxu\Desktop\KGE\Final_Dataset\HeadOrTail_dataset.tsv")
training, testing = tf.split()

result = pipeline(
    model='RGCN',
    training=training,
    testing=testing,
    training_kwargs=dict(
        num_epochs=100,
        batch_size=32,
        sampler='schlichtkrull'
    ),
    model_kwargs=dict(
        embedding_dim=16,
        num_layers=2,
    ),
    optimizer_kwargs=dict(
        lr=0.01,
    ),
    regularizer_kwargs=dict(
        weight=0.0005,
    )
)


result.save_to_directory('doctests/RGCN')
print(result.get_metric('hits_at_k'))
