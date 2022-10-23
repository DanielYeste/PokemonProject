import pandas as pd


class Model:

    def __init__(self, database):
        self.database = pd.read_csv(database)

    def cleanPokemonName(self, name):
        firstLetter = True
        cleanedString = ""
        for letters in name:
            if letters != " ":
                if firstLetter:
                    x = letters.upper()
                    firstLetter = False
                else:
                    x = letters.lower()
                cleanedString += x
        return cleanedString

    # Clean the stronger types
    def defineDisadvantatges(self, typesList, effectiveness):
        trainerMessage = "This pokemon has a disadvantatge of x" + effectiveness + " against: "
        for types in typesList:
            type = types.replace('against_', '')
            trainerMessage += type + ", "
        print(trainerMessage[:-2])

        '''searchPokemon = pokemon_dataset.loc[pokemon_dataset['name'] == "Snorlax"]
    effectiveness = [0, 0.25, 0.5, 2, 4]
    for damage in effectiveness:
        getTypes = searchPokemon[["type1", "type2", "against_bug", "against_dark",
                                  "against_dragon", "against_electric", "against_fairy",
                                  "against_fight", "against_fire", "against_flying",
                                  "against_ghost", "against_grass", "against_ground",
                                  "against_ice", "against_normal", "against_poison",
                                  "against_psychic", "against_rock", "against_steel",
                                  "against_water"]] == damage
        disadvantatgeTypes = getTypes.apply(lambda row: row[row].index.tolist(), axis=1)
        if not len(disadvantatgeTypes.values[0]) == 0:
            cleanStrongestTypes(disadvantatgeTypes.values[0], str(damage))'''
