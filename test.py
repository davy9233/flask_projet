import pandas as pd
import numpy as np
data =  pd.read_csv(r"C:\flask_projet\sauvegarde\5000_movies.csv", sep=',')
test = data.describe()
for k in test:
    print(test[k])


