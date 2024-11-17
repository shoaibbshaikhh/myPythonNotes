# module = a file containing python code. May contain functions, classes, etc.
# used with modular programming, which is to separate a program into parts
from sys import modules

import message as msg
msg.hello()
msg.bye()

# Output:
# Hello! Have a nice day!
# Bye! Have a wonderful time :)


from message import hello,bye
hello()
bye()

# Output:
# Hello! Have a nice day!
# Bye! Have a wonderful time :)

from message import *
hello()
bye()

# Output:
# Hello! Have a nice day!
# Bye! Have a wonderful time :)


help("modules")

# Output:
# output is so big plz run manually this command in your local machine