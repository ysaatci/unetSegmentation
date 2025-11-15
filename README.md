# Implementation of deep learning network Unet for Cerebral veins segmentation and Cerebral aneurysm classification/segmentation.

The architecture was inspired by [U-Net: Convolutional Networks for Biomedical Image Segmentation](http://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/).

---

## Overview

### Data

The original dataset is gathered with the collabration of https://www.cddft.nhs.uk/services/neurology, it includes MRI scans of patients with cerebral aneurysms located in different parts of the brain.



### Model


This deep neural network is implemented with Keras functional API, which makes it extremely easy to experiment with different interesting architectures.

Output from the network is a 512*512 which represents mask that should be learned. Sigmoid activation function
makes sure that mask pixels are in \[0, 1\] range.

### Training

The model is trained for roughly 100 epochs on a server with around 40~ Nvidia 2080 GPU's.

After 100 epochs, calculated accuracy is about 0.97.

Loss function for the training is dice loss function since the MRI scans have class imbalances.


---


### Results

Segmentation results for cerebral veins, aneurysm segmentation is done in a different repo.\


![](https://github.com/ysaatci/unetSegmentation/blob/main/ezgif.com-optimize.gif)
![](https://github.com/ysaatci/unetSegmentation/blob/main/ezgif.com-speed.gif)

