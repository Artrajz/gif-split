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

