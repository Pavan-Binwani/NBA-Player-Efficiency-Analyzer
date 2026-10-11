from data_loader import load_eligible
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

print(find_player("luka doncic", eligible[["Player", "Team", "PTS", "TS"]]))
print(find_player("  NIKOLA JOKIC ", eligible[["Player", "Team", "PTS", "TS"]]))
print(find_player("not a player", eligible))