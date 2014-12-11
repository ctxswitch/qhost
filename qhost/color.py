class Color:
    RED = 0
    GREEN = 1
    GRAY = 2
    BLUE = 3
    TEAL = 4
    RESET = 5

    @staticmethod
    def message(msg, color):
        if color == Color.RED:
            return "\033[31m%s\033[0m" % (msg)
        elif color == Color.GREEN:
            return "\033[1;32m%s\033[0m" % (msg)
        elif color == Color.GRAY:
            return "\033[1;30m%s\033[0m" % (msg)
        elif color == Color.BLUE:
            return "\033[1;34m%s\033[0m" % (msg)
        elif color == Color.TEAL:
            return "\033[36m%s\033[0m" % (msg)
        return msg

    @staticmethod
    def ratio(value, maxval):
        # Get the percentage and return the string with the
        # appropriate color
        msg = ""
        p = float(value) / float(maxval)
        if p >= 1.0:
            msg = Color.message(value, Color.RED)
        elif p >= 0.75 and p < 1.0:
            msg = Color.message(value, Color.RED)
        elif p >= 0.50 and p < 0.75:
            msg = Color.message(value, Color.GREEN)
        elif p >= 0.25 and p < 0.50:
            msg = Color.message(value, Color.GREEN)
        else:
            msg = Color.message(value, Color.BLUE)
        return msg
