from urllib import request
import os
url=f"https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset/download?datasetVersionNumber=1"
filename="UCI_Credit_Card.csv"
request.urlretrieve(url, os.path.join(os.getcwd(),"dataset.csv"))
print(os.getcwd())