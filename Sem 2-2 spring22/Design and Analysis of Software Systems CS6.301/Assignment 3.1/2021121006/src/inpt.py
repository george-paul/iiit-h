# """Defining input class."""
# import sys
# import termios
# import tty
# import signal

# class Get:
#     """Class to get input."""

#     def __call__(self):
#         """Defining __call__."""
#         fd = sys.stdin.fileno()
#         old_settings = termios.tcgetattr(fd)
#         try:
#             tty.setraw(sys.stdin.fileno())
#             ch = sys.stdin.read(1)
#         finally:
#             termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#         return ch


# class AlarmException(Exception):
#     """Handling alarm exception."""
#     pass


# def alarmHandler(signum, frame):
#     """Handling timeouts."""
#     raise AlarmException


# def input_to(getch, timeout=0.1):
#     """Taking input from user."""
#     signal.signal(signal.SIGALRM, alarmHandler)
#     signal.setitimer(signal.ITIMER_REAL, timeout)
#     try:
#         text = getch()
#         signal.alarm(0)
#         return text
#     except AlarmException:
#         signal.signal(signal.SIGALRM, signal.SIG_IGN)
#         return None

# import msvcrt

# def input_to():
# 	if msvcrt.kbhit():
# 		key = msvcrt.getch()
# 		return key



# cross-platform using pynput
# pip install pynput 

from pynput import keyboard

def on_activate_h():
    print('w pressed')

def on_activate_i():
    print('<ctrl>+<alt>+i pressed')

with keyboard.GlobalHotKeys({
        'w': on_activate_h,
        's': on_activate_i}) as h:
    h.join()