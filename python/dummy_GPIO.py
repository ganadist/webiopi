class GPIO:
    # defined in native/gpio.h
    GPIO_COUNT  = 54
    LOW         = 0
    HIGH        = 1
    IN          = 0
    OUT         = 1
    ALT0, ALT1, ALT2, ALT3 = range(4, 8)
    ALT4, ALT5  = range(3, 1, -1)
    PUD_OFF, PUD_DOWN, PUD_UP = range(3)
    BOARD_REVISION = 2
    def __init__(self):
        pass
    def setFunction(self, channel, direction, pull_up_down = PUD_OFF):
        pass
    def getFunction(channel, gpio):
        return 0
    def getFunctionString(self, gpio):
        FUNCTIONS = ("IN", "OUT", "ALT5", "ALT4", "ALT0", "ALT1", "ALT2", "ALT3")
        return FUNCTIONS[self.getFunction(gpio)]
    def output(self, channel, value):
        pass
    def outputSequence(self, channel, period, sequence):
        pass
    def input(self, channel):
        return True
