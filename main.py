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
            xstop = lat2 * (40000/360) * 3280.4
            ystart = long1 * (40000/360) * 3280.4
            ystop =  long2 * (40000/360) * 3280.4

            x_vector = xstop - xstart
            y_vector = ystop - ystart

            length = math.sqrt(x_vector**2 + y_vector**2)
            angle = math.atan(y_vector/x_vector)

            return(print('Length: {} Angle: {}'.format(length, angle)))


        def menu():
            #looping through inputs until correct input type is entered
            while True:
                print('Vector Calculator')
                selection = None
                try:
                    selection = int(input('1: Convert DMS to Decimal Degrees\n2: Convert Decimal Degrees to Vector Notation\n(0 to quit)\n'))
                    #DMS to decimal degrees
                    if selection == 1:
                        #looping through inputs until correct input type is entered
                        while True:
                            print('DMS to Decimal Degrees')
                            try:
                                geoDeg = int(input('Enter degrees: '))
                                geoMin = int(input('Enter mins: '))
                                geoSec = int(input('Enter secs: '))
                                print('DMS to Decimal Degrees: ''{}{}, {} minutes, and {} seconds equals'.format(geoDeg,chr(176),geoMin,geoSec), '{}{}'.format(DMS_to_DecDeg(geoDeg, geoMin, geoSec),chr(176)))
                                break
                            except: print('***Inputs require integers. Try again.***')
                    #decimal degrees to vector notation **not done**
                    elif selection == 2:
                        lat1 = int(input('Enter latitude'))
                        DecDeg_to_Vector()
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