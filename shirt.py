import sys
from PIL import Image, ImageOps

try:
    extensions = (".png", ".jpg", ".jpeg")
    input = sys.argv[1]
    output = sys.argv[2]
    name, format1 = input.split(".")
    name, format2 = output.split(".")

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not input.endswith(extensions) or not output.endswith(extensions):
        sys.exit("Invalid output")
    if format1 != format2:
        sys.exit("Input and output have different extensions")

    before = Image.open(input)
    shirt = Image.open("shirt.png")
    size = shirt.size
    before_resized = ImageOps.fit(before, size)
    before_resized.paste(shirt, shirt)
    before_resized.save(output)

except FileNotFoundError:
    sys.exit("Input does not exist")
