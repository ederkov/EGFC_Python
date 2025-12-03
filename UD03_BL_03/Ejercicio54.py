import time
h = m = s = 0
while True:
    print(f"{h:02}:{m:02}:{s:02}")
    time.sleep(1)
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
