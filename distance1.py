# https://www.it-swarm-fr.com/fr/python/obtenir-la-distance-entre-deux-points-en-fonction-de-la-latitude-longitude/1041560830/
# https://fr.acervolima.com/comment-obtenir-la-geolocalisation-en-python/


import mpu
d : int
# Point one
lat1 = 52.2296756
lon1 = 21.0122287

# Point two
lat2 = 52.406374
lon2 = 16.9251681

lat3 = 40
lon3 = -5

lat4 = 41 + 15/60 + 40.924579/3600
lon4 = -(3 + 18/60 + 44.877103/3600)


# What you were looking for
dist = mpu.haversine_distance((lat1, lon1), (lat2, lon2))
print(dist)  # gives 278.45817507541943.

dist1 = mpu.haversine_distance((lat3, lon3), (lat4, lon4))
print(dist1)  # gives 462.06693 km


# paris
lat_paris = 46.86
lon_paris = 2.34445

# marseille
lat_mars = 43.2976
lon_mars = 5.37639

dist2 = mpu.haversine_distance((lat_mars, lon_mars), (lat_paris, lon_paris))
print(dist2)  # gives 462.06693 km.
"""
import geopy.distance

coords_1 = (52.2296756, 21.0122287)
coords_2 = (52.406374, 16.9251681)

# print(geopy.distance.vincenty(coords_1, coords_2).km)
geopy.distance(coords_1, coords_2)
"""
from geopy.geocoders import Nominatim


geoLoc = Nominatim(user_agent="GetLoc")

locname = geoLoc.reverse("26.7674446, 81.109758")

print(locname.address)



geoLoc = Nominatim(user_agent="GetLoc")

locname = geoLoc.reverse("43.2976, 5.37639 ")

print(locname.address)

if __name__ == "__main__":
    pass