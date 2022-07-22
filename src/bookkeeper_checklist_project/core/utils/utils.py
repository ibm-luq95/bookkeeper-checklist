# -*- coding: utf-8 -*-#
from django.utils.translation import gettext as _


def sort_dict(dict_object: dict) -> dict:
    res = dict()
    for k, v in sorted(dict_object.items()):
        if isinstance(v, dict):
            res[k] = sort_dict(v)
        else:
            res[k] = v
    return res


def get_trans_txt(txt):
    return _(txt)
