import pandas as pd

def extract_colors(colors):
    return pd.read_csv(colors)

if __name__ == "__main__":
    colors_df = extract_colors('data/The Joy Of Painiting - Colors Used')
    print(colors_df.head())