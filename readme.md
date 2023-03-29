# gif-split

这是一个可以将gif拆分成图片的脚本，功能有

- gif拆分jpg：模式有RGB、灰度图像和二值图像，可以修改图片大小。
- jpg转jpg：模式有RGB、灰度图像和二值图像，可以修改图片大小

# 使用方法

## 参数说明

```
H:\gif-split>python gifSplit.py -h

usage: gifSplit.py [-h] [-g2j] [-j2j] [-i IMG] [-s SIZE] [-m MODE] [-f FILL]

gif tool,used for showing picture or animate on oled

optional arguments:
  -h, --help            show this help message and exit
  -g2j, --gif2jpg       run gif2jpg （gif拆分成图片，大小为gif的大小）
  -j2j, --jpg2jpg       run jpg2gray jpg （单张图片转灰度图）
  -i IMG, --img IMG     img path （这里填需要转换的图片路径）
  -s SIZE, --size SIZE  图像大小(默认为原图大小)
  -m MODE, --mode MODE  default=RGB （图像模式默认为RGB，可选RGB|L|1）
  -f FILL, --fill FILL  default=0 （是否填充，0不填充|1黑色|2白色）
  -b BINARY_SCOPE, --binary_scope BINARY_SCOPE
                        default=-1 （二值化范围，默认使用PIL库原版二值化,可选范围0-255）
```

## 使用示例

## gif2jpg

```
python gifSplit.py -g2j -i bad_apple.gif -s 1280x640 -m 1 -f 1 -b 128
```

- 意思是将gif拆分成图片，文件为bad_apple.gif，大小为1280x640，原图比例保持不变，多出来的地方会用**黑色填充**，模式为二值图像，二值范围为灰度值在0-127之间为0，128-255之间为1，保存至文件夹**bad_apple_g2j**。
- 注意如果是在SSD1306上使用必须要和屏幕分辨率**成任意比例关系**，比如128x64的分辨率可以用640x320、1280x640的图片，否则也不是不可以运行，只是oled上显示的图片将会被拉伸。

## jpg2jpg

```
python gifSplit.py -j2j -i head.jpg -m L
```

- 意思是处理jpg图片，文件是head.jpg，大小为原图大小，模式为灰度图像，不填充，保存至文件夹**head_j2j**。

```
python gifSplit.py -j2j -i head.jpg -s 1000x550 -m RGB
```

- 意思是处理jpg图片，文件是head.jpg，大小为原图1000x550，模式为RGB图像，不填充，保存至文件夹**head_j2j**。
- 由于1000x550和原图比例不一致，原图将会被拉伸。
