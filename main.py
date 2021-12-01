if __name__ == '__main__':
    def main():
        import math

        #Convert degrees/minutes/seconds (Lat and Long on Google Earth) to decimal degrees
        def DMS_to_DecDeg(geoDeg, geoMin, geoSec):
            while True:
                try:
                    total = geoDeg + (geoMin/60) + (geoSec/3600)
                    return(round(total,5))
                except: print('Inputs require integers. Try again.')

        #Convert decimal degrees to vector notation        
        def DecDeg_to_Vector(lat1, long1, lat2, long2):
            xstart = lat1 * (40000/360) * 3280.4
            ystart = long1 * (40000/360) * 3280.4
            xstop = lat2 * (40000/360) * 3280.4
            ystop =  long2 * (40000/360) * 3280.4

            x_vector = xstop - xstart
            y_vector = ystop - ystart

            length = math.sqrt(x_vector**2 + y_vector**2)
            angle = math.atan(y_vector/x_vector)

            return(print('i:{}, j:{}, Length: {} Angle: {}'.format(x_vector, y_vector, length, angle)))


        def menu():
            #looping through inputs until correct input type is entered
            while True:
                print('Vector Calculator')
                selection = None
                try:
                    selection = int(input('1: Convert DMS to Decimal Degrees\n2: Convert Decimal Degrees to Vector Notation\n3:Convert DMS to Vector Notation\n(0 to quit)\n'))
                    #DMS to decimal degrees
                    if selection == 1:
                        #looping through inputs until correct input type is entered
                        while True:
                            print('DMS to Decimal Degrees')
                            try:
                                print('Enter DMS for Latitide or Longitude')
                                geoDeg1 = float(input('Enter degrees: '))
                                geoMin1 = float(input('Enter mins: '))
                                geoSec1 = float(input('Enter secs: '))
                                print('DMS to Decimal Degrees: ''{}{}, {} minutes, and {} seconds equals'.format(geoDeg1,chr(176),geoMin1,geoSec1), '{}{}'.format(DMS_to_DecDeg(geoDeg1, geoMin1, geoSec1),chr(176)))
                                latitude1 = DMS_to_DecDeg(geoDeg1,geoMin1, geoSec1)
                                break
                            except: print('***Inputs require integers. Try again.***')
                    #decimal degrees to vector notation
                    elif selection == 2:
                        lat1 = float(input('Enter latitude 1: '))
                        long2 = float(input('Enter longitude 1: '))
                        lat2 = float(input('Enter latitude 2: '))
                        long2 = float(input('Enter longitude 2: '))
                        print(DecDeg_to_Vector(lat1, long2, lat2, long2))
                    #converts DMS directly into vector notation ***THIS SELECTION STILL NEEDS WORK (NEED TO IMPLEMENT FOR LOOP AND ARRAY)***
                    elif selection == 3:
                        print('Enter DMS for Latitide 1')
                        geoDeg1 = float(input('Enter degrees: '))
                        geoMin1 = float(input('Enter mins: '))
                        geoSec1 = float(input('Enter secs: '))
                        print('DMS to Decimal Degrees: ''{}{}, {} minutes, and {} seconds equals'.format(geoDeg1,chr(176),geoMin1,geoSec1), '{}{}'.format(DMS_to_DecDeg(geoDeg1, geoMin1, geoSec1),chr(176)))
                        latitude1 = DMS_to_DecDeg(geoDeg1,geoMin1, geoSec1)

                        print('Enter DMS for Longitude 1')
                        geoDeg2 = float(input('Enter degrees: '))
                        geoMin2 = float(input('Enter mins: '))
                        geoSec2 = float(input('Enter secs: '))
                        print('DMS to Decimal Degrees: ''{}{}, {} minutes, and {} seconds equals'.format(geoDeg2,chr(176),geoMin2,geoSec2), '{}{}'.format(DMS_to_DecDeg(geoDeg2, geoMin2, geoSec2),chr(176)))
                        longitude1 = DMS_to_DecDeg(geoDeg2,geoMin2, geoSec2)

                        print('Enter DMS for Latitide 2')
                        geoDeg3 = float(input('Enter degrees: '))
                        geoMin3 = float(input('Enter mins: '))
                        geoSec3 = float(input('Enter secs: '))
                        print('DMS to Decimal Degrees: ''{}{}, {} minutes, and {} seconds equals'.format(geoDeg3,chr(176),geoMin3,geoSec3), '{}{}'.format(DMS_to_DecDeg(geoDeg3, geoMin3, geoSec3),chr(176)))
                        latitude2 = DMS_to_DecDeg(geoDeg3,geoMin3, geoSec3)

                        print('Enter DMS for Longitude 2')
                        geoDeg4 = float(input('Enter degrees: '))
                        geoMin4 = float(input('Enter mins: '))
                        geoSec4 = float(input('Enter secs: '))
                        print('DMS to Decimal Degrees: ''{}{}, {} minutes, and {} seconds equals'.format(geoDeg4,chr(176),geoMin4,geoSec4), '{}{}'.format(DMS_to_DecDeg(geoDeg4, geoMin4, geoSec4),chr(176)))
                        longitude2 = DMS_to_DecDeg(geoDeg4,geoMin4, geoSec4)

                        print(DecDeg_to_Vector(latitude1, longitude1, latitude2, longitude2))
                    #exit condition
                    elif selection == 0:
                        print('Thanks.')
                        return
                    else:
                        print('***Entered value was not an option. Try again.***')
                except: 
                    print('***Incorrect type. Input requires an integer. Try again.***')
        
        menu()

    main()