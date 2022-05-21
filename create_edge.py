import numpy as np
import pandas as pd

df = pd.read_csv("../datasets/sp500_companies.csv")
company_list = df["Symbol"].unique()
sector_list = df["Sector"].unique()
name2index = {}
for i, key in enumerate(company_list):
    name2index[key] = i


outer_edge = []
for i in range(len(sector_list)):
    for j in range(i, len(sector_list)):
        outer_edge.append((i, j))

inner_edge = []
for sector in sector_list:
    intra_companies = df[df.Sector == sector]["Symbol"].unique()
    for i in range(len(intra_companies)):
        for j in range(i, len(intra_companies)):
            inner_edge.append((name2index[intra_companies[i]], name2index[intra_companies[j]]))

inner_edge = np.array(inner_edge)
outer_edge = np.array(outer_edge)
np.save("../datasets/inner_edge.npy", inner_edge)
np.save("../datasets/outer_edge.npy", outer_edge)
print(inner_edge.shape, outer_edge.shape)
