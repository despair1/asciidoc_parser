# dParsers = {"//ох": [ParseRef, "template/ox.adoc"]}
import datetime
import logging

logger = logging.getLogger(__name__)


class BaseParse:
    def __init__(self):
        self.line_number = 0
        self.data = {}
        self.sdata = []

    def __call__(self, line_data):
        line_data = line_data.rstrip()
        self.line_number += 1
        if 1 == self.line_number:
            self.data["template_path"] = line_data
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

    def __del__(self):
        logger.info("Replacements: ")
        logger.info(self.data)
        logger.info(self.data["fio"])
        logger.info("Static data: ")
        logger.info(self.sdata)




