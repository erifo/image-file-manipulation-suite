import os
from glob import glob
from PIL import Image

def main():
    images = []
    scale = 0.5
    destination = "./resized/"
    names = glob("./*.jpg", recursive=True)
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    for name in names:
        print("Resizing:", name)
        head, tail = os.path.split(name)
        image = Image.open(name)
        new_width = int(image.width * scale)
        new_height = int(image.height * scale)
        new_image = image.resize((new_width, new_height))
        new_image.save(destination+tail)
    print("done")

if __name__ == "__main__":
    main()


