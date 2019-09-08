import sys
import logging
import InitParse
import Templates
from staticData import base_dir

# base_dir = "F:/dev/asciidoc/"
#logging.basicConfig(filename=base_dir+"adoc.log", level=logging.INFO)
logging.basicConfig(handlers=[logging.FileHandler(
    base_dir+"adoc.log", "a+", "utf-8")], level=logging.INFO)
logging.info("Start")
logger = logging.getLogger(__name__)
logger.info("START")

with open(sys.argv[1], "r", encoding="utf8") as f:
    logger.info("Init from: " + sys.argv[1])
    p = InitParse.InitParse()
    for line in f:
        p(line)
    p.create_filename()
"""
    with open(Templates.dTepmlates["template_name"], "r") as reader,
        open()

with open(base_dir+"test.adoc", "w") as f:
    for i in sys.argv:
        f.write(i+"\n")
"""

