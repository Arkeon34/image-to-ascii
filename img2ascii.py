import argparse
from PIL import Image
ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('-in', '--image_path', type=str)
parser.add_argument('-out', '--output_path', type=str)
args = parser.parse_args()


# Resize Image Function
def resize(image, new_width=35):
    width, height = image.size
    new_height = new_width * height // width
    return image.resize((int(new_width * 2.7), new_height))


img = Image.open(args.image_path).convert('L')
img = resize(img)
ascii_str = ""
for data in img.getdata():
    # Division by 24 because [0; 255] / 24 = ASCII_CHARS[0; -1]
    ascii_str += ASCII_CHARS[data//24]

ascii_str_len = len(ascii_str)
ascii_img = ''

for i in range(0, ascii_str_len, img.width):
    ascii_img += ascii_str[i:i+img.width] + "\n"

with open(args.output_path, "w") as f:
    f.write(ascii_img)
