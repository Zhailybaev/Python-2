class Time():
    def __init__(self,s):
        self.s=s
    def convert_to_minutes(self):
        m=int(self.s/60)
        sec=self.s%60
        print('{}:{}'.format(m,sec))
    def convert_to_hours(self):
        h=int(self.s/3600)
        m=int((self.s%3600)/60)
        sec=(self.s%3600)%60
        print('{}:{}:{}'.format(h,m,sec))
s=int(input())
t=Time(s)
t.convert_to_minutes()
t.convert_to_hours()