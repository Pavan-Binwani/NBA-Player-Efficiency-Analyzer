import pandas as pd

def load_eligible():
    df = pd.read_csv("data/nba_per_game.csv")

    mask = (df["G"] >= 20) & (df["MP"] >= 10) & (df["FGA"] >= 2)
    df_no_dupe = df.drop_duplicates(subset="Rk")

    eligible = df_no_dupe[mask]
    return eligible