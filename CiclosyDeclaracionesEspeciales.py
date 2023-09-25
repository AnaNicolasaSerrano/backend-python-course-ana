import time


def countdown(time_sec):
    """Temporizador"""
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = f'{mins:02d}:{secs:02d}'
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    print("stop")


def countup(time_sec):
    """Contador"""
    mins, secs, counter = 0, 0, 0
    while time_sec > counter:
        mins, secs = divmod(counter, 60)
        timeformat = f'{mins:02d}:{secs:02d}'
        print(timeformat, end='\r')
        time.sleep(1)
        counter += 1
    print("stop")


# countdown(90)
countup(90)
