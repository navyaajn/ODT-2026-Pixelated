from machine import Pin, PWM, time_pulse_us
import neopixel
import time
import math

# ================================================================
# CONFIGURATION
# ================================================================
ANIM_DURATION = 10
TEXT_DURATION = 15

# ================================================================
# BUTTONS
# ================================================================
btn_wave  = Pin(32, Pin.IN, Pin.PULL_UP)
btn_heart = Pin(33, Pin.IN, Pin.PULL_UP)
btn_stop  = Pin(26, Pin.IN, Pin.PULL_UP)
btn_rings = Pin(27, Pin.IN, Pin.PULL_UP)
btn_text  = Pin(14, Pin.IN, Pin.PULL_UP)

prev_wave  = 1
prev_heart = 1
prev_stop  = 1
prev_rings = 1
prev_text  = 1

# ================================================================
# SERVO
# ================================================================
servo = PWM(Pin(13))
servo.freq(50)

def set_angle(angle):
    duty = int(1638 + (angle / 180) * (8192 - 1638))
    servo.duty_u16(duty)

# ================================================================
# ULTRASONIC SENSOR
# ================================================================
trig = Pin(5, Pin.OUT)
echo = Pin(18, Pin.IN)

def get_distance():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    duration = time_pulse_us(echo, 1, 30000)
    if duration < 0:
        return None
    return (duration * 0.0343) / 2

# ================================================================
# NEOPIXELS
# ================================================================
NUM_LEDS = 60
channels = [
    neopixel.NeoPixel(Pin(23), NUM_LEDS),
    neopixel.NeoPixel(Pin(22), NUM_LEDS),
    neopixel.NeoPixel(Pin(21), NUM_LEDS),
    neopixel.NeoPixel(Pin(19), NUM_LEDS),
    neopixel.NeoPixel(Pin(25), NUM_LEDS),
]

def clear():
    for ch in channels:
        for i in range(NUM_LEDS):
            ch[i] = (0,0,0)

def write_all():
    for ch in channels:
        ch.write()

# ================================================================
# RADAR (FAST FADE + DUAL TRAIL)
# ================================================================
TRAIL_FADES = [1.0,0.9,0.75,0.6,0.45,0.32,0.2,0.12,0.06,0.03]
TRAIL_LEN = 10

BACK_TRAIL_LEN = 5
BACK_TRAIL_FADES = [0.45,0.30,0.18,0.08,0.03]

channel_intensity = [0.0]*5
FADE_STEP = 0.5

def get_active_channels(dist):
    if dist is None or dist > 100:
        return []
    elif dist > 60:
        return [2]
    elif dist > 30:
        return [1,2,3]
    else:
        return [0,1,2,3,4]

def update_intensity(active):
    for i in range(5):
        target = 1.0 if i in active else 0.0
        channel_intensity[i] += (target - channel_intensity[i]) * FADE_STEP

def get_color(led_index):
    ratio = led_index/(NUM_LEDS-1)
    if ratio < 0.33:
        t = ratio/0.33
        return (0,int(180*t),int(220-80*t))
    elif ratio < 0.66:
        t = (ratio-0.33)/0.33
        return (int(220*t),int(180-160*t),int(140+60*t))
    else:
        t = (ratio-0.66)/0.34
        return (220,int(20+130*t),int(200-200*t))

start = 35
end   = 155
delay = 0.06

def draw_radar(angle, forward, dist):
    clear()
    active = get_active_channels(dist)
    update_intensity(active)

    head = NUM_LEDS - 1 - int((angle - start)/2)
    head = max(0,min(NUM_LEDS-1,head))

    for ch_i,ch in enumerate(channels):
        scale = channel_intensity[ch_i]
        if scale <= 0.01:
            continue

        for t_i in range(TRAIL_LEN):
            idx = head + t_i if forward else head - t_i
            if 0 <= idx < NUM_LEDS:
                fade = TRAIL_FADES[t_i] * scale
                base = get_color(idx)
                ch[idx] = (
                    int(base[0]*fade),
                    int(base[1]*fade),
                    int(base[2]*fade)
                )

        for t_i in range(1, BACK_TRAIL_LEN+1):
            idx = head - t_i if forward else head + t_i
            if 0 <= idx < NUM_LEDS:
                fade = BACK_TRAIL_FADES[t_i-1] * scale
                base = get_color(idx)
                ch[idx] = (
                    int(base[0]*fade),
                    int(base[1]*fade),
                    int(base[2]*fade)
                )

    write_all()

# ================================================================
# WAVE
# ================================================================
def draw_wave(frame):
    clear()
    for ch_idx,ch in enumerate(channels):
        for led in range(NUM_LEDS):
            wave = math.sin((led + frame + ch_idx*8)*0.25)*0.5+0.5
            b = wave**2
            ch[led]=(0,int(180*b),int(255*b))
    write_all()

# ================================================================
# HEART
# ================================================================
pattern = [
"000000000111100011110000000000",
"000000001111111111111000000000",
"000000001111111111111000000000",
"000000000011111111100000000000",
"000000000000111110000000000000"
]

