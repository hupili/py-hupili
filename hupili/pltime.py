import time
import sys

def report_time(func):
    def report_time_wrapper(*al, **ad):
        start = time.time()
        ret = func(*al, **ad)
        end = time.time()
        sys.stderr.write("Function '%s' execution time: %.2f\n" % (func.__name__, end - start))
        return ret
    return report_time_wrapper

if __name__ == '__main__':
    def testfunc():
        print "in test func"
        time.sleep(1)

    testfunc()
    testfunc = report_time(testfunc)
    testfunc()
