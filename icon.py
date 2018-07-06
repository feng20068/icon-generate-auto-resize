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
        ('android/drawable',512),
        ('android/drawable-hdpi',72),
        ('android/drawable-ldpi',36),
        ('android/drawable-mdpi',48),
        ('android/drawable-xhdpi',96),
        ('android/drawable-xxhdpi',144),
        ('android/drawable-xxxhdpi',192),
    ]
    names = ['icon','push']

    for s in sizeFolders:
        folder,size = s
        img = icon.resize((size/2,size/2),Image.ANTIALIAS)

        oFolder = folder
        if os.path.exists(oFolder):
            shutil.rmtree(oFolder)
        os.makedirs(oFolder)
        for name in names:
            oPath = oFolder+'/'+name+'.png'
            img.save(oPath, icon.format)
            print(oPath)

    # ios
    sizes = [
        ('20-pad.png',20),
        ('20-pad@2x.png',40),
        ('20@2x.png',40),
        ('20@3x.png',60),
        ('29-pad.png',29),
        ('29-pad@2x.png',58),
        ('29.png',29),
        ('29@2x.png',58),
        ('29@3x.png',87),
        ('40-pad.png',40),
        ('40-pad@2x.png',80),
        ('40@2x.png',80),
        ('40@3x.png',120),
        ('50-pad.png',50),
        ('50-pad@2x.png',100),
        ('57.png',57),
        ('57@2x.png',114),
        ('60@2x.png',120),
        ('60@3x.png',180),
        ('72-pad.png',72),
        ('72-pad@2x.png',144),
        ('76-pad.png',76),
        ('76-pad@2x.png',152),
        ('83p5@2x.png',167),
    ]

    if os.path.exists('ios'):
        shutil.rmtree('ios')
    os.makedirs('ios')
    for s in sizes:
        name,size = s
        img = icon.resize((size,size), Image.ANTIALIAS)
        oPath = 'ios/'+name
        img.save(oPath, icon.format)
        print(oPath)

generate()
