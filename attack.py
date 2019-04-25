#NonTargetedAttack.py
import numpy
import sys
import PIL.ImageFile
import PIL.ImageFilter
from PIL import Image
from numpy import *
from scipy.ndimage import filters

(PIL.ImageFile).LOAD_TRUNCATED_IMAGES = True
NUMBER_OF_CLASSES = 110
SIZE = 299

InputDirectory = sys.argv[1]
OutputDirectory = sys.argv[2]

File = open(InputDirectory + "/dev.csv")
File.readline()

for line in File:
    split_line = line.strip().split(",")

    filename = split_line[0]
    true_label = int(split_line[1])
    targeted_label = int(split_line[2])

    image_pil = array(PIL.Image.open(InputDirectory + "/" + filename))

    image2 = zeros(image_pil.shape)
    for i in range(3):
        image2[:,:,i] = filters.gaussian_filter(image_pil[:,:,i],3)
    image = uint8(image2)
    new_image = Image.fromarray(image)
    #new_image = new_image.astype(numpy.uint8)

    PIL.Image.fromarray(numpy.asarray(new_image, numpy.int8), "RGB").save(OutputDirectory + "/" + filename)

File.close()
