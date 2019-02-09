#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Geetika Batra <geetika791@gmail.com>
#

"""Class to define routes."""

import connexion
import flask
import defaults
import logging
from flask import request
from schedule_check import ScheduleJob
        
ScheduleJob.schedule_job()

def call_logger():
    logger = logging.getLogger('werkzeug')
    handler = logging.FileHandler('/tmp/access.log')
    #handler = logging.FileHandler('../../tmp/tempLog.log')
    logger.addHandler(handler)

def readiness():
    """Readiness probe."""
    return flask.jsonify({}), 200


def liveness():
    """Liveness probe."""
    return flask.jsonify({}), 200


def report():
    """Report Data."""
    """
    Generates report.
    """
    resp_dict = {
        "success": True,
        "summary": ""
    }
    if request.content_type != 'application/json':
        resp_dict["success"] = False
        resp_dict["summary"] = "Set content type to application/json"
        call_logger()
        return flask.jsonify(resp_dict), 400

    call_logger()
    return flask.jsonify(resp_dict), 200

def user_post():
    """User Data."""
    """
    Creates User.
    """
    resp_dict = {
        "success": True,
        "summary": ""
    }
    input_json = request.get_json()
    if request.content_type != 'application/json':
        resp_dict["success"] = False
        resp_dict["summary"] = "Set content type to application/json"
        call_logger()
        return flask.jsonify(resp_dict), 400

    call_logger()
    return flask.jsonify(resp_dict), 200


def user_get():
    """User Data."""
    """
    Get User.
    """
    resp_dict = {
        "success": True,
        "summary": ""
    }
    call_logger()
    return flask.jsonify(resp_dict), 200

def pages_create():
    """Pages Data."""
    """
    Create Page.
    """
    resp_dict = {
        "success": True,
        "summary": ""
    }
    input_json = request.get_json()
    if request.content_type != 'application/json':
        resp_dict["success"] = False
        resp_dict["summary"] = "Set content type to application/json"
        call_logger()
        return flask.jsonify(resp_dict), 400
    
    call_logger()
    return flask.jsonify(resp_dict), 200

app = connexion.FlaskApp(__name__)
app.add_api(defaults.SWAGGER_YAML_PATH)


if __name__ == "__main__":
    app.run()
