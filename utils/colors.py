from colored import fore, back, style, fg, bg, attr, stylize

class Colors:
    def __init__(self) -> None:
        self.animation = "🕸🕷"
        self.reset = attr('reset')
        self.light_grey = fg('light_gray')
        self.dark_grey = fg('dark_gray')
        self.red = fg('red')
        self.green = fg('green')
        self.bold = attr('bold')
        self.white = fg('white')
        self.magenta = fg('magenta')
        self.yellow = fg('yellow')
        self.blue = fg('blue')
        self.purple = fg('purple_4a')
        self.pink = fg('pink_3')
        self.cyan = fg('cyan')
        self.purple_3 = fg('purple_3')

    