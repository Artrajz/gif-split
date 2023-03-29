# gifSplit

这是一个可以将gif拆分成图片的脚本，功能有gif拆分图片、单张图片转灰度图、gif拆分成图片并转存灰度图

# 使用方法

## 参数说明

```
H:\gif-split>python gifSplit.py -h

usage: gifSplit.py [-h] [-g2j] [-j2gj] [-g2gj] [-i IMG] [-s SIZE]

gif tool,used for showing picture or animate on oled

optional arguments:
  -h, --help            show this help message and exit
  -g2j, --gif2jpg       run gif2jpg （gif拆分成图片）
  -j2gj, --jpg2gray_jpg
                        run jpg2gray jpg （单张图片转灰度图）
  -g2gj, --gif2gray_jpg
                        run gif2gray_jpg （gif拆分成灰度图）
  -i IMG, --img IMG     img path （这里填需要转换的图片路径）
  -s SIZE, --size SIZE  default=1280x640 （默认大小为1280x640）
```

## 使用示例

```
python gifSplit.py -g2gj -i gif_path
```

意思是使用gif拆分成灰度图功能，将gif拆分成灰度图，大小默认为1280x640，原图比例保持不变，多出来的地方会用**黑色填充**。

如果要**改成其他大小**再加上参数`-s 128x64`即可。

如果不需要填充，**只拆分GIF**，在参数-s 后加上原图片的大小即可。

注意如果是在SSD1306上使用必须要和屏幕分辨率**成比例关系**，比如128x64的分辨率可以用1280x640的图片，否则也不是不可以运行，只是oled上显示的图片将会被拉伸。
