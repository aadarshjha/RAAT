'''
Input Params: Data file name
Output Params: Result File name
File Description: MRI Super Resolution
Ex Input: superResolution.py 1000_3.nii.gz 1000_3_superResolution.nii.gz
'''

import sys
import ants
import antspynet

def arg_func(args):
    #Make sure input is selected
    if len(args) != 3:
        print("Usage: " + args[0] + " <inputImage> <OutputImage>")
        sys.exit(1)

    inputImage = args[1]
    outputImage = args[2]

    image = ants.image_read(inputImage)
    superRes = antspynet.utilities.mri_super_resolution(image)
    ants.image_write(superRes, outputImage)

if __name__ == '__main__':
    arg_func(sys.argv)
