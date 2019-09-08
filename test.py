import sys
import time



base_dir = "F:/dev/asciidoc/"
with open(base_dir+"test.adoc", "w") as f:
    for i in sys.argv:
        f.write(i+"\n")


