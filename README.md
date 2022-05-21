## Requirements
* pytorch==1.11.0
* pytorch-geometric

## Model architecture
![](https://i.imgur.com/lkCA1Rt.png)



## How to train the model
1. Run clean_data.py
This script would run the preprocessing for raw data and dump a preprocessed file.

2. Run create_edge.py
This script would create a fully-connected graph

3. Run train.py
This script is used for training model
