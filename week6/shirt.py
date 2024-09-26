import sys
from PIL import Image, ImageOps

shirt = Image.open('shirt.png')

if len(sys.argv) > 3 :
    sys.exit('Too many command-line arguments')

elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')

else:
    name1, extension1 = sys.argv[1].split('.')
    name2, extension2 = sys.argv[2].split('.')
    if extension1.lower() != 'jpg' and extension1.lower() != 'jpeg' and extension1.lower() != 'png' and extension2.lower() != 'jpg' and extension2.lower() != 'jpeg' and extension2.lower() != 'png':
        sys.exit('Invalid input')

    elif extension1 != extension2:
        sys.exit('Input and output have different extensions')
    
    else:
        try:
            background = Image.open(sys.argv[1])
            background = ImageOps.fit(image = background, size = (600, 600))
            background.paste(shirt, shirt)
            after = background.save(sys.argv[2])

        except FileNotFoundError:
            sys.exit('File does not exist')
        