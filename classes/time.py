class Time:
    seconds: int
    minutes: int
    hours: float

    def __init__(self, seconds, minutes, hours):
        all_seconds = hours * 3600 + minutes * 60 + seconds
        self.hours = all_seconds // 3600
        self.minutes = all_seconds % 3600 // 60
        self.seconds = all_seconds - self.hours * 3600 - self.minutes * 60

    def sum_time(self):
        pass
    def diff_time(self):
        pass

    def comp_time(self):
        pass

time = Time(1, 67, 66)
print(time.sum_time())



