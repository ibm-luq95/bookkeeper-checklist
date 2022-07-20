# -*- coding: utf-8 -*-#


def sort_dict(dict_object: dict) -> dict:
    res = dict()
    for k, v in sorted(dict_object.items()):
        if isinstance(v, dict):
            res[k] = sort_dict(v)
        else:
            res[k] = v
    return res
