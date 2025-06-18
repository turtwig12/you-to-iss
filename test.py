from PIL import Image

# Load the base image and the overlay image
Map_image = Image.open("World.png").convert("RGBA")
ISS_image = Image.open("ISS.png").convert("RGBA")

lat=0.0
lng=0.0

def find_iss_cords(lat, lng):
    x = 0.0
    y = 0.0

    if lng <= 0:
        x = (180 + lng)*10
    else:
        lng = -lng
        x = (180 - lng)*10

    if lng <= 0:
        y = (90 + lat)*10
    else:
        lat = -lat
        y = (90 - lat)*10

    x=int(x)
    y=int(y)
    return x, y

ISS_image = ISS_image.resize((100, 100))

x, y = find_iss_cords(lat, lng)

# Define the position where the overlay image will be placed
position = (x, y)

# Create a copy of the base image to avoid modifying the original
combined_image = Map_image.copy()

# Paste the overlay image onto the base image using its alpha channel for transparency
combined_image.paste(ISS_image, position, ISS_image)

# Save or display the result
combined_image.save("combined_image.png")
combined_image.show()

