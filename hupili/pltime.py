
def report_time(func):
    def report_time_wrapper(*al, **ad):
        start = time.time()
        ret = func(*al, **ad)
        end = time.time()
        logger.info("Function '%s' execution time: %.2f", func.__name__, end - start)
        return ret
    return report_time_wrapper

