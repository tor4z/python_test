import time
import sys

"""
toolbar_width = 40

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(toolbar_width):
    time.sleep(0.01) # do real work here
    # update the bar
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("\n")
"""

"""
Loading
"""
def bar():
    for x in range (0,30):  
        b = "Loading {0}".format("." * x)
        print (b, end="\r")
        time.sleep(0.01)
        
bar()