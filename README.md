### Pickle
To get all the signals concatenated into just one 
pickle with train/test splits just run `python to_pickle.py`
Files will be converted into one pickle in the following format:
```
{
 "train": [
    1 x class name,
    1 x grasp outcome: 0 - stable, 1 - slipped, 
    24 * 3 x electrodes values, 
    1 x palm orientation: 0 - down, 1 - middle, 2 - side
 ]
 
 "test": [
    ...
  ]
    
} -> N x [1, 1, 72, 1]
```

### Data description
Data description reference https://www.syntouchinc.com/wp-content/uploads/2018/08/BioTac-Manual-V.21.pdf
Each sensor consists of an array of 24 electrodes.
```
As forces are applied to the skin, the skin and fluid deform. Changes in
impedance as the fluid deforms are detected by an array of electrodes on the
surface of the BioTac core.
```

# BioTacSp Stability Set (BTS3) V2

This dataset is an extended version of the previously introduced [BioTacSp Images](https://github.com/yayaneath/biotac-sp-images) by Zapata-Impata et. al.

The aforementioned [BioTacSp Images](https://github.com/yayaneath/biotac-sp-images) contains grasp samples performed over 41 objects with different geometries (i.e. cylinders, spheres, boxes), materials (i.e. wood, plastic, aluminum), stiffness levels (i.e. solid, soft) as well as sizes and weights. This extended version adds a test set of 10 new objects with similar materials but different geometries and stiffness levels. The original 41 were left for the training and validation purposes. Here we show a group photo of both sets.

<p align="center">
  Train Objects
  <img src="https://github.com/3dperceptionlab/biotacsp-stability-set-v2/blob/master/img/trainobjects2.jpg">
</p>

<p align="center">
  Test Objects
  <img src="https://github.com/3dperceptionlab/biotacsp-stability-set-v2/blob/master/img/testobjects.jpg">
</p>

Both sets, training and test, were recorded following these steps:

1) Grasp the test object: the hand performed a three-fingered grasp that contacted the object with each of the fingers equipped with a tactile sensor.
2) Read the sensors: a single reading was recorded then from each of the sensors at the same time.
3) Lift the object: the hand was raised in order to lift the object and check the outcome.
4) Label the trial: the previously recorded tactile readings were labeled according to the outcome of the lifting with two classes (stable, i.e., it is completely static, or slip, i.e., either fell from the hand or it moves within it).

We have performed grasps using a Shadow Dexterous hand equipped with three BioTac SP tactile sensors in its index finger (ff), middle finger (mf) and thumb (th). The dataset stores 24 values for each of the tactile sensors, the grasped object and whether the object slipped or not from the hand. There are two hand configurations in the original dataset: palm down grasps were performed pointing the palm of the hand downwards while palm side grasps were recorded pointing it to one side, with the thumb upwards. In this work, we have added a new configuration: palm 45 which is in between the other two configurations at an angle of 45 degrees. Pictures below show examples for each orientation.

| Palm Down | Palm 45 | Palm Side | 
|:-:|:-:|:-:|
|![](img/palmdown.jpg) | ![](img/palm45.jpg) | ![](img/palmside.jpg) |
|![](img/palmdown_grasp.jpg) | ![](img/palm45_grasp.jpg) | ![](img/palmside_grasp.jpg) |

The dataset is split into six files, three for the training set and three for the test set with one individual file for each orientation. Here is the list of the provided CSV files.

- bts3v2_palm_down.csv (Training set for the palm down orientation)
- bts3v2_palm_side.csv (Training set for the palm side orientation)
- **NEW** bts3v2_palm_45.csv (Training set for the palm 45 orientation)
- **NEW** bts3v2_palm_down_test.csv (Test set for the palm down orientation)
- **NEW** bts3v2_palm_side_test.csv (Test set for the palm side orientation)
- **NEW** bts3v2_palm_45_test.csv (Test set for the palm 45 orientation)

See the next table for a summary of the whole dataset and its splits:

|               | Training Set |          | Test Set |          |
|---------------|--------------|----------|----------|----------|
| **Configuration** | **Stable**       | **Slippery** | **Stable**   | **Slippery** |
| Palm Down     | 667          | 609      | 153      | 163      |
| Palm Side     | 603          | 670      | 157      | 165      |
| Palm 45       | 1058         | 1075     | 250      | 261      |
| *All*           | *2328*         | *2354*     | *560*      | *589*      |

## Citation

If you use this dataset, please cite:

```
@inproceedings{Garcia-Garcia2019,
  author    = {Alberto Garcia{-}Garcia and
               Brayan S. Zapata{-}Impata and
               Sergio Orts{-}Escolano and
               Pablo Gil and
               Jose Garcia{-}Rodriguez},
  title     = {TactileGCN: A Graph Convolutional Network for Predicting Grasp Stability with Tactile Sensors},
  booktitle = {Proceedings of the International Joint Conference on Neural Networks (IJCNN)}
  year      = {2019},
}

```
