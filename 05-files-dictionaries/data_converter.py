from os import listdir
from json import dump

def parse_txt_to_json(filePath: str):
    with open(filePath, 'r', encoding="utf8") as file:
        rawData = file.readlines()
    
    name_hp_type = rawData[0].strip("\n").split(',')

    name = name_hp_type[0]
    hp = int(name_hp_type[1])
    poke_type = name_hp_type[2]

    abilityRow = rawData[1].strip("\n").split(',')

    ability_name = abilityRow[0]
    ability_desc = abilityRow[2]

    move_row = rawData[2].strip("\n").split(',')

    move_name = move_row[0]
    move_costs = move_row[2].strip().split(" ")

    move_costs_converted = dict()
    for index in range(0, len(move_costs)-1, 2):
        move_costs_converted[move_costs[index]] = move_costs[index+1]


    move_dmg = move_row[3]
    move_desc = ','.join(move_row[4:])

    data = {
        "name": name,
        "HP": hp,
        "type": poke_type,

        "ability": {
            "name": ability_name,
            "description": ability_desc
        },

        "move": {
            "name": move_name,
            "cost": move_costs_converted,
            "damage": move_dmg,
            "description": move_desc
        }
}
    return data

def get_data_from_folder(folderPath: str) -> list:
    fileNames = listdir(folderPath)

    pokemon = list()
    for file in fileNames:
        pokemon.append(parse_txt_to_json(f"{folderPath}/{file}"))

    return pokemon

def save_converted_data(pokemon: list, end_path: str):
    for element in pokemon:
        with open(f'{end_path}/{element["name"]}.json', 'w') as out_file:
            dump(element, out_file)
    return

def main():
    pokemon = get_data_from_folder('05-files-dictionaries/transkiberad-data/')
    save_converted_data(pokemon, '05-files-dictionaries/konverterad-data')


if __name__ == '__main__':
    main()