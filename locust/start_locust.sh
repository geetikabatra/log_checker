#!/bin/bash

set -e

set -x

#Start Locust service
locust -f loc_script.py --host=http://schedule-server:5000/