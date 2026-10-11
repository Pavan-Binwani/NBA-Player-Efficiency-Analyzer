from data_loader import load_eligible
import pandas as pd
import unicodedata

MIN_PLAYERS = 2
MAX_PLAYERS = 5

eligible = load_eligible()

def strip_accents(text):
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch))

def find_player(name, df):
    result = df[strip_accents(name.strip().lower()) == df["Player"].apply(strip_accents).str.lower()]
    if result.empty:
        return None
    return result

def parse_names(text):
    cleaned = []
    for player in text.split(","):
        if player.strip():
            cleaned.append(player.strip())
    return cleaned

def lookup_names(names, df):
    found = []
    found_names = []
    not_found = []
    for name in names:
        result = find_player(name, df)
        if result is None:
            if name not in not_found:
                not_found.append(name)
        else:
            player_name = result["Player"].iloc[0]
            if player_name not in found_names:
                found.append(result)
                found_names.append(player_name)
    if not found:
        return None, not_found
    combined = pd.concat(found)
    return combined, not_found
        
found, missing = lookup_names(parse_names("zzz, qqq"), eligible)
print(found)
print(missing)

# Input Loop
def get_players(df):
    while True:
        text = input("Enter the full names of the players you would like to compare, separated by commas (or enter 'quit'): ")
        if (text.strip().lower() == "quit"):
            return None
        else:
            cleaned_text = parse_names(text)
            if not cleaned_text:
                print("No valid player names were entered. Please try again.")
            else:
                names_found, names_missing = lookup_names(cleaned_text, df)
                if names_found is None:
                    print("None of those players were found. Please try again.")
                elif len(names_missing) > 0:
                    print(f"The following names were not found: {', '.join(names_missing)}") 
                elif len(names_found) < MIN_PLAYERS:
                    print(f"You need to compare a minimum of {MIN_PLAYERS} players. Try again.")
                elif len(names_found) > MAX_PLAYERS:
                    print(f"You cannot compare more than {MAX_PLAYERS} players. Try again.")
                else:
                    return names_found

def show_comparison(players):
    players_new = players.copy()
    players_new["TS"] = round(players_new["TS"] * 100, 1)
    print(players_new[["Player", "Team", "G", "MP", "PTS", "FGA", "TS"]].to_string(index=False))

# Putting Everything Together
while True:
    players = get_players(eligible)
    if players is None:
        break
    show_comparison(players)