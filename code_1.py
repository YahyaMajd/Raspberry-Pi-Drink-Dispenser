# Group 4G
# Members: Amir Farah, Felix Ma, Rudy Ma, Yahya Abouelmagd
import time, sys, supervisor
#import serial.tools.list_ports
import board
import digitalio
import busio
import pwmio
import usb_cdc
import displayio
import terminalio
import adafruit_hcsr04
#from queue import Queue
from adafruit_display_text import label
from adafruit_st7789 import ST7789

import usb_cdc
if usb_cdc.data is None:
    print("Need to enable USB CDC serial data in boot.py!")



ONE_PART = 1
TWO_PARTS = 2
THREE_PARTS = 3
FOUR_PARTS = 4
FIVE_PARTS = 5
SIX_PARTS = 6



TOTAL_TIME = 10

#-----------------Declarations-----------------#
ledboard = digitalio.DigitalInOut(board.LED)
ledboard.direction = digitalio.Direction.OUTPUT

rum = digitalio.DigitalInOut(board.GP0)
rum.direction = digitalio.Direction.OUTPUT

vodka = digitalio.DigitalInOut(board.GP1)
vodka.direction = digitalio.Direction.OUTPUT

gin = digitalio.DigitalInOut(board.GP2)
gin.direction = digitalio.Direction.OUTPUT

coke = digitalio.DigitalInOut(board.GP3)
coke.direction = digitalio.Direction.OUTPUT

soda = digitalio.DigitalInOut(board.GP4)
soda.direction = digitalio.Direction.OUTPUT

mango = digitalio.DigitalInOut(board.GP5)
mango.direction = digitalio.Direction.OUTPUT

orange = digitalio.DigitalInOut(board.GP6)
orange.direction = digitalio.Direction.OUTPUT

grenadine = digitalio.DigitalInOut(board.GP7)
grenadine.direction = digitalio.Direction.OUTPUT

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP16, echo_pin=board.GP17)


#Our queue element, to add later
#q = Queue(0)

dispensing = False



def updateText(inputText):
    text_area.text = inputText.format(time.monotonic())


def clear():
    # Draws over screen with another rectangle
    inner_bitmap = displayio.Bitmap(
        display.width - BORDER * 2, display.height - BORDER * 2, 1
    )
    inner_palette = displayio.Palette(1)
    inner_palette[0] = FOREGROUND_COLOR
    inner_sprite = displayio.TileGrid(
        inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
    )
    splash.append(inner_sprite)



# -------------------------------------------------
# INSTANTIATING LCD (BASE FUNCTIONALITY)
# -------------------------------------------------

# First set some parameters used for shapes and text
BORDER = 20
FONTSCALE = 2
BACKGROUND_COLOR = 0x086788
FOREGROUND_COLOR = 0x06AED5
TEXT_COLOR = 0xF0C808

# Release any resources currently in use for the displays
displayio.release_displays()

tft_cs = board.GP9
tft_dc = board.GP8
spi_mosi = board.GP11
spi_clk = board.GP10
spi_reset = board.GP12
spi_bl = board.GP13
spi = busio.SPI(spi_clk, spi_mosi)

display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=spi_reset
)
display = ST7789(
    display_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53
)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = BACKGROUND_COLOR

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# -------------------------------------------------
# CODE FOR DISPLAYING ON LCD (BASE FUNCTIONALITY)
# -------------------------------------------------

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(
    display.width - BORDER * 2, display.height - BORDER * 2, 1
)
inner_palette = displayio.Palette(1)
inner_palette[0] = FOREGROUND_COLOR
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)

#Initialize a label
text = "At your \n service..."
text_area = label.Label(terminalio.FONT, text=text.format(time.monotonic()), color=TEXT_COLOR)
text_area.anchor_point = (0.5, 0)
text_area.anchored_position = (60, 25)
text_width = text_area.bounding_box[2] * FONTSCALE
text_group = displayio.Group(
    scale=FONTSCALE,
)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)

#text = "Hello World!"
#text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
#text_width = text_area.bounding_box[2] * FONTSCALE
#text_group = displayio.Group(
 #   scale=FONTSCALE,
  #  x=display.width // 2 - text_width // 2,
   # y=display.height // 2,
#)
#text_group.append(text_area)  # Subgroup for text scaling
#splash.append(text_group)




#-----------------Drinks-----------------#

def rum_and_coke():
    dispensing = True
    updateText("Dispensing : \n Rum and Coke !")
    rum.value = False
    time.sleep(1.5)
    rum.value = True
    time.sleep(0.5)
    coke.value = False
    time.sleep(6)
    coke.value = True
    updateText("At your \n service...")
    dispensing = False

def gin_and_tonic():
    dispensing = True
    updateText("Dispensing : \n Gin and Tonic")
    gin.value = False
    time.sleep(1.5)
    gin.value = True
  
    soda.value = False
    time.sleep(6)
    soda.value = True
    updateText("At your \n service...")
    dispensing = False

def mango_rum_fizz():
    dispensing = True
    updateText("Dispensing : \n Mango Rum Fizz")
    mango.value = False
    time.sleep(2.5)
    mango.value = True
  
    rum.value = False
    time.sleep(2.5)
    rum.value = True
    time.sleep(0.5)
    soda.value = False
    time.sleep(2.5)
    updateText("At your \n service...")
    soda.value = True

    dispensing = False
def orange_vodka_sunrise():
    dispensing = True
    updateText("Dispensing : \n Orange Vodka Sunrise")
    grenadine.value = False
    time.sleep(2)
    grenadine.value = True
 
    vodka.value = False
    time.sleep(2)
    vodka.value = True
    
    orange.value = False
    time.sleep(5)
    orange.value = True
    updateText("At your \n service...")
    dispensing = False
def Tequila_Sunrise():
    dispensing = True
    updateText("Dispensing : \n Tequila Sunrise")
    orange.value = False
    time.sleep(3)
    orange.value = True
  
    vodka.value = False
    time.sleep(2)
    vodka.value = True
    
    soda.value = False
    time.sleep(4)
    soda.value = True
    dispensing = False
    updateText("At your \n service")

while True:
    vodka.value = True
    mango.value = True
    rum.value = True
    gin.value = True
    soda.value = True
    grenadine.value = True
    orange.value = True
    coke.value = True
    #print(sonar.distance)
    try:
        if(sonar.distance <= 5):
            command = sys.stdin.readline()
            print(command)
            if "RUM_COKE" in command:
                rum_and_coke()
            elif "TEQUILA_SUNRISE" in command:
                Tequila_Sunrise()
            elif "MANGO_RUM" in command:
                mango_rum_fizz()
            elif "GIN_TONIC" in command:
                gin_and_tonic()
            elif "ORANGE_VODKA" in command:
                orange_vodka_sunrise()
    except RuntimeError:
        print("Retrying!")
    ledboard.value = True

    time.sleep(5)