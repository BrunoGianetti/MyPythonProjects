import pandas as pd

# Extract .dat
dataframe = pd.read_csv('data.dat', sep=',')
dataframe.to_excel('data_dat.xlsx', index=False)

# Extract .fid
dataframe = pd.read_csv('data.fid', sep=',')
dataframe.to_excel('data_fid.xlsx', index=False)

# Extract .idx
dataframe = pd.read_csv('data.idx', sep=',')
dataframe.to_excel('data_idx.xlsx', index=False)