import pandas as pd
from pathlib import Path

CURRENT_FOLDER = Path(__file__).parent
PARENT_FOLDER = CURRENT_FOLDER.parent

def load_data():
    df1 = pd.read_csv(PARENT_FOLDER / 'data' / 'raw' / 'Used_Car_Dataset.csv')

    print(df1.columns)

    df2 = pd.read_csv(PARENT_FOLDER / 'data' / 'raw' / 'vehicles.csv')

    print(df2.columns)

load_data()