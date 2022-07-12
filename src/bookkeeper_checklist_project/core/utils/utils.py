# -*- coding: utf-8 -*-#
from collections import OrderedDict


def sort_dict(dict_object: dict) -> OrderedDict:
    res = OrderedDict()
    for k, v in sorted(dict_object.items()):
        if isinstance(v, dict):
            res[k] = sort_dict(v)
        else:
            res[k] = v
    return res
