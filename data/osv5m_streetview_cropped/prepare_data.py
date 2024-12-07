from pathlib import Path
import pandas as pd
import numpy as np

# Move all of the images up into the image directory
images_dir = Path("./data/osv5m_streetview_cropped/images/")
train_images_dir = Path("./data/osv5m_streetview_cropped/images/train/")
test_images_dir = Path("./data/osv5m_streetview_cropped/images/test/")

for image in train_images_dir.rglob("*.jpg"):
    image.rename(images_dir / image.name)
    # print(images_dir / image.name)
for image in test_images_dir.rglob("*.jpg"):
    image.rename(images_dir / image.name)
    # print(images_dir / image.name)

print("begining the processing of the dataframes")
test_df = pd.read_csv("./data/osv5m_streetview_cropped/test.csv")
train_df = pd.read_csv("./data/osv5m_streetview_cropped/train.csv")
final_df = pd.concat([test_df, train_df], axis=0)

# From: https://stackoverflow.com/a/69833830
final_df["selection"] = pd.NA 
selection = ["train", "val", "test"]
final_df["selection"] = final_df["selection"].apply(lambda x: np.random.choice(selection, p=[0.80, 0.10, 0.10]))
final_df.to_csv("./data/osv5m_streetview_cropped/metadata.csv")

print(final_df["selection"].value_counts())

print("done with processing the dataframes")
print(list(test_df))
print(list(train_df))
print(list(set(train_df) - set(test_df)))
# test_df.insert(0,
