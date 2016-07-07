# coding: utf8
import sys
import os
import shutil
from PIL import Image

#自动生成android,ios 需要的图标
#python icon.py
def generate():
    iPath = 'icon.png'
    icon = Image.open(iPath)

    #android
    sizeFolders = [
        ('drawable',512),
        ('drawable-hdpi',72),
        ('drawable-ldpi',36),
        ('drawable-mdpi',48),
        ('drawable-xhdpi',96),
        ('drawable-xxhdpi',144),
        ('drawable-xxxhdpi',192),
    ]
    names = ['icon','push']

    for s in sizeFolders:
        folder,size = s
        img = icon.resize((size,size),Image.ANTIALIAS)

        oFolder = 'android/'+folder
        if os.path.exists(oFolder):
            shutil.rmtree(oFolder)
        os.makedirs(oFolder)
        for name in names:
            oPath = oFolder+'/'+name+'.png'
            img.save(oPath, icon.format)
            print(oPath)

    # ios
    sizes = [
        29,
        40,
        48,
        50,
        57,
        58,
        72,
        76,
        80,
        96,
        100,
        114,
        120,
        144,
        152,
    ]

    if os.path.exists('ios'):
        shutil.rmtree('ios')
    os.makedirs('ios')
    for size in sizes:
        img = icon.resize((size,size), Image.ANTIALIAS)
        oPath = 'ios/icon-'+str(size)+'.png'
        img.save(oPath, icon.format)
        print(oPath)

generate()
