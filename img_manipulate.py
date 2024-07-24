>>> from PIL import ImageColor
>>> ImageColor.getcolor('red', 'RGBA')
(255, 0, 0, 255)
>>> ImageColor.getcolor('RED', 'RGBA') # case insensitive
(255, 0, 0, 255)
>>> ImageColor.getcolor('Black', 'RGBA')
(0, 0, 0, 255)
>>> ImageColor.getcolor('chocolate', 'RGBA')
(210, 105, 30, 255)
>>> ImageColor.getcolor('CornflowerBlue', 'RGBA')
(100, 149, 237, 255)

# Pillow is expecting a tuple of four integer coordinates that represent a rect- angular region in an image.
>>> from PIL import Image
>>> catIm = Image.open('zophie.png')
# If the image file isn’t in the current working directory, change the working directory to the folder that contains the image file by calling the os.chdir() function
>>> import os
>>> os.chdir('C:\\folder_with_image_file')


>>> from PIL import Image
>>> catIm = Image.open('zophie.png')
>>> catIm.size
(816, 1088)
>>> width, height = catIm.size
>>> width
816
>>> height
1088
>>> catIm.filename
'zophie.png'
>>> catIm.format
'PNG'
>>> catIm.format_description
'Portable network graphics'
>>> catIm.save('zophie.jpg')


>>> from PIL import Image
>>> im = Image.new('RGBA', (100, 200), 'purple')
>>> im.save('purpleImage.png')
>>> im2 = Image.new('RGBA', (20, 20))
>>> im2.save('transparentImage.png')
# Here we create an Image object for an image that’s 100 pixels wide and
# 200 pixels tall, with a purple background . This image is then saved to
# the file purpleImage.png. We call Image.new() again to create another Image
# object, this time passing (20, 20) for the dimensions and nothing for the
# background color. Invisible black, (0, 0, 0, 0), is the default color used if
# no color argument is specified, so the second image has a transparent back-
# ground; we save this 20×20 transparent square in transparentImage.png.


# Cropping Images
>>> croppedIm = catIm.crop((335, 345, 565, 560))
>>> croppedIm.save('cropped.png')
# The cropping does not happen in place—that is, the
# original Image object is left untouched, and the crop() method returns a
# new Image object. The new file cropped.png will be created from the original image,


# Copying and Pasting Images onto Other Images
>>> catIm = Image.open('zophie.png')
>>> catCopyIm = catIm.copy()
# The catIm and catCopyIm variables contain two separate Image objects,
# which both have the same image on them. you can modify catCopyIm as you like and save
# it to a new filename, leaving zophie.png untouched. 


>>> faceIm = catIm.crop((335, 345, 565, 560))
>>> faceIm.size
(230, 215)
>>> catCopyIm.paste(faceIm, (0, 0))
>>> catCopyIm.paste(faceIm, (400, 500))
>>> catCopyIm.save('pasted.png')
# First we pass crop() a box tuple for the rectangular area in zophie.png
# that contains Zophie’s face. This creates an Image object representing a
# 230×215 crop, which we store in faceIm. Now we can paste faceIm onto
# catCopyIm. The paste() method takes two arguments: a “source” Image
# object and a tuple of the x- and y-coordinates where you want to paste
# the top-left corner of the source Image object onto the main Image object.
# Here we call paste() twice on catCopyIm, passing (0, 0) the first time and
# (400, 500) the second time. This pastes faceIm onto catCopyIm twice: once
# with the top-left corner of faceIm at (0, 0) on catCopyIm, and once with
# the top-left corner of faceIm at (400, 500). Finally, we save the modified
# catCopyIm to pasted.png. 


#Despite their names, the copy() and paste() methods in Pillow do not use your computer’s clipboard.
# Note that the paste() method modifies its Image object in place; it does
# not return an Image object with the pasted image. If you want to call paste()
# but also keep an untouched version of the original image around, you’ll
# need to first copy the image and then call paste() on that copy.

>>> catImWidth, catImHeight = catIm.size
>>> faceImWidth, faceImHeight = faceIm.size
>>> catCopyTwo = catIm.copy()
>>> for left in range(0, catImWidth, faceImWidth):
    for top in range(0, catImHeight, faceImHeight):
        print(left, top)
        catCopyTwo.paste(faceIm, (left, top))1
>>> catCopyTwo.save('tiled.png')
# Here we store the width of height of catIm in catImWidth and
# catImHeight. At u we make a copy of catIm and store it in catCopyTwo. Now
# that we have a copy that we can paste onto, we start looping to paste faceIm
# onto catCopyTwo. The outer for loop’s left variable starts at 0 and increases by
# faceImWidth(230). The inner for loop’s top variable start at 0 and increases
# by faceImHeight(215). These nested for loops produce values for left and
# top to paste a grid of faceIm images over the catCopyTwo Image object, as in
# Figure 17-6. To see our nested loops working, we print left and top. After
# the pasting is complete, we save the modified catCopyTwo to tiled.png.



>>> width, height = catIm.size
>>> quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
>>> quartersizedIm.save('quartersized.png')
>>> svelteIm = catIm.resize((width, height + 300))
>>> svelteIm.save('svelte.png')
