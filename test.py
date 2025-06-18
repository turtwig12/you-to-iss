from PIL import Image

ISS_lat=0
ISS_lng=0
your_lat=80
your_lng=0


def display_map(ISS_lat, ISS_lng, your_lat, your_lng):
    Map_image = Image.open("World.png").convert("RGBA")
    ISS_image = Image.open("ISS.png").convert("RGBA")
    your_image = Image.open("stickman.png").convert("RGBA")

    if ISS_lng <= 0:
        ISS_x = (180 + ISS_lng)*10
    else:
        ISS_lng = -ISS_lng
        ISS_x = (180 - ISS_lng)*10

    if ISS_lng <= 0:
        ISS_y = (90 + ISS_lat)*10
    else:
        ISS_lat = -ISS_lat
        ISS_y = (90 - ISS_lat)*10

    ISS_x=int(ISS_x)
    ISS_y=int(ISS_y)


    if your_lng <= 0:
        your_x = (180 + your_lng)*10
    else:
        your_lng = -your_lng
        your_x = (180 - your_lng)*10

    if your_lng <= 0:
        your_y = (90 + your_lat)*10
    else:
        your_lat = -your_lat
        your_y = (90 - your_lat)*10

    your_x=int(your_x)
    your_y=int(your_y)


    ISS_image = ISS_image.resize((100, 100))
    your_image = your_image.resize((50, 50))

    combined_image = Map_image.copy()

    combined_image.paste(ISS_image, (ISS_x, ISS_y), ISS_image)

    combined_image.paste(your_image, (your_x, your_y), your_image)

    combined_image.show()

display_map(ISS_lat, ISS_lng, your_lat, your_lng)