PL = len(pattern[0])
CENTER = PL//2

def get_color_phase(t):
    phase=(math.sin(t)*0.5+0.5)
    colors=[(255,60,120),(0,180,180),(255,140,0),(255,0,0),(255,60,120)]
    pos=phase*(len(colors)-1)
    i=int(pos)
    f=pos-i
    c1,c2=colors[i],colors[i+1]
    return (int(c1[0]+(c2[0]-c1[0])*f),
            int(c1[1]+(c2[1]-c1[1])*f),
            int(c1[2]+(c2[2]-c1[2])*f))

def apply_center_fade(color,idx):
    d=abs(idx-CENTER)
    f=1-(d/CENTER)
    return (int(color[0]*f),int(color[1]*f),int(color[2]*f))

def draw_heart(t):
    base=get_color_phase(t)
    for y,ch in enumerate(channels):
        row=pattern[y]
        for i in range(NUM_LEDS):
            p=int(i*PL/NUM_LEDS)
            ch[i]=apply_center_fade(base,p) if row[p]=='1' else (0,0,0)
        ch.write()

# ================================================================
# RINGS
# ================================================================
rings_buffer=[[(0,0,0) for _ in range(NUM_LEDS)] for _ in range(5)]

def draw_rings(frame):
    for y in range(5):
        for x in range(NUM_LEDS):
            r,g,b=rings_buffer[y][x]
            rings_buffer[y][x]=(int(r*0.65),int(g*0.65),int(b*0.65))

    for y in range(5):
        for x in range(NUM_LEDS):
            dx=x-NUM_LEDS//2
            dy=(y-2)*6
            d=math.sqrt(dx*dx+dy*dy)
            ph=(d/1.8)-frame*0.45
            if math.sin(ph)>0:
                v=math.sin(ph)**2
                col=(int(180*v*0.5),int(140*v*0.5),int(200*v*0.5))
                br,bg,bb=rings_buffer[y][x]
                rings_buffer[y][x]=(min(180,br+col[0]),min(180,bg+col[1]),min(180,bb+col[2]))

    for y,ch in enumerate(channels):
        for x in range(NUM_LEDS):
            ch[x]=rings_buffer[y][x]
        ch.write()

# ================================================================
# TEXT
# ================================================================
font = {
    "V":["10001","10001","10001","01010","00100"],
    "I":["11111","00100","00100","00100","11111"],
    "S":["01111","10000","01110","00001","11110"],
    "R":["11110","10001","11110","10100","10010"],
    "U":["10001","10001","10001","10001","01110"],
    "T":["11111","00100","00100","00100","00100"],
    "A":["01110","10001","11111","10001","10001"],
    "N":["10001","11001","10101","10011","10001"],
    "D":["11110","10001","10001","10001","11110"],
    "Y":["10001","01010","00100","00100","00100"],
    " ":["00000"]*5
}

TEXT="VISRUTA AND NAVYAA  "
text_pos=NUM_LEDS

def draw_text():
    global text_pos
    clear()
    x=text_pos
    for c in TEXT:
        pat=font.get(c)
        for y in range(5):
            for dx in range(5):
                if pat[y][dx]=="1":
                    px=x+dx
                    if 0<=px<NUM_LEDS:
                        channels[y][px]=(60,20,20)
        x+=8
    write_all()
    text_pos-=1
    if text_pos < -len(TEXT)*8:
        text_pos=NUM_LEDS

# ================================================================
# STATE
# ================================================================
mode="radar"
mode_end=0
angle=start
forward=True
frame=0
t=0

# ================================================================
# MAIN LOOP
# ================================================================
while True:

    v1,v2,v3,v4,v5 = btn_wave.value(),btn_heart.value(),btn_stop.value(),btn_rings.value(),btn_text.value()

    if v1==0 and prev_wave==1:
        mode="wave"; mode_end=time.time()+ANIM_DURATION

    if v2==0 and prev_heart==1:
        mode="heart"; mode_end=time.time()+ANIM_DURATION

    if v4==0 and prev_rings==1:
        mode="rings"; mode_end=time.time()+ANIM_DURATION

    if v5==0 and prev_text==1:
        mode="text"; mode_end=time.time()+TEXT_DURATION

    if v3==0 and prev_stop==1:
        mode="radar"

    prev_wave,prev_heart,prev_stop,prev_rings,prev_text=v1,v2,v3,v4,v5

    if mode!="radar" and time.time()>mode_end:
        mode="radar"

    if mode=="radar":
        set_angle(angle)
        dist=get_distance()
        draw_radar(angle,forward,dist)

        if forward:
            angle+=2
            if angle>=end: forward=False
        else:
            angle-=2
            if angle<=start: forward=True

        time.sleep(delay)

    elif mode=="wave":
        draw_wave(frame); frame+=1; time.sleep(0.03)

    elif mode=="heart":
        draw_heart(t); t+=0.08; time.sleep(0.03)

    elif mode=="rings":
        draw_rings(frame); frame+=1; time.sleep(0.02)

    elif mode=="text":
        draw_text(); time.sleep(0.035)