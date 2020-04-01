from shutil import get_terminal_size
from Story_Node import Story_Node



class Text_Format:
    reset      = '\033[0m'
    bold       = '\033[01m'
    dim        = '\033[02m'
    italic     = '\033[03m'
    underline  = '\033[04m'
    slow_blink = '\033[05m'
    fast_blink = '\033[06m'
    invert     = '\033[07m'
    strike     = '\022[09m'

    class font:
        black      = '\033[30m'
        red        = '\033[31m'
        green      = '\033[32m'
        yellow     = '\033[33m'
        blue       = '\033[34m'
        magenta    = '\033[35m'
        cyan       = '\033[36m'
        white      = '\033[37m'
        bright_red = '\033[91m'
        lightgreen = '\033[92m'
        lightblue  = '\033[94m'

    class bg:
        black      = '\033[40m'
        red        = '\033[41m'
        green      = '\033[42m'
        yellow     = '\033[43m'
        blue       = '\033[44m'
        magenta    = '\033[45m'
        cyan       = '\033[46m'
        white      = '\033[47m'
        bright_red = '\033[101m'
        lightgreen = '\033[102m'
        lightblue  = '\033[104m'

    def __init__(self):
        pass

    def _fprint(self, s, fg, bg, effect, reset):
        string = ""
        if bg: string += bg
        if fg: string += fg
        if effect: string += effect
        string += s
        if reset: string += Text_Format.reset
        print(string)

    def _line_fill(self, lefthand, center, righthand):
        width = get_terminal_size()[0]
        l_size = len(lefthand)
        r_size = len(righthand)
        c_size = len(center)
        lr_max = max(l_size, r_size)
        if lr_max*2 + c_size > width:
            return "Error: components wider than line"
        string = lefthand
        if l_size < lr_max: string += ' '*(lr_max-l_size)
        c_pad = (width - (lr_max*2 + c_size))//2
        string += ' '*c_pad + center + ' '*c_pad
        if r_size < lr_max: string += ' '*(lr_max-r_size)
        string += righthand
        return string

    def __call__(self, s, fg=None, bg=None, effect=None,
                 reset=True):
        string = s
        self._fprint(string, fg, bg, effect, reset)

header_txt_color = Text_Format.font.red
header_bg = Text_Format.bg.white
cursor = Text_Format()
def header(room, middle="", end="", c=cursor):
    head = c._line_fill(room.name, middle, end)
    c(head, fg=header_txt_color, bg=header_bg)

game = True
        

if __name__ == '__main__':
    test_node = Story_Node("The Great Hall","A Big Hall")
    while game:
        header(test_node)
        inp = input()
        if inp == "quit": game = False
