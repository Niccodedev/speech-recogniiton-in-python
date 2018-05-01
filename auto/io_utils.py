import pyttsx3


class Logger:

    ALERT = '\033[31m'
    WARN = '\033[33m'
    INFO = '\033[34m'
    SUCCESS = '\033[36m'
    FOCUS = '\033[40m'
    ENDC = '\033[0m'

    def __init__(self, *args, **kwargs):
        self.say = True if kwargs.get('say') else False
        if self.say:
            self.engine = pyttsx3.init()
        pass

    def sayit(self, msg):
        if self.say:
            self.engine.say(msg)
            self.engine.runAndWait()

    def log(self, msg, **kwargs):
        self.sayit(msg)
        print(kwargs.get('color') + msg + self.ENDC)

    def alert(self, msg):
        self.log(msg, color=self.ALERT)

    def warn(self, msg):
        self.log(msg, color=self.WARN)

    def info(self, msg):
        self.log(msg, color=self.INFO)

    def success(self, msg):
        self.log(msg, color=self.SUCCESS)

    def focus(self, msg):
        self.log(msg, color=self.FOCUS)
