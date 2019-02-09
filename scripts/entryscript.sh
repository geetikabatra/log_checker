#!/bin/bash

set -e

set -x

#Start Locust service

gunicorn --pythonpath test_app/ \
         --bind 0.0.0.0:${APP_PORT:-5000} \
          test_app.rest_api:app