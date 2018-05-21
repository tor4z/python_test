import traceback


class A:
    def __init__(self):
        pass

    def tb(self):
        es = traceback.extract_stack()
        print(es)
        fs = es[-2]
        print(fs.name)
        print(fs.locals)

def another_function():
    lumberstack(A())
    lumberstack(A())


def lumberstack(a):
    a.tb()

another_function()

"""
[<FrameSummary file traceback_test.py, line 23 in <module>>,
<FrameSummary file traceback_test.py, line 16 in another_function>,
<FrameSummary file traceback_test.py, line 21 in lumberstack>,
<FrameSummary file traceback_test.py, line 9 in tb>]
lumberstack
None

[<FrameSummary file traceback_test.py, line 23 in <module>>,
<FrameSummary file traceback_test.py, line 17 in another_function>,
<FrameSummary file traceback_test.py, line 21 in lumberstack>,
<FrameSummary file traceback_test.py, line 9 in tb>]
lumberstack
None
"""