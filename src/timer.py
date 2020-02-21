import time
from datetime import datetime
from lamp import Lamp

# TURN_ON_FADE_IN  = { 'hour': 13, 'minute': 00 }
# TURN_ON_FULL     = { 'hour': 15, 'minute': 00 }
# TURN_ON_FADE_OUT = { 'hour': 22, 'minute': 00 }
# TURN_OFF         = { 'hour': 23, 'minute': 59 }
TURN_ON_FADE_IN  = { 'hour': 12, 'minute': 0 }
TURN_ON_FULL     = { 'hour': 14, 'minute': 0 }
TURN_ON_FADE_OUT = { 'hour': 22, 'minute': 0 }
TURN_OFF         = { 'hour': 23, 'minute': 59 }

lamp = Lamp()

def start_job():
    hour = 21
    minute = 50
    while True:
        now = datetime.now()

        # hour = int(now.strftime('%H'))
        # minute = int(now.strftime('%M'))
        print(hour, ":", minute)

        if should_turn_fade_in(hour, minute):
            intensity = 100 - int(time_diff({'hour': hour, 'minute': minute}, TURN_ON_FULL) * 100 / LENGTH_FADE_IN)
            print("clareando: ", intensity)
            lamp.turn_blue_to(intensity)
            lamp.turn_white_to(intensity)
            lamp.turn_red_to(intensity)

        elif should_turn_full_on(hour, minute):
            print("acesa")
            lamp.turn_blue_to(100)
            lamp.turn_white_to(100)
            lamp.turn_red_to(100)

        elif should_turn_fade_out(hour, minute):
            intensity = int(time_diff({'hour': hour, 'minute': minute}, TURN_OFF) * 100 / LENGTH_FADE_OUT)
            print("apagando: ", intensity)
            lamp.turn_blue_to(intensity)
            lamp.turn_white_to(intensity)
            lamp.turn_red_to(intensity)
        
        else:
            print("apagada")
            lamp.turn_blue_to(0)
            lamp.turn_white_to(0)
            lamp.turn_red_to(0)

        time.sleep(0.5)

        minute += 1
        if minute == 60:
            minute = 0
            hour += 1
            if hour == 24:
                hour = 0

def should_turn_fade_in(current_hour, current_minute):
    return current_hour * 60 + current_minute >= TURN_ON_FADE_IN['hour'] * 60 + TURN_ON_FADE_IN['minute'] and \
        current_hour * 60 + current_minute <= TURN_ON_FULL['hour'] * 60 + TURN_ON_FULL['minute']

def should_turn_full_on(current_hour, current_minute):
    return current_hour * 60 + current_minute >= TURN_ON_FULL['hour'] * 60 + TURN_ON_FULL['minute'] and \
        current_hour * 60 + current_minute <= TURN_ON_FADE_OUT['hour'] * 60 + TURN_ON_FADE_OUT['minute']

def should_turn_fade_out(current_hour, current_minute):
    return current_hour * 60 + current_minute >= TURN_ON_FADE_OUT['hour'] * 60 + TURN_ON_FADE_OUT['minute'] and \
        current_hour * 60 + current_minute <= TURN_OFF['hour'] * 60 + TURN_OFF['minute']

def time_diff(start, end):
    if start['hour'] > end['hour'] or start['hour'] == end['hour'] and start['minute'] > end['minute']:
        return (datetime(2020, 1, 2, end['hour'], end['minute'], 0) - \
            datetime(2020, 1, 1, start['hour'], start['minute'], 0)) \
                .total_seconds()
    else: 
        return (datetime(2020, 1, 1, end['hour'], end['minute'], 0) - \
            datetime(2020, 1, 1, start['hour'], start['minute'], 0)) \
                .total_seconds()     

    
LENGTH_FADE_IN = time_diff(TURN_ON_FADE_IN, TURN_ON_FULL)
LENGTH_FADE_OUT = time_diff(TURN_ON_FADE_OUT, TURN_OFF)

# print(time_diff(TURN_ON_FADE_IN, TURN_ON_FULL))
# print(time_diff(TURN_ON_FULL, TURN_ON_FADE_OUT))
# print(time_diff(TURN_ON_FADE_OUT, TURN_OFF))
# print(time_diff(TURN_OFF, TURN_ON_FADE_IN))
# print ('apagou')
start_job()