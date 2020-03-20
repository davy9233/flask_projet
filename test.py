import pandas as pd
import numpy as np
data =  pd.read_csv(r"C:\flask_projet\sauvegarde\5000_movies.csv", sep=',')
test = data.describe()
print(data.select_dtypes(include="object").columns)


nb_l=int(test.shape[0])
print(nb_l)
print(len(test))