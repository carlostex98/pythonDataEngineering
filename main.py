import pandas as pd


def start():
    print(f'Reading data')
    df = pd.read_csv('data/MOCK_DATA.csv')
    print(df.head())


if __name__ == '__main__':
    start()
