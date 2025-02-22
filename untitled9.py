# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RsOGxGOlP1Ii6Fprv_-afRUu39sZmXI1
"""

from fastai import *
from fastai.vision import *
from fastai.metrics import error_rate
import os
import pandas as pd
import numpy as np
from pathlib import Path

from google.colab import drive
drive.mount('/content/drive')

from pathlib import Path

x = "/content/drive/My Drive/face mask data/train"
path = Path(x)

print(path.ls())

from fastai.vision import *

from fastai.vision.all import *
np.random.seed(40)

data = ImageDataLoaders.from_folder(path, train='.', valid_pct=0.2,
                                  item_tfms=Resize(224), # Resize images to 224x224
                                  batch_tfms=[*aug_transforms(size=224), Normalize.from_stats(*imagenet_stats)]) #  normalization

data.show_batch(max_n=9, figsize=(7,6), nrows=3)

print(data.train_ds.vocab)
len(data.train_ds.vocab)
data.c

data

learn = cnn_learner(data, models.resnet50, metrics=[accuracy], model_dir = Path('../kaggle/working'),path = Path("."))

learn = cnn_learner(data, models.resnet50, metrics=[accuracy])

learn.lr_find()
learn.scheduler.plot()

learn = cnn_learner(data, models.resnet18, metrics=accuracy)

lr1 = 1e-3
lr2 = 1e-1
learn.fit_one_cycle(4,slice(lr1,lr2))

learn.export("/content/drive/My Drive/face_mask_model.pkl")

learn = load_learner("/content/drive/My Drive/face_mask_model.pkl")

learn.save("/content/drive/My Drive/face_mask_stage-1")
learn.load("/content/drive/My Drive/face_mask_stage-1")

learn.unfreeze()
learn.fit_one_cycle(10,slice(1e-4,1e-3))

interp = ClassificationInterpretation.from_learner(learn)
interp.plot_confusion_matrix()

interp.plot_top_losses(6,figsize = (25,5))

