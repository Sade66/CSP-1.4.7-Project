import PIL  
from PIL import ImageFilter  
from PIL import Image  
from PIL import ImageFont  
import matplotlib.pyplot as plt  
import os.path  
import PIL.ImageDraw  
import textwrap
# get_images code adapted from source code provided by PLTW.
def get_images(directory=None):
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list
    

#All code below here is original.

def frame_image(image, wide, r,g,b):
    width, height= image.size
    frame = PIL.Image.new('RGBA', (width, height), (0,0,0,0))
    drawing_layer = PIL.ImageDraw.Draw(frame)
    drawing_layer.rectangle([(width/wide,height/wide), ((width/wide)*(wide-1),(height/wide)*(wide-1))],fill=(127,0,127,255))
    result = PIL.Image.new('RGBA', image.size, (r,g,b,255))
    result.paste(image,(0,0),mask=frame)
    print 'Framing Image...'
    print 'Image',image,'has been framed.'
    return result
    
def frame_all_images(wider, r,g,b, directory=None):
    directory = os.getcwd()
    new_directory = os.path.join(directory, "Framed Images")
    try:
        os.mkdir(new_directory)
    except:
        pass
    images, files = get_images(directory)
    for n in range(len(images)):
        fname,ftype = files[n].split('.')
        new_image = frame_image(images[n], wider ,r,g,b)
        new_name = os.path.join(new_directory,fname + ".png")
        new_image.save(new_name)
    print 'Success! All images have been framed!'
    
def tint_image(image, r,g,b):
    result = PIL.Image.new('RGBA', image.size, (r,g,b,105))
    image.paste(result,(0,0),result)
    print 'Tinting Image...'
    print 'Image',image,'has been tinted.'
    return image
    
def tint_all_images(r,g,b, directory=None):
    directory = os.getcwd()
    new_directory = os.path.join(directory, "Tinted Images")
    try:
        os.mkdir(new_directory)
    except:
        pass
    images, files = get_images(directory)
    for n in range(len(images)):
        fname,ftype = files[n].split('.')
        new_image = tint_image(images[n], r,g,b)
        new_name = os.path.join(new_directory,fname + ".png")
        new_image.save(new_name)
    print 'Success! All images have been tinted!'
    
def blur_image(image, radius):
    blur = image.filter(ImageFilter.GaussianBlur(radius))
    image.paste(blur,(0,0))
    print 'Blurring Image...'
    print 'Image',image,'has been blurred.'
    return image
    
def blur_all_images(radius, directory=None):
    directory = os.getcwd()
    new_directory = os.path.join(directory, "Blurred Images")
    try:
        os.mkdir(new_directory)
    except:
        pass
    images, files = get_images(directory)
    for n in range(len(images)):
        fname,ftype = files[n].split('.')
        new_image = blur_image(images[n], radius)
        new_name = os.path.join(new_directory,fname + ".png")
        new_image.save(new_name)
    print 'Success! All images have been blurred!'
    
def text_on_image(image, text, size, line_width, r,g,b):
    '''Font must be one of the following:
        - 'Arial.ttf'
        - More
    '''
    font = ImageFont.truetype("Arial.ttf",size)
    width, height = image.size
    img = Image.new('RGBA', (width,height), (0,0,0,0))
    write = PIL.ImageDraw.Draw(img)
    lines = textwrap.fill(text, width=line_width)
    w,h = font.getsize(lines)
    print w,width,h,height
    write.text((((width-w)/2),((height-h)/2)),lines,(r,g,b),font=font)
    image.paste(img,(0,0),img)
    print 'Image',image,'now has text on it!'
    return image
    
def text_on_all_images(text, size, line_width, r,g,b, directory=None):
    directory = os.getcwd()
    new_directory = os.path.join(directory, "Images With Text")
    try:
        os.mkdir(new_directory)
    except:
        pass
    images, files = get_images(directory)
    for n in range(len(images)):
        fname,ftype = files[n].split('.')
        new_image = text_on_image(images[n], text, size, line_width, r,g,b)
        new_name = os.path.join(new_directory,fname + ".png")
        new_image.save(new_name)
    print 'Success! All images have text on them!'