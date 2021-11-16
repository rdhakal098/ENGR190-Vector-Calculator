
#Convert degrees/minutes/seconds (Lat and Long on Google Earth) to decimal degrees

def GeoCor_DecDeg(geoDeg, geoMin, geoSec):
    total = geoDeg + (geoMin/60) + (geoSec/3600)
    return(total)

