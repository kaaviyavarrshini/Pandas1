import pandas as pd

# Two-dimensional list
data = [['Geek1', 26, 'Scientist'],
        ['Geek2', 31, 'Researcher'],
        ['Geek3', 24, 'Engineer']]

# Column names
columns = ['Name', 'Age', 'Occupation']

# Creating DataFrame using pd.DataFrame.from_dict()
df = pd.DataFrame.from_dict(dict(zip(columns, zip(*data))))

# Displaying the DataFrame
print(df)