#!/bin/bash

set -e

set -x

#Start Locust service

nohup python3 testApp/rest_api.py &
python3 schedule_check.py
