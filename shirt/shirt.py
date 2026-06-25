import sys
from PIL import Image, ImageOps

def main():
    shirt()

def shirt():
    try:
        if len(sys.argv) < 3:
            print("Too few command-line arguments")
            sys.exit(1)
        if len(sys.argv) > 3:
            print("Too many command-line arguments")
            sys.exit(1)

        extension1=sys.argv[1].split(".")
        extension2=sys.argv[2].split(".")
        if (extension1[1] not in ["jpg","jpeg","png"] or extension2[1] not in ["jpg","jpeg","png"]):
            print("Invalid output")
            sys.exit(1)
        if not extension1[1] == extension2[1]:
            print("Input and Output have different extensions") 
            sys.exit(1)

        input_image = Image.open(sys.argv[1]) #opens before.jpg  image
    except FileNotFoundError:
        print("Input does not exist")
        sys.exit(1)
        

    shirt_image = Image.open("shirt.png") #opens shirt.png
    resized_image = ImageOps.fit(input_image, shirt_image.size) # resizes before image for mask image
    resized_image.paste(shirt_image, mask = shirt_image) # pastes mask image onto before image
    resized_image.save(sys.argv[2]) # resized imaged is now masked with shirt, so we save it to a new image

if __name__ == "__main__":
    main()