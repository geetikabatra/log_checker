#!/bin/bash

set -e

set -x

#Start Locust service
locust loc_scripy.py --host=schedule_checker:5000