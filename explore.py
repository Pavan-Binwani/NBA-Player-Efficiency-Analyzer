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



import pandas as pd

df = pd.read_csv("data/nba_per_game.csv")
print(df.shape)
print(df.columns)
print(df.head())
print(df.info())
print(df.describe())

mask = (df["G"] >= 20) & (df["MP"] >= 10) & (df["FGA"] >= 2)
print(mask.sum())
print(df["Team"].isin(["2TM", "3TM"]).sum())