import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(10,
                                    20,
                                    size=(3,4)),
                  index=['A1','A2','A3'],
                  columns=['B1','B2','B3','B4'])
print(df)
df1 = pd.DataFrame(np.random.randint(10,20,size=(9,9)))
print(df1)
df2 = pd.DataFrame(np.zeros(shape=(3,4)))
print(df2)