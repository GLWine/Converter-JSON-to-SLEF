#!/usr/bin/env python
# coding=utf-8

import json

_data = None


def loader_JSON(file):  # file è il percorso del file json
    with open(file) as json_file:  # file è il percorso del file json
        _data = json.load(json_file)  # carica il file json in una variabile

    print("Chiavi primarie del Json:")  # stampa le chiavi primarie del json
    print(
        f"|#| La var [ _data ] è di tipo: [{type(_data)}] |#|\r",
        f"    Contiene le: {_data.keys()}\r\r",
        "########################################################\r",
    )
    return _data


def parser_JSON(_data):  # file è il percorso del file json
    key1 = list(_data.keys())
    for k in key1:  # le chiavi primarie del json
        # print("    -", k)  # stampa i valori delle chiavi primarie del json
        if type(_data[k]) is dict:  # se la chiave è un dizionario
            print(
                f"|#| La key [ {k} ] è di tipo: [{type(_data[k])}] |#|"
            )  # stampa i valori delle chiavi primarie del json

        elif type(_data[k]) is list:
            print(_data[k][0].keys())
            # print(f"|#| La key [ {_data[k][0]} ] è di tipo: [{type(_data[k][0])}] |#|")

        else:
            print(f"|#| La key [ {k} ] è di tipo: [{type(_data[k])}] |#|")

        print("\rTipo di _data:", type(_data))
    return _data


loader_JSON(
    "E:\\Giampiero\\Documents\\GitHub\\Converter-JSON-to-SLEF\\"
    "src\\build_ship\\json_build\\PVE-Federal_Corvette_DtEA.json"
)
