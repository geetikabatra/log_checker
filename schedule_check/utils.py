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

"""Utils."""

from datetime import datetime


class Utils():
    """Contains utility function."""

    def process_date(self, date_):
        """Process date."""
        date_ = date_[1:-1]
        datetime_object = datetime.strptime(date_, '%d/%b/%Y %H:%M:%S')
        return datetime_object

    def break_info(self, line_):
        """Break information into a usable dictionary."""
        info_dict = dict()
        data_arr = line_.split()
        if len(data_arr) is 0:
            raise Exception("line is empty")
        info_dict["user"] = data_arr[2]
        datetime_ = self.process_date(data_arr[3] + " " + data_arr[4])
        info_dict["datetime_"] = datetime_
        info_dict["re_type"] = data_arr[6]
        info_dict["endpoint"] = data_arr[7]
        info_dict["status_code"] = data_arr[8]
        return info_dict
