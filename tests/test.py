import colourpick.clusterpick as cp
import os

print(cp.pick(r"{}\tests\green.jpg".format(os.getcwd()),2))