import datetime
import logging
from staticData import base_dir, dTepmlates, cons_output

dTepmlates = {"//ох": "template/ox.adoc"}
logger = logging.getLogger(__name__)


class InitParse:
    def __init__(self):
        self.reader = ""
        self.writer = ""
        self.line_number = 0
        self.data = {}
        self.sdata = []

    def __call__(self, line_data):
        line_data = line_data.rstrip()
        self.line_number += 1
        if 1 == self.line_number:
            self.data["template_name"] = line_data
            return
        if 2 == self.line_number:
            self.data["fio"] = line_data
            return
        if 3 == self.line_number:
            self.data["bday"] = datetime.datetime.strptime(line_data, "%d%m%Y")
            return
        d = line_data.split("=", 1)
        if len(d) == 1:
            self.sdata.append(d[0])
        if len(d) == 2:
            self.data[d[0]] = d[1]

    def create_filename(self):
        self.reader = base_dir+dTepmlates[self.data["template_name"]]
        time_str = datetime.date.today().strftime("%Y%m%d")
        name_str = self.data["fio"].split()[0]
        self.writer = base_dir+cons_output+time_str+name_str


    def __del__(self):
        logger.info("Replacements: ")
        logger.info(self.data)
        logger.info(self.data["fio"])
        logger.info("Static data: ")
        logger.info(self.sdata)
        logger.info("Reader: " + self.reader)
        logger.info("Writer: " + self.writer)




