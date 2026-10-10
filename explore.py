# Research Question:
# Are the NBA's highest-scoring players also the most efficient scorers?

# Eligible players: 
# at least 20 games, 10 minutes per game, and 2 FGA per game
# with one row per player (traded players use their combined season line)

# Highest-scoring:
# The eligible NBA players in the 90th percentile or higher of points per game (PPG) for the 2025-2026 NBA regular season.

# Most efficient:
# The eligible NBA players in the 90th percentile or higher of true shooting percentage (TS%) for the 2025-2026 NBA regular season. 

# Hypothesis:
# Among eligible NBA players for the 2025-2026 NBA season,
# PPG and TS% will have a medium to high positive correlation (r between 0.5 and 0.7),
# and at least 25% of the players in the 90th percentile of PPG will also be in the 90th percentile of TS%.


# Coding Starts
import pandas as pd

# Initial Data
df = pd.read_csv("data/nba_per_game.csv")
print(df.shape)
print(df.columns)
print(df.head())
print(df.info())
print(df.describe())

#Filter Values
mask = (df["G"] >= 20) & (df["MP"] >= 10) & (df["FGA"] >= 2)
print(mask.sum())
print(df["Team"].isin(["2TM", "3TM"]).sum())

# Cleaning Data of Duplicates
df_no_dupes = df.drop_duplicates(subset="Rk")
print(df_no_dupes.shape)
print(df_no_dupes[df_no_dupes["Player"] == "James Harden"])
print(df_no_dupes["Player"].duplicated().sum())
print(df_no_dupes["Team"].isin(["2TM", "3TM", "4TM"]).sum())

# Filtering Data for Elgible Players
eligible = df_no_dupes[mask]
print(eligible.shape)

# Testing Filter
cols = ["G", "MP", "PTS", "FGA", "FTA"]
print(eligible[cols].isna().sum())

# TS% Calculation
eligible["TS"] = eligible["PTS"] / (2 * (eligible["FGA"] + 0.44 * eligible["FTA"]))
print(eligible[["Player", "PTS", "FGA", "FTA", "TS"]].head())
print(eligible["TS"].describe())