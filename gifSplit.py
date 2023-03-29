import os
import argparse
from PIL import Image, ImageSequence

parser = argparse.ArgumentParser(description='gif tool,used for showing picture or animate on oled')
parser.add_argument('-g2j', '--gif2jpg', action="store_true",help='run gif2jpg （gif拆分成图片）')
parser.add_argument('-j2gj', '--jpg2gray_jpg', action="store_true",help='run jpg2gray jpg （单张图片转灰度图）')
parser.add_argument('-g2gj', '--gif2gray_jpg', action="store_true",help='run gif2gray_jpg （gif拆分成灰度图）')
parser.add_argument('-i','--img', type=str,help='img path （这里填需要转换的图片路径）')
parser.add_argument('-s','--size', type=str,default='1280x640',help='default=1280x640 （默认大小为1280x640）')

args = parser.parse_args()

target_size = args.size.split('x')
tw = int(target_size[0])
th = int(target_size[1])

img_path = args.img


def gif2jpg():
    print('runing gif2jpg...')
    gif = img_path.split('.')[0]

    path = gif+'_gif2jpg'

    #获取gif迭代流
    im = Image.open(img_path)
    iter = ImageSequence.Iterator(im)
    
    # 创建文件夹
    try:
        os.mkdir(path)
    except:
        pass

    #图片转换，放入文件夹
    try:

        for im in iter:
            current = im.tell()
            width = im.size[0]   # 获取宽度
            height = im.size[1]   # 获取高度
            scale = max(width / tw, height / th)
            
            nw = int(width / scale +0.5)
            nh = int(height / scale + 0/5)
            
            im = im.resize((nw, nh))
            im = im.convert('1')
            
            new_image = Image.new('1', (tw,th), 0)
            new_image.paste(im, ((tw-nw) // 2,(th-nh) // 2))
            
            image = new_image
            image.save(path+'/'+str(current)+'.jpg')
    except TypeError as error:
        print(error)




def jpg2gray_jpg(size):
    print('runing jpg2gray_jpg...')
    jpg = img_path.split('.')[0]
    path = jpg+'_jpg2gray'
    
    try:
        os.mkdir(path)
    except:
        pass
    
    try:
        im = Image.open(img_path)
        width = im.size[0]   # 获取宽度
        height = im.size[1]   # 获取高度
        scale = max(width / tw, height / th)
        
        nw = int(width / scale +0.5)
        nh = int(height / scale + 0/5)
        
        im = im.resize((nw, nh))
        
        new_image = Image.new('1', (tw,th), 0)
        new_image.paste(im, ((tw-nw) // 2,(th-nh) // 2))
        
        im = new_image
        im = im.convert('1')
        im.save(path+'/'+jpg+'.jpg')
    except TypeError as error:
        print(error)

def gif2gray_jpg(size):
    print('runing gif2gray_jpg...')
    gif = img_path.split('.')[0]
    
    path = gif+"_gif2gray_jpg"
    
    #获取gif迭代流
    im = Image.open(img_path)
    iter = ImageSequence.Iterator(im)
    
    try:
        os.mkdir(path)
    except:
        pass
    
    try:
        
        for im in iter:
            current = im.tell()
            width = im.size[0]   # 获取宽度
            height = im.size[1]   # 获取高度
            scale = max(width / tw, height / th)
            
            nw = int(width / scale +0.5)
            nh = int(height / scale + 0/5)
            
            im = im.resize((nw, nh))
            
            new_image = Image.new('1', (tw,th), 0)
            new_image.paste(im, ((tw-nw) // 2,(th-nh) // 2))
            
            im = new_image
            image = im.convert('1')
            image.save(path+'/'+str(current)+'.jpg')
    except TypeError as error:
        print(error)
    
if __name__ == '__main__':
    if args.gif2jpg:
        gif2jpg()
    if args.jpg2gray_jpg:
        jpg2gray_jpg(args.size)
    if args.gif2gray_jpg:
        gif2gray_jpg(args.size)

    print('finish')
