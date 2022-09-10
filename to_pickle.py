import pickle
from enum import Enum
from glob import glob

import pandas as pd


class PalmOrientation(Enum):
    DOWN = 0
    MIDDLE = 1
    SIDE = 2


# get existing paths
paths = sorted(glob("./*csv"))
print(paths)

# concatenate them together
df_train, df_test = pd.DataFrame(), pd.DataFrame()
for path in paths:
    tmp = pd.read_csv(path)

    # determine a palm information
    if "down" in path:
        palm = PalmOrientation.DOWN.value
    elif "45" in path:
        palm = PalmOrientation.MIDDLE.value
    else:
        palm = PalmOrientation.SIDE.value

    # append palm information
    tmp["palm_orientation"] = palm

    # train / test split
    if "test" in path:
        df_test = pd.concat([df_test, tmp], ignore_index=True, axis=0)
    else:
        df_train = pd.concat([df_train, tmp], ignore_index=True, axis=0)

# save as pickle with train/test keys
dataset = {
    "train": df_train.to_numpy(),
    "test": df_test.to_numpy()
}

with open("biotac2.pickle", "wb") as f:
    pickle.dump(dataset, f)
