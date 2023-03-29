import os
import argparse
from PIL import Image, ImageSequence, ImageFilter

parser= argparse.ArgumentParser(description='gif tool,used for showing picture or animate on oled')
parser.add_argument('-g2j', '--gif2jpg', action="store_true",help='run gif2jpg （gif拆分成图片，大小为gif的大小）')
parser.add_argument('-j2j', '--jpg2jpg', action="store_true",help='run jpg2gray jpg （单张图片转灰度图）')
parser.add_argument('-i','--img', type=str,help='img path （这里填需要转换的图片路径）')
parser.add_argument('-s','--size', type=str,default='0x0',help='图像大小(默认为原图大小)')
parser.add_argument('-m','--mode', type=str,default='RGB',help='default=RGB （图像模式默认为RGB，可选RGB|L|1）')
parser.add_argument('-f','--fill', type=int,default=0,help='default=0 （是否填充，0不填充|1黑色|2白色）')


args = parser.parse_args()

target_size = args.size.split('x')
tw = int(target_size[0])
th = int(target_size[1])

img_path = args.img
mode = args.mode
fill = args.fill


def gif2jpg():
    print('runing gif2jpg...')
    gif = img_path.split('.')[0]

    path = gif+'_g2j'

    im = Image.open(img_path)
    iter = ImageSequence.Iterator(im)
    
    try:
        os.mkdir(path)
    except:
        pass

    
    try:
        for im in iter:
            current = im.tell()
            width = im.size[0]
            height = im.size[1]

            if tw != 0 and th != 0:
                scale = max(width / tw, height / th)
                nw = int(width / scale +0.5)
                nh = int(height / scale + 0/5)
                im = im.resize((nw, nh))
            
            if mode.upper() == "1":
                im = im.convert("L")
                im = im.point(lambda x: 0 if x<128 else 255, '1')
            else:
                im = im.convert(mode.upper())
            
            if fill:
                new_image = Image.new(mode, (tw,th), 0)
                new_image.paste(im, ((tw-nw) // 2,(th-nh) // 2))
                im = new_image
            
            im.save(path+'/'+str(current)+'.jpg')

    except TypeError as error:
        print(error)


def jpg2jpg():
    print('runing jpg2jpg...')
    jpg = img_path.split('.')[0]
    path = jpg+'_j2j'
    
    try:
        os.mkdir(path)
    except:
        pass
    
    try:
        im = Image.open(img_path)
        width = im.size[0]
        height = im.size[1]
        
        if tw != 0 and th != 0:
            if fill:
                scale = max(width / tw, height / th)
                nw = int(width / scale +0.5)
                nh = int(height / scale + 0/5)
                im = im.resize((nw, nh))
            else:
                im = im.resize((tw, th))

        if mode.upper() == "1":
                im = im.convert("L")
                im = im.point(lambda x: 0 if x<128 else 255, '1')
        else:  
            im = im.convert(mode.upper())
        
        if fill:
            new_image = Image.new('1', (tw,th), 0)
            new_image.paste(im, ((tw-nw) // 2,(th-nh) // 2))
            im = new_image
            
        
        im.save(path+'/'+jpg+'.jpg')
    except TypeError as error:
        print(error)


        
if __name__ == '__main__':
    print(args)
    if args.gif2jpg:
        gif2jpg()
    if args.jpg2jpg:
        jpg2jpg()

    print('finish')
