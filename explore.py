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
import matplotlib.pyplot as plt

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

# Finding Top 10% of PPG & TS%
PPG_cutoff = eligible["PTS"].quantile(0.90)
print(PPG_cutoff)
top_PPG_mask = (eligible["PTS"] >= PPG_cutoff)

TS_cutoff = eligible["TS"].quantile(0.90)
print(TS_cutoff)
top_TS_mask = (eligible["TS"] >= TS_cutoff)

top_PPG = eligible[top_PPG_mask]
top_TS = eligible[top_TS_mask]

# Testing Mask
print(top_PPG.shape)
print(top_TS.shape)

# Checking for Overlap
overlap_check = top_PPG["Player"].isin(top_TS["Player"])
overlap = overlap_check.sum()
overlap_percent = (overlap / len(top_PPG)) * 100

print(overlap)
print(overlap_percent)
print(top_PPG[overlap_check]["Player"])

# Scoring Volume & Efficiency Comparison
print(top_PPG["TS"].mean())
print(eligible["TS"].mean())

r = eligible["PTS"].corr(eligible["TS"])
print(r)

print(eligible.sort_values("TS", ascending=False)[["Player", "G", "MP", "PTS", "FGA", "TS"]].head(5))
print(top_TS["FGA"].mean())
print(eligible["FGA"].mean())

# Starting the Plot
plt.figure("NBA Scoring vs Efficiency")
plt.scatter(eligible["PTS"], eligible["TS"]*100)
plt.xlabel("Points Per Game")
plt.ylabel("True Shooting Percentage (%)")
plt.title("PPG vs TS% Scatter Plot")
plt.show()