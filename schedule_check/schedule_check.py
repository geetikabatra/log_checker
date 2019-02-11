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
"""Schedules Job."""

from apscheduler.schedulers.blocking import BlockingScheduler
from utils import Utils
import datetime
import subprocess
import os


class ScheduleJob():
    """Contains Schedule Job."""

    @classmethod
    def schedule_job(cls):
        """Class method to schedule a cron job."""
        def watch_job():
            """Inner function to create a watch job."""
            list_of_lines = list()
            filename_ = '/var/log/access.log'
            # filename_ = '../tmp/tempLog.log'
            line_end = subprocess.check_output(['wc', '-l', filename_])
            line_end = int(line_end[:2])
            begin_line = int(os.environ.get("LAST_LINE_PROCESSED", 0))
            if begin_line != line_end:
                with open(filename_, 'r') as file:  # Use file to refer to the file object
                    # line = subprocess.check_output(['tail', '-1', filename])
                    i = begin_line

                    for i, line in enumerate(file):
                        if i == line_end:
                            print("Reaxhed here")

                            list_of_lines.append(line)

                            break
                        list_of_lines.append(line)
                sec_data_dict = dict()
                count_per_sec = 0
                list_of_lines = list(map(lambda s: s.strip(), list_of_lines))
                list_of_lines = list(filter(None, list_of_lines))
                for line_ in list_of_lines:
                    u_obj = Utils()
                    if line_.startswith("High traffic"):
                        continue
                    info_dict = u_obj.break_info(line_)
                    date_time = info_dict.get("datetime_", None)
                    second_ = None
                    if date_time is not None:
                        if sec_data_dict.get(date_time, None) is None:
                            sec_data_dict[date_time] = list()
                        sec_data_dict[date_time].append(info_dict)
                for k, v in sec_data_dict.items():
                    if len(v) > 10:
                        # Use file to refer to the file object
                        with open(filename_, 'a') as file:
                            file.write("\n")
                            file.write(
                                "High traffic generated an alert - hits = {0}, triggered at {1}".format(len(v), k))
                            # i+1 because now last line because now extra line
                            # will be added
                            os.environ['LAST_LINE_PROCESSED'] = str(
                                line_end + 1)
                    else:
                        os.environ['LAST_LINE_PROCESSED'] = str(line_end)

        scheduler = BlockingScheduler()
        scheduler.add_job(watch_job, 'interval', seconds=10)
        scheduler.start()


ScheduleJob.schedule_job()
