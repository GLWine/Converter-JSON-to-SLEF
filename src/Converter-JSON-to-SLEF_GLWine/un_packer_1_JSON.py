#!/usr/bin/env python
# coding=utf-8

import json

main_folder: str = (
    "E:\\Giampiero\\Documents\\GitHub\\Converter-JSON-to-SLEF\\src\\build_ship\\json_build\\"
)
folder_of_first_level_frag: str = (
    "E:\\Giampiero\\Documents\\GitHub\\Converter-JSON-to-SLEF\\src\\build_ship\\json_build\\fragment_first_level_json\\"
)

list_of_first_level_json_frag_paths: list = []


def loader_JSON(file: str) -> dict:  # file è il percorso del file json
    """
    Questa funzione carica un file JSON dal percorso file specificato e restituisce i dati come dizionario.

    parametri:
    file (str): il percorso del file JSON da caricare.

    Ritorna:
    dict: i dati JSON come dizionario.

    Solleva:
    FileNotFoundError: se il file specificato non esiste.
    json.JSONDecodeError: se il file JSON contiene una sintassi non valida.
    """

    with open(file) as json_file:  # file è il percorso del file json
        data: dict = json.load(json_file)  # carica il file json in una variabile
    return data  # restituisce il dizionario


def item_finder(json_dict: dict) -> list:
    """
    Questa funzione accetta un dizionario come input, che si presuppone sia un oggetto JSON.
    Quindi estrae ciascuna coppia chiave-valore dal dizionario e la memorizza in un elenco di dizionari.
    Ogni dizionario nell'elenco contiene una singola coppia chiave-valore dal dizionario di input.

    parametri:
    json_dict (dict): un dizionario che rappresenta un oggetto JSON.

    Ritorna:
    list: un elenco di dizionari, in cui ciascun dizionario contiene una singola coppia chiave-valore dal dizionario di input.

    Solleva:
    TypeError: se l'input non è un dizionario.
    """

    pack: list = []
    if isinstance(json_dict, dict):
        for key, value in json_dict.items():  # carica il file json in una variabile
            pack.append({key: value})  # carica il file json in una variabile
    else:
        raise TypeError("il valore passato non è un dizionario")
    return pack


def first_frag_file_generator(pack_of_fragment: list) -> None:
    """
    Questa funzione genera file JSON per ogni frammento nell'elenco fornito.
    Ogni file è denominato "00i-nome_indice.json" e salvato nella directory specificata da "directory_frag_first_level_json".
    Se il file esiste già, verrà sovrascritto. Se non esiste, verrà creato.

    parametri:
    pack_of_fragment (list): un elenco di dizionari, in cui ciascun dizionario rappresenta un frammento.

    Ritorna:
    Nessuno

    Solleva:
    TypeError: se l'input non è un elenco.
    """

    if not isinstance(pack_of_fragment, list):
        raise TypeError("il valore passato non è una lista")

    for i in range(len(pack_of_fragment)):
        stamp_element = list(pack_of_fragment[i].keys())[0]
        # print(stamp_element)
        try:  # se il file esiste allora:
            with open(  # apre il file se esiste
                # f"prende la directory, ci aggiunge 00 + il numero e il nome del frammento.json"
                f"{folder_of_first_level_frag}00{i}-{stamp_element}.json",
                "w",  # apre in modalità sovrascrivi
            ) as json_file:
                # json.dump(frammento del json, nel file, indent 4)
                json.dump(
                    pack_of_fragment[i], json_file, indent=4
                )  # effettua il dump del frammento nel file con l'indentazione 4
                list_of_first_level_json_frag_paths.append(
                    f"{folder_of_first_level_frag}00{i}-{stamp_element}.json"
                )  # carica la directory nella lista
        except FileNotFoundError:  # se il file non esiste allora:
            with open(  # crea e apre il file se non esiste
                # f"prende la directory, ci aggiunge 00 + il numero e il nome del frammento.json"
                f"{folder_of_first_level_frag}00{i}-{stamp_element}.json",
                "x",  # crea il file e ci scrive
            ) as json_file:
                # json.dump(frammento del json, nel file, indent 4)
                json.dump(
                    pack_of_fragment[i], json_file, indent=4
                )  # effettua il dump del frammento nel file con l'indentazione 4
                list_of_first_level_json_frag_paths.append(
                    f"{folder_of_first_level_frag}00{i}-{stamp_element}.json"
                )  # carica la directory nella lista


def start():
    first_frag_file_generator(
        item_finder(  #
            loader_JSON(
                f"{main_folder}PVE-Federal_Corvette_DtEA.json"
            )  # carica il file json dalla posizione
        )
    )
    print("un_packer_1_JSON finished\r")


def extract_key_structure(json_obj: dict) -> dict:
    """
    This function extracts the structure of keys from a given JSON object.
    It returns a new JSON object with the same structure but only containing the keys.
    The values are replaced with None.

    Parameters:
    json_obj (dict): The JSON object from which to extract the key structure.

    Returns:
    dict: A new JSON object with the same structure as the input, but only containing the keys.
          The values are replaced with None.

    Example:
    >>> json_obj = {
        "name": "John",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "New York"
        },
        "hobbies": ["reading", "painting"]
    }
    >>> extract_key_structure(json_obj)
    {
        "name": None,
        "age": None,
        "address": {
            "street": None,
            "city": None
        },
        "hobbies": [
            {"list": None},
            {"list": None}
        ]
    }
    """

    def extract_keys(obj: dict) -> (dict | list | None):
        """
        A helper function that recursively extracts the keys from a JSON object.

        Parameters:
        obj (dict | list): The JSON object or list from which to extract the keys.

        Returns:
        dict | list | None: A new JSON object or list with the same structure as the input,
                           but only containing the keys. The values are replaced with None.
        """
        if isinstance(obj, dict):
            return {key: extract_keys(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [{"list": extract_keys(item)} for item in obj]
        else:
            return None

    return extract_keys(json_obj)
