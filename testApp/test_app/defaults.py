# Copyright © 2018 Red Hat Inc.
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

"""Configuration."""

import logging
from urllib.parse import quote

from os import environ, path

logger = logging.getLogger(__name__)

SWAGGER_YAML_PATH = path.join(path.dirname(path.realpath(__file__)), 'swagger/swagger.yaml')
print("********************************************************")
print(SWAGGER_YAML_PATH)
class AppConfiguration(object):
    """Configuration."""
    
    def __init__(self):
        """Initiates the class.

        """

configuration = AppConfiguration()
