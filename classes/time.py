class Time:
    def __init__(self, hours=0, minutes=0, seconds=0, milliseconds=0):
        if any(x < 0 for x in [hours, minutes, seconds, milliseconds]):
            raise ValueError("Параметры времени не могут быть отрицательными.")

        total_seconds = (hours * 3600) + (minutes * 60) + seconds + (milliseconds / 1000)
        total_seconds %= 86400  # секунд в сутках

        self.hours, remainder = divmod(total_seconds, 3600)
        self.minutes, remainder = divmod(remainder, 60)
        self.seconds, self.milliseconds = divmod(remainder * 1000, 1000)

    def GetHour(self):
        return int(self.hours)

    def GetMinute(self):
        return int(self.minutes)

    def GetSecond(self):
        return int(self.seconds)

    def GetMillisecond(self):
        return int(self.milliseconds)

    def Add(self, time):
        self.hours += time.hours
        self.minutes += time.minutes
        self.seconds += time.seconds
        self.milliseconds += time.milliseconds

        total_seconds = (self.hours * 3600) + (self.minutes * 60) + self.seconds + (self.milliseconds / 1000)
        total_seconds %= 86400  # секунд в сутках

        self.hours, remainder = divmod(total_seconds, 3600)
        self.minutes, remainder = divmod(remainder, 60)
        self.seconds, self.milliseconds = divmod(remainder * 1000, 1000)

    def __str__(self):
        return f'{int(self.hours):02d}:{int(self.minutes):02d}:{int(self.seconds):02d}.{int(self.milliseconds)}'


time = Time(25, 11, 12, 1)
print(str(time))
time.Add(Time(0, 0, 0, 1010))
print(str(time))
