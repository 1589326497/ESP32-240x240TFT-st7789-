from machine import Pin, SPI
import st7789_itprojects
import time


tft = st7789_itprojects.ST7889_Image(SPI(2, 60000000), dc=Pin(2), cs=Pin(5), rst=Pin(15))
tft.fill(st7789_itprojects.color565(0, 0, 0))  # 背景设置为黑色

# 因为用到了13张图片，所以这里创建13个文件对象 放到列表中
f_list = [open("text_img{}.dat".format(i), "rb") for i in range(0, 13)]


def show_img():
    while True:
        for f in f_list:  # 遍历13个文件，显示图片
            f.seek(0)	#文件指针拉回到开始处
            for row in range(0, 240, 24*3):
                buffer = f.read(11520*3)
                tft.show_img(0, row, 239, row+24*3, buffer)


def main():
    show_img()

if __name__ == "__main__":
    main()

