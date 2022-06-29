from collections import deque
import time


class LogComponent:
    def __init__(self):
        self.last_day = time.localtime().tm_mday
        self.last_timestamp = time.time()
        self.filename = "LogTest"
        self.normal_queue = deque([])
        self.outstanding_queue = deque([])
        self.all_stop = False
        self.normal_stop = False

    def write_logging(self):
        try:
            my_filename = self.filename + str(self.last_timestamp) + ".txt"
            with open(my_filename, "a") as f:
                while not self.all_stop and self.outstanding_queue:
                    if not self.check_cross_night():
                        f.write(self.outstanding_queue.popleft())

                    else:
                        self.last_timestamp = time.time()
                        self.last_day = time.localtime().tm_mday
                        self.write_logging()

                while not self.all_stop and not self.normal_stop and self.normal_queue:
                    f.write(self.normal_queue.popleft())
        except:
            print("Error comes from LogComponent write logging Error")

    def add_logging(self, priority, message):
        try:
            if priority > 0:
                self.outstanding_queue.append(message)
            else:
                self.normal_queue.append(message)
        except:
            print("Error comes from LogComponent add logging Error")

    def stop_all_logging(self):
        self.all_stop = True

    def stop_normal_logging(self):
        self.normal_stop = True

    def check_cross_night(self):
        if self.last_day != time.localtime().tm_mday:
            return True
        else:
            return False
