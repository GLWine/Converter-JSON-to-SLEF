#!/usr/bin/env python
# coding=utf-8

import json

reanalisi_list: list = []


def loader_JSON(file: str) -> dict:  # file è il percorso del file json
    with open(file) as json_file:  # file è il percorso del file json
        data: dict = json.load(json_file)  # carica il file json in una variabile
    return data


def parser_JSON(json_loaded: dict):  # file è il percorso del file json
    print("Chiavi primarie del Json:")  # stampa le chiavi primarie del json
    print(
        f"|#| L'oggetto analizzato è di tipo: [{type(json_loaded)}] |#|\r",
        f"    Contiene le: {json_loaded.keys()}\r\r",
        "########################################################\r",
    )

    keys1 = list(json_loaded.keys())  # crea una lista con le chiavi primarie del json
    for key1 in keys1:  # cicla le chiavi primarie del json

        if type(json_loaded[key1]) is dict:  # se la chiave è un dizionario
            # stampa i valori delle chiavi primarie del json
            print(f"|#| La key [ {key1} ] è di tipo: [{type(json_loaded[key1])}] |#|")

        elif type(json_loaded[key1]) is list:
            for i in range(len(json_loaded[key1])):
                print(
                    f"|#| La key [ {key1} ] è di tipo: [{type(json_loaded[key1][i])}] |#|"
                )

                if type(json_loaded[key1][i]) is dict:  # se il tipo è un dizionario
                    print(f"    Dizzionario contenuto alla pozizione {i} della lista {key1}: {json_loaded[key1][i].keys()}")
                    sub_dict: dict = json_loaded[key1][i]  # crea una variabile con il valore della chiave primaria
                    reanalisi_list.append(sub_dict)
                else:  # altrimenti
                    raise TypeError(
                        f"La variabile è di tipo: [{type(json_loaded[key1][i])}], invece dovrebbe essere un dict!"
                    )  # solleva un errore indicando il tipo della variabile

        elif type(json_loaded[key1]) is str:
            print(f"|#| La key [ {key1} ] è di tipo: [{type(json_loaded[key1])}] |#|")

        else:
            print(f"|#| La key [ {key1} ] è di tipo: [{type(json_loaded[key1])}] ERROR |#|")


def ricorsione(variabile: dict) -> None:
    for key2 in variabile:  # cicla le chiavi primarie del json
        if type(variabile[key2]) is dict:  # se la chiave è un dizionario
            # stampa i valori delle chiavi primarie del json
            print(f"|#| La key [ {key2} ] è di tipo: [{type(variabile[key2])}] |#|")

        elif type(variabile[key2]) is list:
            print(
                f"|#| La key [ {key2} ] è di tipo: [{type(variabile[key2][0].keys())}] |#|"
            )
            print(variabile[key2][0].keys())

        else:
            print(f"|#| La key [ {key2} ] è di tipo: [{type(variabile[key2])}] |#|")


parser_JSON(
    loader_JSON(
        "E:\\Giampiero\\Documents\\GitHub\\Converter-JSON-to-SLEF\\"
        "src\\build_ship\\json_build\\PVE-Federal_Corvette_DtEA.json"
    )
)
