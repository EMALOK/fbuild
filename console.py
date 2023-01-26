
log_level = 0

debug_color = "\x1b[38;5;15m"
log_color = "\x1b[38;5;226m"
success_color = "\x1b[38;5;40m"
warning_color = "\x1b[38;2;255;105;0m"
error_color = "\x1b[38;5;9m"
abort_color = "\x1b[37;41m"

reset_color = "\x1b[0m"

def reset():
    print(reset_color)

# log-level: debug
def debug(message):
    print(debug_color,end='')
    print(message,end='')
    reset()

# log-level: high
def log(message):
    print(log_color,end='')
    print(message,end='')
    reset()

def success(message):
    print(success_color,end='')
    print(message,end='')
    reset()

# log-level: medium
def warning(message):
    print(warning_color,end='')
    print("[WARNING]",message,end='')
    reset()

# log-level: low
def error(message):
    print(error_color,end='')
    print("[ERROR]",message,end='')
    reset()

# log-level: always
def abort(message,quit_exec = True):
    print(abort_color,end='')
    print("[ABORT]",message,end='')
    reset()
    if quit_exec:
        quit(-1)