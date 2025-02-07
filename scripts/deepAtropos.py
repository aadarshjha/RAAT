'''
Input Params: Data file name
Output Params: Result File name
File Description: Perform Atropos-style six tissue segmentation using deep learning.
Ex Input: deepAtropos.py SubjectA_T1.nrrd SubjectA_T1_deepAtroposSegmentation.nrrd
SubjectA_T1_deepAtroposBackground.nrrd SubjectA_T1_deepAtroposCSF.nrrd SubjectA_T1_deepAtroposGM.nrrd
SubjectA_T1_deepAtroposWM.nrrd SubjectA_T1_deepAtroposDeepGM.nrrd SubjectA_T1_deepAtroposBrainStem.nrrd
SubjectA_T1_deepAtroposCerebellum.nrrd
'''

import sys
import ants
import antspynet

def arg_func(args):
    #Make sure input is selected
    if len(args) != 10:
        print("Usage: " + args[0] + " <inputImage> <Segmentation>"
              "<BackgroundOutput> <CSFOutput> <GMOutput> <WMOutput> <DeepGMOutput> <BrainStem> <Cerebellum>")
        sys.exit(1)

    inputImage = args[1]
    segmentationOutput = args[2]
    BackgroundOutput = args[3]
    CSFOutput = args[4]
    GMOutput = args[5]
    WMOutput = args[6]
    DeepGMOutput = args[7]
    BrainStemOutput = args[8]
    CerebellumOutput = args[9]

    image = ants.image_read(inputImage)
    flash = antspynet.utilities.deep_atropos(image, do_preprocessing=True, verbose=True)
    ants.image_write(flash['segmentation_image'], segmentationOutput)
    probability = flash['probability_images']
    ants.image_write(probability[0], BackgroundOutput)
    ants.image_write(probability[1], CSFOutput)
    ants.image_write(probability[2], GMOutput)
    ants.image_write(probability[3], WMOutput)
    ants.image_write(probability[4], DeepGMOutput)
    ants.image_write(probability[5], BrainStemOutput)
    ants.image_write(probability[6], CerebellumOutput)

if __name__ == '__main__':
    arg_func(sys.argv)
