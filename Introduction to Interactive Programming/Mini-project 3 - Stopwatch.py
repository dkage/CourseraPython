# template for "Stopwatch: The Game"

import simplegui

# define global variables
interval = 1000
time = 0
position = [50, 50]

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format():
    global time
    hours = time / 3600
    timeleft = time - (hours * 3600)
    minutes = time / 60
    seconds = time % 60
    if hours < 10:
        hours = "0" + str(hours)
    if minutes < 10:
        minutes = "0" + str(minutes)
    if seconds < 10:
        seconds = "0" + str(seconds)
    watch = str(hours) + ":" + str(minutes) + ":" + str(seconds)
    return watch
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
def stop():
    timer.stop()
def reset():
    global time
    time = 0

# define event handler for timer with 0.1 sec interval
def stopwatch():
    global time
    time = time + 1

# define draw handler    
def draw (canvas):
    canvas.draw_text(format(), position, 36, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 500, 500)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, stopwatch)


# start frame

frame.start()
timer.start()
