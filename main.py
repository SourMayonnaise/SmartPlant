import Adafruit_DHT
import epd1in54b
import Image
import ImageFont
import ImageDraw
import time

#sensor configuration
sensor = Adafruit_DHT.DHT11
pin = 23
#screen configuration
COLORED = 1
UNCOLORED = 0


def main():
    epd = epd1in54b.EPD()
    epd.init()

    # clear the frame buffer
    frame_black = [0xFF] * (epd.width * epd.height / 8)
    frame_red = [0xFF] * (epd.width * epd.height / 8)
    
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)) 
        #draw background
        epd.draw_horizontal_line(frame_red, 0, 65, 1000, COLORED);
        epd.draw_horizontal_line(frame_red, 0, 66, 1000, COLORED);
        
        epd.draw_horizontal_line(frame_red, 0, 130, 1000, COLORED);
        epd.draw_horizontal_line(frame_red, 0, 131, 1000, COLORED);
        
        epd.draw_vertical_line(frame_red, 100, 65, 65, COLORED);
        epd.draw_vertical_line(frame_red, 101, 65, 65, COLORED);
        
        font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 18)
        font_big = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 30)
        font_huge = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 40)

        epd.display_string_at(frame_black, 10, 20, time.strftime("%a %d %b"), font_big, COLORED)
        epd.display_string_at(frame_black, 10, 70, "T", font_big, COLORED)
        epd.display_string_at(frame_black, 20, 80, str(int(temperature))+"C", font_huge, COLORED)
        epd.display_string_at(frame_black, 110, 70, "H", font_big, COLORED)
        epd.display_string_at(frame_black, 120, 80, str(int(humidity))+"%", font_huge, COLORED)
        epd.display_string_at(frame_black, 30, 160, "Last watered : ", font, COLORED)
        epd.display_frame(frame_black, frame_red)
        
        epd.sleep()
    else:
        print('Failed to get reading. Try ')
        

if __name__ == '__main__':
    main()
