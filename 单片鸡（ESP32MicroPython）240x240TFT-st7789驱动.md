![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/27a10c9c6b9c43f9b68a16657676a539.jpeg)

**我们的项目是在240x240屏幕上显示下面这张动态图片**

![请添加图片描述](https://img-blog.csdnimg.cn/direct/3b3857940e95484ca0d29409bf7d9896.webp)

# 关于ST7789
ST7789是由Sitronix公司研制的一款高度集成的液晶显示控制器芯片，它被广泛用于驱动LCD屏幕。这款芯片支持RGB565、RGB666以及RGB888格式的彩色显示，具有240x320像素的分辨率和最大60帧/秒的刷新率。在市场上，采用ST7789驱动IC的屏幕并不少见，例如1.3寸和1.54寸的屏幕均采用了这款驱动芯片。此外，值得注意的是，尽管驱动芯片相同，由于不同TFT厂家在设计接口时各有不同，所以使用体验可能会有所差异。

# 240x240屏幕介绍

![请添加图片描述](https://img-blog.csdnimg.cn/direct/dc49b6e4d92346ebb2febd14f1f71e1b.jpeg)
![请添加图片描述](https://img-blog.csdnimg.cn/direct/9fd5afd72917429bad21ccd02ff1e4a8.jpeg)
有8个引脚，说明如下
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/b859de6783e94f71a70d538c3720ffb7.png)
和esp32接线方面
![请添加图片描述](https://img-blog.csdnimg.cn/direct/564f13728a6b49109583c61f7c4cbe8f.png)
![请添加图片描述](https://img-blog.csdnimg.cn/direct/79cc38f32f1649ab9cc8e02b0b20144f.jpeg)
# 代码部分
在ESP32上使用ST7789驱动模块显示13张图片的。首先，它导入了必要的库，然后初始化了ST7789驱动模块，将背景设置为黑色。接着，它创建了一个包含13个文件对象的列表，这些文件对象分别对应13张图片。`show_img()`函数是一个无限循环，它会遍历这13个文件对象，每次读取一张图片的数据，并将其显示在屏幕上。为了控制图片切换速度，代码中添加了一个0.1秒的延时。最后，`main()`函数调用了`show_img()`函数，程序开始执行。

```python
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



```





