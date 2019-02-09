from datetime import datetime

class Utils():
    
    def process_date(self, date_):
        
        date_ = date_[1:-1]
        datetime_object = datetime.strptime(date_, '%d/%b/%Y %H:%M:%S')
        return datetime_object
        
    def break_info(self, line_):
        info_dict = dict()
        data_arr = line_.split()
        if len(data_arr) is 0:
            raise Exception("line is empty")
        info_dict["user"] = data_arr[2]
        datetime_ = self.process_date(data_arr[3]+ " " + data_arr[4] )
        info_dict["datetime_"] = datetime_
        info_dict["re_type"] = data_arr[6]
        info_dict["endpoint"] = data_arr[7]
        info_dict["status_code"] =data_arr[8]
        return info_dict

    