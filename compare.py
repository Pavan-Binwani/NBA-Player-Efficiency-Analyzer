from data_loader import load_eligible
import pandas as pd
import unicodedata

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