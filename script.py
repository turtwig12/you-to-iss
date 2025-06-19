import requests
import math
import folium
import webbrowser
import os


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

def get_distance(lat1, lon1, lat2, lon2, height):

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

    distance_to_iss = (distance_below ** 2) + (height ** 2)
    distance_to_iss = math.sqrt(distance_to_iss)
    return distance_to_iss

def plot_map(lat1, lon1, lat2, lon2, distance_to_iss):
    location1 = (lat1, lon1)  # you
    location2 = (lat2, lon2)  # iss

    # Calculate the distance between the two points

    distance_text = f"Distance: {distance_to_iss:.2f} km"

    # Create a folium map centered between the two points
    midpoint = [(location1[0] + location2[0]) / 2, (location1[1] + location2[1]) / 2]
    m = folium.Map(location=midpoint, zoom_start=5)

    # adds markers to the map and gives them their names
    folium.Marker(location1, popup='you').add_to(m)
    folium.Marker(location2, popup='iss').add_to(m)

    # puts the line between the two points
    folium.PolyLine([location1, location2], color='blue', weight=2.5, opacity=1).add_to(m)

    # Add a popup at the midpoint with the distance
    folium.Marker(midpoint, popup=distance_text, icon=folium.Icon(color='green')).add_to(m)

    # Save and open the map in a browser
    map_path = 'map_with_distance.html'
    m.save(map_path)
    webbrowser.open('file://' + os.path.realpath(map_path))

my_latitude, my_longitude = get_my_location() #gets your location
iss_latitude, iss_longitude, altitude = get_iss_location() #gets iss's location

#incase issues locations and data are all printed, also helps with testing
print(f"my_Latitude: {my_latitude}")
print(f"my_Longitude: {my_longitude}")
print(f"iss_Latitude: {iss_latitude}")
print(f"iss_Longitude: {iss_longitude}")
print("")

distance_to_iss = get_distance(my_latitude, my_longitude, iss_latitude, iss_longitude,altitude) #calculates the distance you are from the iss, accounts for the height the iss is above the earths surface
print(f"distance_to_iss:{distance_to_iss}km")

plot_map(my_latitude, my_longitude, iss_latitude, iss_longitude, distance_to_iss)#makes the map and displays it on screen
