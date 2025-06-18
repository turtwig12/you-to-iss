import requests
import math

def get_iss_location():
    response = requests.get("https://api.wheretheiss.at/v1/satellites/25544") #sends api call to get info on iss
    if response.status_code == 200: #checks if the request comes back
        data = response.json()
        iss_lat, iss_lng, altitude = data['latitude'], data['longitude'], data['altitude']
        return iss_lat, iss_lng, altitude
    else:
        return None

def get_my_location():
    response = requests.get("https://ipinfo.io/json") #sends api call to get info on your ip
    if response.status_code == 200: #checks if the request comes back
        data = response.json()
        my_lat, my_lon = map(float, data["loc"].split(","))
        return my_lat, my_lon
    else:
        return None

def get_distance(lat1, lon1, lat2, lon2, hight):

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Compute the central angle using spherical law of cosines
    theta = math.acos(
    math.sin(lat1) * math.sin(lat2) +
    math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)
    )

    # Compute the chord distance
    distance_below = 2 * 6371 * math.sin(theta / 2)

    distance_to_iss = (distance_below ** 2) + (hight ** 2)
    distance_to_iss = math.sqrt(distance_to_iss)
    return distance_to_iss

my_latitude, my_longitude = get_my_location() #gets your location
iss_latitude, iss_longitude, altitude = get_iss_location() #gets iss's location


print(f"my_Latitude: {my_latitude}")
print(f"my_Longitude: {my_longitude}")

print(f"iss_Latitude: {iss_latitude}")
print(f"iss_Longitude: {iss_longitude}")

print("")
distance_to_iss = get_distance(my_latitude, my_longitude, iss_latitude, iss_longitude,altitude)
print(f"distance_to_iss:{distance_to_iss}km")


