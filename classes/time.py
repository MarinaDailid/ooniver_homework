class Time:
    seconds: int

    def __init__(self, seconds, minutes, hours):
        self.seconds = hours * 60 * 60 + minutes * 60 + seconds

    def print(self):
        hours = self.seconds // 3600
        minutes = self.seconds % 3600 // 60
        seconds = self.seconds - hours * 3600 - minutes * 60
        print(f'{hours} : {minutes} : {seconds}')

    def sum_time(self, time):
        self.seconds += time.seconds
    def diff_time(self, time):
        self.seconds -= time.seconds

    def comp_time(self, time):
        if self.seconds > time.seconds:
            print('больше')
        elif self.seconds == time.seconds:
            print('равно')
        else:
            print('меньше')

time = Time(3, 69 , 1)
time1 = Time(30, 67, 2)
time.sum_time(time1)
time.print()
time.diff_time(time1)
time.print()
time.comp_time(time1)
time.print()

