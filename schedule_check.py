from apscheduler.schedulers.blocking import BlockingScheduler
from utils import Utils
import datetime
import subprocess

class ScheduleJob():

    @classmethod
    def schedule_job(cls):
        def some_job():
            list_of_lines = list()  
            # filename_ = '/var/log/access.log'
            filename_ = 'tmp/tempLog.log'
            line_end = subprocess.check_output(['tail', '-1', filename_])
            begin_line = 2
            with open(filename_, 'r') as file:  # Use file to refer to the file object
                # line = subprocess.check_output(['tail', '-1', filename])
                i = begin_line
                for i, line in enumerate(file):
                    
                    if line == line_end:
                        list_of_lines.append(line)
                        break
                    list_of_lines.append(line)
            sec_data_dict = dict()
            count_per_sec = 0
            list_of_lines = list(map(lambda s: s.strip(), list_of_lines))
            list_of_lines = list(filter(None, list_of_lines))

            for line_ in list_of_lines:
                print(list_of_lines)
                print("******************************")
                print(line_)
                u_obj = Utils()
                info_dict = u_obj.break_info(line_)
                date_time = info_dict.get("datetime_", None)
                second_ = None
                if date_time is not None:
                    sec_data_dict[date_time] = list()
                    sec_data_dict[date_time].append(info_dict)
            x = "09/May/2018:16:00:39"
            pivot_time = datetime.datetime.strptime(x, '%d/%b/%Y:%H:%M:%S')   
            # ƒutilsivot_time = 39 9
            for k,v in info_dict.items():
               
                if len(k)>10:

                        with open(filename_, 'a') as file:  # Use file to refer to the file object

                            file.write('Hi there!')
            print("Decorated job")

        scheduler = BlockingScheduler()
        scheduler.add_job(some_job, 'interval', seconds=1)
        scheduler.start()

ScheduleJob.schedule_job()


['127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123\n', '\n', '127.0.0.1 - jill [09/May/2018:16:00:41 +0000] "GET /api/user HTTP/1.0" 200 234\n', '127.0.0.1 - frank [09/May/2018:16:00:42 +0000] "POST /api/user HTTP/1.0" 200 34\n', '127.0.0.1 - mary [09/May/2018:16:00:42 +0000] "POST /api/user HTTP/1.0" 503 12']