#!/usr/bin env python
# -*- coding: utf-8 -*-

import os
from time import sleep

from sklearn.datasets import make_classification
from kafka import KafkaProducer

from utils import msg_serializer, data_serializer

KAFKA_SERVER = os.environ.get("KAFKA_SERVER", "localhost:9092")

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER,
                         client_id="Data-set Producer",
                         value_serializer=msg_serializer)

while True:
    X, y = make_classification(n_samples=10, n_features=5, flip_y=.1)

    msg = {"X": data_serializer(X),
           "y": data_serializer(y)}

    producer.send("datasets", msg)
    sleep(2)
