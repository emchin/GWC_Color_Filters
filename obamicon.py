'''
#obamicon: turns everything red or dark blue, with some tans (like the Obama ad)

#emily_inversion: inverts the colors

#karli_myFilter: Karli's filter, tasteful inverse rainbow

#myOwnFilter: Krithika's filter, dark background w/sepia image

'''

from random import *
from PIL import Image
from PIL import ImageFilter
from math import *

im = '/Users/emily/Desktop/image.png' #Where to find image 

#This is for the obamicon filter:
def load_img(filename):
  im = Image.open(filename)
  return im

def show_img(im):
  im.show()

def save_img(im, filename):
  im.save(filename, "jpeg")
  show_img(im)

'''
Obamicon filter (part 2 of assignment)
'''
def obamicon(im):
  im = Image.open(im)
  pixels = im.getdata() # Load the pixel data from im.
  new_pixels = [] # Create a list to hold the new image pixel data.

  # Define color constants to use for recoloring:
  darkBlue = (0, 51, 76)
  red = (217, 26, 33)
  lightBlue = (112, 150, 158)
  yellow = (252, 227, 166)

  # Process the pixels in the image.
  for p in pixels:
    # Pixel intensity = R value + G value + B value
    intensity = p[0] + p[1] + p[2]

    if intensity < 182:
      new_pixels.append(darkBlue)

    elif intensity >= 182 and intensity < 364:
      new_pixels.append(red)

    elif intensity >= 364 and intensity < 546:
      new_pixels.append(lightBlue)

    elif intensity >=546:
      new_pixels.append(yellow)

  # Save the filtered pixels as a new image
  newim = Image.new("RGB", im.size)
  newim.putdata(new_pixels)
  
  newim.show()

'''
Other fun filters!
'''

#Grayscale filter
def gray(pic):
    im = Image.open(pic)
    result = []
    pixel = list(im.getdata())
    for r,b,g in pixel:
        sum = r + b + g
        average = int(sum/3)
        color = (average,average,average)
        result.append(color)
    image = Image.new(im.mode,im.size)
    image.putdata(result)
    image.show()

#Inversion Filter
def emily_inversion(file):
    inverted = []
    image = Image.open(file)
    pixels = list(image.getdata())
    for r, g, b, a in pixels:
        new_red = 255 - r #The more red originally, the less red now!
        new_blue = 225 - b #Conversely, the less blue the pixel was, the more blue it is now!
        new_green = 225 - g #This is why color is inverted.
        new_data = (new_red, new_green, new_blue)
        inverted.append(new_data)
    invert_image = Image.new(image.mode, image.size)
    invert_image.putdata(inverted)
    invert_image.show()

#Rainbow Filter
def karli_myFilter(picture):
    # picture1 = picture.filter(ImageFilter.BLUR)
    # return picture1
    picture = Image.open(picture)
    pixelmap = picture.load()
    rgb = picture.convert("RGB")
    width, height = picture.size
    for w in range(width):
        for h in range(height):
            rgbValue = rgb.getpixel((w, h))
            intensity = rgbValue[0]+rgbValue[1]+rgbValue[2]
            if intensity>635:
                pixelmap[w, h] = (3, 61, 5)
            elif intensity>508 and intensity < 635:
                pixelmap[w,h] = (4, 17, 134)
            elif intensity>381 and intensity < 508:
                pixelmap[w, h] = (118, 4, 218)
            elif intensity>254 and intensity < 381:
                pixelmap[w, h] = (232, 23, 0)
            elif intensity>127 and intensity < 254:
                pixelmap[w, h] = (255, 157, 9)
            elif intensity<127:
                pixelmap[w, h] = (255, 248, 134)
    picture.show()

#Sepia Filter
def myOwnFilter(loadedFile):
  loadedFile = Image.open(loadedFile)
  width, height = loadedFile.size
  pixelColor= []
  pixelMap = loadedFile.load() #create the pixel map
  #pixel = pixelMap[0,0] #get the first pixel's value
  rgb_im = loadedFile.convert('RGB')
  i = 0
  j = 0
  for i in range(width):
      for j in range(height):
        rgbValue = rgb_im.getpixel((i, j))
        grayScale = (rgbValue[0] + rgbValue[1] + rgbValue[2])/3
        pixelMap[i,j] = (int(grayScale * 1.5), int(grayScale), int(grayScale * 0.5))
  loadedFile.show()
  return loadedFile

print("\n")
print("Hello! This is a program that applies a filter to your image.")
print("Please select a filter to apply!")
print("For OBAMICON, a dramatic red-blue-tan filter, press 1.")
print("For GRAYSCALE, press 2.")
print("For COLOR INVERSION, press 3.")
print("For AN INVERSE RAINBOW, press 4.")
print("For SEPIA, press 5.")
print("\n")

user_input = raw_input()

if user_input == "1":
  obamicon(im)
elif user_input == "2":
  gray(im)
elif user_input == "3":
  emily_inversion(im)
elif user_input == "4":
  karli_myFilter(im)
elif user_input == "5":
  myOwnFilter(im)
else:
  x = randint(1,5)
  if user_input == "1":
    obamicon(im)
  elif user_input == "2":
   gray(im)
  elif user_input == "3":
    emily_inversion(im)
  elif user_input == "4":
   karli_myFilter(im)
  else:
   myOwnFilter(im)
