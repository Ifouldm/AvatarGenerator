import os
import random
from typing import List

from PIL import Image, ImageDraw, ImageFont

extensions: [str] = ['.jpg', '.png', '.jpeg', '.gif']
limit: int = 100


def create_avatars(users: List[str]):
    if len(users) > limit:
        print("User limit exceeded")
        return
    for name in users:
        filename: str = 'avatars/' + name + '.png'
        displayname: str = name
        random.seed(name)
        hue = random.randint(0, 360)
        bg = 'hsl(%d, 50%%, 70%%)' % hue
        fg = 'hsl(%d, 50%%, 80%%)' % hue
        fontsize: int = 80
        if len(name) > 8:
            fontsize = 60
            if len(name) > 14:
                displayname = name[0:10] + '...'

        if not os.path.exists(filename):
            print(filename)
            font = ImageFont.truetype('resources/Amatic-Bold.ttf', size=fontsize)
            with blank_avatar(bg, fg) as image:
                draw = ImageDraw.Draw(image)
                text_width = font.getsize(displayname)[0]
                text_height = font.getsize(displayname)[1]
                x: float = ((image.width / 2) - (text_width / 2))
                y: int = image.height - text_height - 10
                draw.text((x, y), displayname, font=font)
                image.save(filename, 'PNG')
                image.close()


def blank_avatar(bgcolor: int, fcolor: int) -> Image:
    avatar_image = Image.new('RGB', (256, 256), color=bgcolor)
    draw_blank = ImageDraw.Draw(avatar_image)
    draw_blank.ellipse([(69, 46), (182, 159)], fill=fcolor)
    draw_blank.ellipse([(25, 147), (223, 430)], fill=fcolor)
    return avatar_image
