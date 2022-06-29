import unittest
from LogComponent import LogComponent
import threading


class TestLogging(unittest.TestCase):
    def setUp(self) -> None:
        self.log_component = LogComponent()
        self.filename = "LogTest.txt"

    def test_adding_log(self):
        # for i in range(3):
        self.log_component.add_logging(0, "1")
        self.log_component.add_logging(0, "2")
        self.log_component.add_logging(1, "3")

    def test_writing_log(self):
        self.log_component.add_logging(0, "1")
        self.log_component.add_logging(0, "2")
        self.log_component.add_logging(1, "3")
        self.log_component.write_logging()

    def test_stopping_log(self):
        def write_log():
            self.log_component.add_logging(0, "1")
            self.log_component.add_logging(0, "2")
            self.log_component.add_logging(0, "3")
            self.log_component.add_logging(0, "1")
            self.log_component.add_logging(0, "2")
            self.log_component.add_logging(0, "3")
            self.log_component.add_logging(0, "1")
            self.log_component.add_logging(0, "2")
            self.log_component.add_logging(0, "3")
            self.log_component.add_logging(0, "1")
            self.log_component.add_logging(0, "2")
            self.log_component.add_logging(0, "3")
            self.log_component.write_logging()

        def stop_log():
            self.log_component.stop_all_logging()

        t1 = threading.Thread(target=write_log())
        t2 = threading.Thread(target=stop_log())

        t1.start()
        t2.start()

    def tearDown(self) -> None:
        self.log_component = None
        # with open(self.filename, "w") as f:
        #     f.close()


if __name__ == "__main__":
    unittest.main()
