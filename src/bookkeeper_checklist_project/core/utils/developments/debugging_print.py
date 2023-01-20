# -*- coding: utf-8 -*-#
import ast
import logging
import os
import traceback
from typing import Any

if os.environ.get("STAGE_ENVIRONMENT") == "PRODUCTION":
    from prettyprinter import cpprint
    from termcolor import cprint

logger = logging.getLogger(__name__)

IS_DEBUGGING = ast.literal_eval(os.environ.get("DEBUG"))


def debugging_print(txt_object, **kwargs):
    try:
        from rich import print as rprint
        from rich.pretty import pprint
        from rich import inspect
        from rich.console import Console
        from termcolor import cprint

        console = Console()
        if IS_DEBUGGING is True:
            # var_name = f"{txt_object=}".split("=")
            # cprint(f"######### Variable Name: -> {var_name[0]} <- #########", "yellow", attrs=["bold"])
            if kwargs.get("is_cpprint") is True:
                cpprint(txt_object)
            elif kwargs.get("is_inspect") is True:
                inspect(
                    txt_object,
                    methods=kwargs.get("methods"),
                    sort=True,
                    help=kwargs.get("help"),
                    private=kwargs.get("private"),
                    title=f"Debugging info for {str(txt_object)} object",
                )
            else:
                # rprint(txt_object)
                pprint(txt_object, expand_all=True)
                # console.log(txt_object)
    except ImportError:
        logger.error("The package rich not installed!")
        pass
    except Exception:
        logger.error(traceback.format_exc())


def cprint_print(msg: Any, color: str, attrs=None):
    if attrs is None:
        attrs = ["bold"]
    if IS_DEBUGGING is True:
        cprint(msg, color, attrs=attrs)


def get_all_methods(object, is_with_dunder=False) -> list:
    all_methods = []
    for method in dir(object):
        if is_with_dunder is True:
            all_methods.append(method)
        else:
            if not method.startswith("__"):
                all_methods.append(method)
    return all_methods
