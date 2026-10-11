import pandas as pd

def load_eligible():
    df = pd.read_csv("data/nba_per_game.csv")

    df_no_dupe = df.drop_duplicates(subset="Rk")
    mask = (df_no_dupe["G"] >= 20) & (df_no_dupe["MP"] >= 10) & (df_no_dupe["FGA"] >= 2)

    eligible = df_no_dupe[mask]
    eligible["TS"] = eligible["PTS"] / (2 * (eligible["FGA"] + 0.44 * eligible["FTA"]))
    return eligible