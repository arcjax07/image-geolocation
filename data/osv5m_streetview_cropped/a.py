import pandas as pd


print("begining the processing of the dataframes")
test_df = pd.read_csv("./data/osv5m_streetview_cropped/test.csv")
train_df = pd.read_csv("./data/osv5m_streetview_cropped/train.csv")
final_df = pd.concat([test_df, train_df], axis=0)


print("done with processing the dataframes")
print(list(test_df))
print(list(train_df))
print(list(set(train_df) - set(test_df)))
# test_df.insert(0,
