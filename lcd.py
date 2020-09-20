import ST7735
from PIL import Image, ImageDraw, ImageFont
from fonts.ttf import RobotoMedium as UserFont

# Create LCD class instance.
disp = ST7735.ST7735(
    port=0,
    cs=1,
    dc=9,
    backlight=12,
    rotation=270,
    spi_speed_hz=10000000
)

# Width and height to calculate text position.
WIDTH = disp.width
HEIGHT = disp.height

# New canvas to draw on.
img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
draw = ImageDraw.Draw(img)

# Text settings.
font_size = 25
font = ImageFont.truetype(UserFont, font_size)
text_colour = (0, 91, 178)
back_colour = (255, 255, 255)

message = "[QIoT Axians]"
size_x, size_y = draw.textsize(message, font)

# Calculate text position
x = (WIDTH - size_x) / 2
y = (HEIGHT / 2) - (size_y / 2)

def draw():
    # Initialize display.
    disp.begin()
    # Draw background rectangle and write text.
    draw.rectangle((0, 0, 160, 80), back_colour)
    draw.text((x, y), message, font=font, fill=text_colour)
    disp.display(img)


def draw_message(display_message):
    try: 
        disp.begin()
        draw.rectangle((0, 0, 160, 80), back_colour)
        draw.text((x, y), display_message, font=font, fill=text_colour)
        disp.display(img)
        return "Message {0} Display".format(message)
    except:
        return "Fail to post message"

def stop():
    disp.set_backlight(0)
