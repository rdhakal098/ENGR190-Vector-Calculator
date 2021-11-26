if __name__ == '__main__':
    def main():

        import math

        #Convert degrees/minutes/seconds (Lat and Long on Google Earth) to decimal degrees
        def DMS_to_DecDeg(geoDeg, geoMin, geoSec):
            total = geoDeg + (geoMin/60) + (geoSec/3600)
            return(round(total,5))


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
            print('Vector Calculator')
            iterations = int(input('Enter # of coordinates u wanna convert: '))
            for i in range(iterations):
                loop(input('Enter selection - 0, 1, 2: '))
        
        def loop(selection):
            match selection:
                case '0':
                   return print('Exiting')

                case 'exit':
                    return print('Exiting')

                case '1': 
                    deg = float(input('Enter Degrees: '))
                    min = float(input('Enter Minutes: '))
                    sec = float(input('Enter Seconds: '))
                    value = DMS_to_DecDeg(deg, min, sec)
                    return print(value)
                case _: return print('Try again.')

        menu()
    
    main()