import sys
import logging
import parsers

base_dir = "F:/dev/asciidoc/"
#logging.basicConfig(filename=base_dir+"adoc.log", level=logging.INFO)
logging.basicConfig(handlers=[logging.FileHandler(
    base_dir+"adoc.log", "a+", "utf-8")], level=logging.INFO)
logging.info("Start")
logger = logging.getLogger(__name__)
logger.info("START")

with open(sys.argv[1], "r", encoding="utf8") as f:
    logger.info("Init from: " + sys.argv[1])
    p = parsers.BaseParse()
    for line in f:
        p(line)

"""
with open(base_dir+"test.adoc", "w") as f:
    for i in sys.argv:
        f.write(i+"\n")
"""

