from pathlib import Path
import pandas as pd
import numpy as np
import country_converter as coco
from pandarallel import pandarallel
from kgcpy import lookupCZ
import json

# Initialize pandarallel
pandarallel.initialize(progress_bar = True)

# Move all of the images up into the image directory
images_dir = Path("./data/osv5m_streetview_cropped/images/")
train_images_dir = Path("./data/osv5m_streetview_cropped/images/train/")
test_images_dir = Path("./data/osv5m_streetview_cropped/images/test/")

# Driving side data
driving_side_data = json.load(open("./data/driving_side/countries_driving_side.json"))
print(driving_side_data)

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

# Generate Train, Val, Test Split
# From: https://stackoverflow.com/a/69833830
final_df["selection"] = pd.NA 
selection = ["train", "val", "test"]
final_df["selection"] = final_df["selection"].parallel_apply(lambda x: np.random.choice(selection, p=[0.80, 0.10, 0.10]))

# Add the country_names to be country codes but the full form (US -> United States)
# Create mapping dictionary for unique country codes
unique_countries = final_df['country'].unique()
country_dict = {code: coco.convert(names=str(code), to='name_short', not_found='countrynotfound') 
                for code in unique_countries}

# Use the mapping dictionary instead of converting each row
final_df["country_name"] = final_df['country'].map(country_dict)

# Add in source component to get the images!
final_df["source"] = final_df.parallel_apply(lambda row: str(images_dir / str(row.id)), axis = 1)

# Create the climate column of the data in the dataframe
final_df["climate_zone"] = final_df.parallel_apply(lambda row: lookupCZ(row.latitude, row.longitude), axis = 1)

final_df.to_csv("./data/osv5m_streetview_cropped/metadata.csv")

print(final_df.iloc[0])
print(final_df["selection"].value_counts())

print("done with processing the dataframes")
print(list(test_df))
print(list(train_df))
print(list(set(train_df) - set(test_df)))