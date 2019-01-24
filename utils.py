from datetime import datetime

class Utils():
    
    def process_date(self, date_):
        date_ = date_[1:]
        print(date_)
        datetime_object = datetime.strptime(date_, '%d/%b/%Y:%H:%M:%S')
        return datetime_object
        
    def break_info(self, line_):
    #     ['127.0.0.1',
    #  '-',
    #  'james',
    #  '[09/May/2018:16:00:39',
    #  '+0000]',
    #  '"GET',
    #  '/report',
    #  'HTTP/1.0"',
    #  '200',
    #  '123']
        info_dict = dict()
        data_arr = line_.split()
        if len(data_arr) is 0:
            raise Exception("line is empty")
        print(data_arr)
        info_dict["user"] = data_arr[2]
        datetime_ = self.process_date(data_arr[3])
        info_dict["datetime_"] = datetime_
        info_dict["re_type"] = data_arr[5]
        info_dict["endpoint"] = data_arr[6]
        info_dict["status_code"] =data_arr[7]
        return info_dict




    