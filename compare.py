from data_loader import load_eligible

eligible = load_eligible()

def find_player(name, df):
    result = eligible[name.strip().lower() == eligible["Player"].str.lower()]
    return result

print(find_player("  lebron james ", eligible))