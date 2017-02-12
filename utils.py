#!/usr/bin env python
# -*- coding: utf-8 -*-

import json
from io import StringIO

import pandas as pd


def msg_deserializer(msg):
    try:
        decoded_msg = json.loads(msg.decode('utf-8'))
    except Exception as e:
        print(repr(e))
    else:
        return decoded_msg


def msg_serializer(msg):
    try:
        encoded_msg = bytes(json.dumps(msg), 'utf-8')
    except Exception as e:
        print(repr(e))
    else:
        return encoded_msg


def data_serializer(X):
    return pd.DataFrame(X).to_string()


def data_deserializer(X_str):
    return pd.read_csv(StringIO(X_str), sep="\s+")
