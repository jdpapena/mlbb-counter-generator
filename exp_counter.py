import json
import difflib

# Storage of every counter
def load_hero_database():
    try:
        with open("heroes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("WARNING: 'heroes.json' file missing! Make sure it's in the same folder.")
        return {}

def run_counter_engine():
    print("--------------------------------------------------")
    print("MLBB EXP-Lane Counter-Draft Generator")

    # Loading database of hero counters
    hero_database = load_hero_database()
    
    if not hero_database:
        return
    
    # 1. User input
    enemy_pick = input("Enter your laning opponent's name: ").strip().lower()

    # 2. Extract all the heroes from the JSON file
    hero_names = list(hero_database.keys())

    # 3. Check for close spelling match using difflib. n=1 is single similar result, cutoff=0.6 is at least 60% similarity.
    close_matches = difflib.get_close_matches(enemy_pick, hero_names, n=1, cutoff=0.6)

    match_found = False
    db_name = None

    # 4A. Typo found, store to db_name the returned similar name in database
    if close_matches:
        db_name = close_matches[0]
        match_found = True

    # 4B. Other cases, removing whitespace and hyphen
    else:
        enemy_pick_clean = enemy_pick.replace(" ", "").replace("-", "")
        for name in hero_names:
            if name.replace(" ", "").replace("-", "") == enemy_pick_clean:
                db_name = name
                match_found = True
                break
    
    # 5. Processing and returning data output (engine usage)

    if match_found and db_name in hero_database:
        data = hero_database[db_name]
            
        # Summary of how to counter
        print("--------------------------------------------------")
        print(f"OPPONENT PICK: {db_name.upper()}")

        print(f"--Damage Type: {data['damage_type']}")
        print(f"--To Counter: {data['weak_against']}")
        print("--------------------------------------------------")
            
        # Heroes to pick
        print("COUNTER HEROES:")
        for hero in data['counter_heroes']:
            print(f"• {hero}")
        print("\n")

        # Items to build 
        print("COUNTER ITEMS:")
        for item in data['counter_items']:
            print(f"• {item}")
        print("\n")

        # Gameplay of the enemy pick
        print(f"🟆  GAMEPLAY OF {db_name.upper()} 🟆")
        print(f'- {data['gameplay']}')
        print("\n")
        
    # Case: Not in the database
    else:
        # Add hero or check spelling
        print(f"Hero '{enemy_pick}' not found in the database.")
        print("WARNING: Make sure you spelled it correctly or it is in the list!")
        print("--------------------------------------------------")

# Execute the application
if __name__ == "__main__":
    run_counter_engine()