import math

#Convert degrees/minutes/seconds (Lat and Long on Google Earth) to decimal degrees

def DMS_DecDeg(geoDeg, geoMin, geoSec):
    total = geoDeg + (geoMin/60) + (geoSec/3600)
    return(total)


def DMS_Vector(lat1, long1, lat2, long2):
    xstart = lat1 * (40000/260) * 3280.4
    xstop = lat2 * (40000/260) * 3280.4
    ystart = long1 * (40000/260) * 3280.4
    ystop =  long2 * (40000/260) * 3280.4

    x_vector = xstop - xstart
    y_vector = ystop - ystart

    length = math.sqrt(x_vector**2 + y_vector**2)
    angle = math.atan(y_vector/x_vector)

    return(print('Length: {} Angle: {}'.format(length, angle)))

input('Press 1 for DMS to Deciman Degrees Cenversion')
print("Convert DMS to Decimal Degrees?")
print("Enter Deg, Min, and Sec of First Latitude")
Deg_Lat1 = int(input("Enter Degrees: "))
Min_Lat1 = int(input("Enter Minutes: "))
Sec_Lat1 = int(input("Enter Seconds: "))
Latitude1 = DMS_DecDeg(Deg_Lat1, Min_Lat1, Sec_Lat1)
print(Latitude1)
print("Enter Deg, Min, and Sec of First Longitude")
Min_Long1 = int(input("Enter Degrees: "))
Deg_Long1 = int(input("Enter Minutes: "))
Sec_Long1 = int(input("Enter Seconds: "))
Longitude1 = DMS_DecDeg(Deg_Long1, Min_Long1, Sec_Long1)
print(Longitude1)
print("Enter Deg, Min, and Sec of Second Latitude")
Deg_Lat2 = int(input("Enter Degrees: "))
Min_Lat2 = int(input("Enter Minutes: "))
Sec_Lat2 = int(input("Enter Seconds: "))
Latitude2 = DMS_DecDeg(Deg_Lat2, Min_Lat2, Sec_Lat2)
print(Latitude2)
print("Enter Deg, Min, and Sec of Second Longitude")
Deg_Long2 = int(input("Enter Degrees: "))
Min_Long2 = int(input("Enter Minutes: "))
Sec_Long2 = int(input("Enter Seconds: "))
Longitude2 = DMS_DecDeg(Deg_Long2, Min_Long2, Sec_Long2)
print(Longitude2)



DMS_Vector(Latitude1, Longitude1, Latitude2, Longitude2)
