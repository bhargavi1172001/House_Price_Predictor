import pandas as pd


# Preprocessing functions


def load_data(csv_path: str):
return pd.read_csv(csv_path)




def encode_categorical(df: pd.DataFrame):
categorical_columns = [
'mainroad', 'guestroom', 'basement',
'hotwaterheating', 'airconditioning', 'prefarea'
]


for column in categorical_columns:
df[column] = df[column].map({'yes': 1, 'no': 0})


df['furnishingstatus'] = df['furnishingstatus'].map({
'furnished': 2,
'semi-furnished': 1,
'unfurnished': 0
})


return df
