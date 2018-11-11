import timeit


class Timer:
    def __init__(self):
        self.start_time = 0

    def getCurrentTime(self):
        return timeit.default_timer()

    def getStartTime(self):
        return self.start_time

    def startTimer(self):
        self.start_time = self.getCurrentTime()

    def stopTimer(self):
        return self.getCurrentTime() - self.getStartTime()

    @staticmethod
    def prettyPrintTime(time):
        """Converts a float to a pretty string of the time"""
        seconds = str(int(time))
        return seconds + ':{0:02.0f}:{1:02.0f}'.format(*divmod(time*1000000, 60))

    def timeFunction(self, function, *args):
        """
        Function to time the runtime of another function
        Call with TimeFunction(function_name, arg1, arg2, ...,argn)
        """
        start_time = timeit.default_timer()
        result = function(*args)
        return result, (timeit.default_timer() - start_time)