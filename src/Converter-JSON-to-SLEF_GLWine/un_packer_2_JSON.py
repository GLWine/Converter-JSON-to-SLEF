#!/usr/bin/env python
# coding=utf-8
# TODO: rimuovere il noqa una volta che il codice è stato finito
from un_packer_1_JSON import (  # noqa: F401
    # variables
    main_folder,
    list_of_first_level_json_frag_paths,
    # function
    loader_JSON,
    item_finder,
    first_frag_file_generator,
    start,
)

folder_of_second_level_frag: str = (
    "E:\\Giampiero\\Documents\\GitHub\\Converter-JSON-to-SLEF\\src\\build_ship\\json_build\\fragment_first_level_json\\fragment_second_level_json\\"
)

list_of_second_level_json_frag_paths: list = []


def find_return_dict():
    for i in range(len(list_of_first_level_json_frag_paths)):
        loaded_file = loader_JSON(f"{list_of_first_level_json_frag_paths[i]}")
        print(f"## stampo la lunghezza di {loaded_file.keys()}: {len(loaded_file.keys())} ##\r")
        for j in range(len(loaded_file.keys())):
            if isinstance(loaded_file[list(loaded_file.keys())[j]], dict):
                # print(f"contenuto lista: {loaded_file[list(loaded_file.keys())[j]]}")
                print("pass")
            else:
                print(f"Il tipo è: {type(loaded_file[list(loaded_file.keys())[j]])}, non va bene!")
                print(f"stampo il contenuto: {loaded_file}\r")


start()

find_return_dict()
