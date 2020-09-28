import requests

def get_stats():
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()

    # abilities
    abilities = r["abilities"]

    for ability in abilities:
        Ability = ability['ability']['name']
        Hidden = ability['is_hidden']
        Slot = ability['slot']



    # forms
    forms = r["forms"]

    for form in forms:
        Form_name = (form['name'])

    print()

    # species
    species = r["species"]

    Species_name = species['name']


    # types
    types = r["types"]

    for poke_type in types:
        Slot_number = (poke_type['slot'])
        Type_name = (poke_type['type']['name'])
    return Slot_number, Hidden, Type_name, Species_name, Form_name, Slot, Ability

Slot_number, Hidden, Type_name, Species_name, Form_name, Slot, Ability = get_stats()




