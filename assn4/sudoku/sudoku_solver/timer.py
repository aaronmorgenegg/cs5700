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

    def timeFunction(self, function, *args):
        """
        Function to time the runtime of another function
        Call with TimeFunction(function_name, arg1, arg2, ...,argn)
        """
        start_time = timeit.default_timer()
        function(*args)
        return timeit.default_timer() - start_time