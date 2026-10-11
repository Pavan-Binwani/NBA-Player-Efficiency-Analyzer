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

def parse_names(text):
    cleaned = []
    for player in text.split(","):
        if player.strip():
            cleaned.append(player.strip())
    return cleaned


print(parse_names("Jokic, Luka Doncic ,  Shai"))
print(parse_names("Jokic,,  ,Tatum,"))
print(parse_names(""))