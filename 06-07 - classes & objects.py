class home:
    def __init__(self, c=0, f=0):
        self.color = c
        self.floor = f

    def getdata(self):
        print("{0}+{1}j".format(self.color, self.floor))

ali_home = home(15, 20)
ali_home.window = 20

ahmed_home = home(12, 21)

mohamed_home = home(21, 12)

ali_home.getdata()
ahmed_home.getdata()
mohamed_home.getdata()