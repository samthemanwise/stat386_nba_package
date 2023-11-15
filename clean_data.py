#Load in 2022-2023 Regular Season Data

#Link: https://www.basketball-reference.com/leagues/NBA_2023_advanced.html
#Hide the partial rows

import pandas as pd

# Read the CSV file into a DataFrame
reg22_23 = pd.read_csv("2022-2023reg.csv")

reg22_23.head()

#Clean Data

reg22_23.drop(index = 0, inplace = True)

columns_to_drop = ["Unnamed: 19", "Unnamed: 24", "Player-additional", "Rk"]

reg22_23.drop(columns=columns_to_drop, axis=1, inplace=True)

#Load in 2022-2023 Playoff Data

#Link: https://www.basketball-reference.com/playoffs/NBA_2023_advanced.html

# Read the CSV file into a DataFrame
playoff22_23 = pd.read_csv("2022-2023playoff.csv")

playoff22_23.head()

#Clean Data

columns_to_drop = ["Unnamed: 19", "Unnamed: 24", "Player-additional", "Rk"]

playoff22_23.drop(columns=columns_to_drop, axis=1, inplace=True)
