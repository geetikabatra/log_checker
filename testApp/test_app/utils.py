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

"""Utility class."""

class LogInput():
    """Class to dump logs."""

    @classmethod
    def dumplog(name_):
        """Dump info into access log.

        :param name_: name_ of the sender
        :return: None
        """
        filename_ = '../tmp/tempLog.log'
        
        date_ = datetime.datetime.now()
        pivot_time = datetime.datetime.strptime(x, '%d/%b/%Y %H:%M:%S')
        
