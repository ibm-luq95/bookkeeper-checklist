# -*- coding: utf-8 -*-#
from django.core import serializers
from collections.abc import Iterable
from django.db.models.query import QuerySet
from django.core.exceptions import ObjectDoesNotExist
import logging
from logging import Logger


class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = (
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    )

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_formatted_logger(file_name: str) -> Logger:
    logger = logging.getLogger(file_name)
    logger.setLevel(logging.DEBUG)

    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(CustomFormatter())
    logger.addHandler(ch)
    return logger


def dd(request, data=""):
    try:
        scheme = request.scheme
        server_name = request.META["SERVER_NAME"]
        server_port = request.META["SERVER_PORT"]
        remote_addr = request.META["REMOTE_ADDR"]
        user_agent = request.META["HTTP_USER_AGENT"]
        path = request.path
        method = request.method
        session = request.session
        cookies = request.COOKIES

        get_data = {}
        for key, value in request.GET.lists():
            get_data[key] = value

        post_data = {}
        for key, value in request.POST.lists():
            post_data[key] = value

        files = {}
        for key, value in request.FILES.lists():
            files["name"] = request.FILES[key].name
            files["content_type"] = request.FILES[key].content_type
            files["size"] = request.FILES[key].size

        dump_data = ""
        query_data = ""
        executed_query = ""
        if data:
            if isinstance(data, Iterable):
                if isinstance(data, QuerySet):
                    executed_query = data.query
                    query_data = serializers.serialize("json", data)
                else:
                    dump_data = dict(data)
            else:
                query_data = serializers.serialize("json", [data])

        msg = f"""
            <html>
                <span style="color: red;"><b>Scheme</b></span>        : <span style="color: blue;">{scheme}</span><br>
                <span style="color: red;"><b>Server Name</b></span>   : <span style="color: blue;">{server_name}</span><br>
                <span style="color: red;"><b>Server Port</b></span>   : <span style="color: blue;">{server_port}</span><br>
                <span style="color: red;"><b>Remote Address</b></span>: <span style="color: blue;">{remote_addr}</span><br>
                <span style="color: red;"><b>User Agent</b></span>    : <span style="color: blue;">{user_agent}</span><br>
                <span style="color: red;"><b>Path</b></span>          : <span style="color: blue;">{path}</span><br>
                <span style="color: red;"><b>Method</b></span>        : <span style="color: blue;">{method}</span><br>
                <span style="color: red;"><b>Session</b></span>       : <span style="color: blue;">{session}</span><br>
                <span style="color: red;"><b>Cookies</b></span>       : <span style="color: blue;">{cookies}</span><br>
                <span style="color: red;"><b>Get Data</b></span>      : <span style="color: blue;">{get_data}</span><br>
                <span style="color: red;"><b>Post Data</b></span>     : <span style="color: blue;">{post_data}</span><br>
                <span style="color: red;"><b>Files</b></span>         : <span style="color: blue;">{files}</span><br>
                <span style="color: red;"><b>Executed Query</b></span>: <span style="color: blue;"><br>{executed_query}</span><br>
                <span style="color: red;"><b>Query Data</b></span>    : <span style="color: blue;"><br>{query_data}</span><br>
                <span style="color: red;"><b>Dump Data</b></span>     : <span style="color: blue;"><br>{dump_data}</span><br>
            </html>
        """

        return msg
    except ObjectDoesNotExist:
        return False
