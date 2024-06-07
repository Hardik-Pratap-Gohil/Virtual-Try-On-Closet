# Week4

## Learning resources
In thsi week, we will begin by starting to learn about Semantic segmentation 
(https://www.youtube.com/watch?v=nDPWywWRIRo&list=RDQMw0DagWEDkno&start_radio=1)[This] lecture will explain the basic concepts around semantic segmentation and topics that follow afterwards  

We will be following the UNet architecture which is famous for semantic segmentation. This is the paper : (https://arxiv.org/pdf/1505.04597)[U-Net: Convolutional Networks for Biomedical
 Image Segmentation]   

After this also read this interesting paper by Google named (https://arxiv.org/pdf/1606.00915)[DeepLab] which is very famous. You can ignore the maths used in CRFs  
 Next up, open the Code folder, you will see UNet.ipynb which is an implementation of Unet architecture on the Cityscapes dataset. Try and get an understanding of how this is working.   
Note: Any machine learning model's code has a few standard steps

## Hands on Implementation

### Part 1
Navigate to the Code folder and open Deeplab.ipynb. This notebook has an implementation of a pretrained Deeplab network and this mostly focuses on ways of visualising the output of segmentation models. Two methods, namely Segmentation map and Overlayed Segmentation have been used.  
From this, we take the inference that Deeplab which is trained on Coco dataset is not good enough to work on Cityscapes dataset as these two are fundamentally different from each other. However, it manages to detect basic objects like cars and humans very effectively

### Part 2
Next, navigate to the Code folder and open UNet.ipynb. This notebook contains an implementation of the modified U-Net architecture applied to the Cityscapes dataset. Follow these steps:  

- **Understand the Code:**  Review the notebook to understand how the U-Net model is implemented. Note the preprocessing steps, the structure of the model, and the training loop.
- **Standard Steps in Machine Learning Model Code:** 
  -Data Loading and Preprocessing
  -Model Definition
  -Loss Function and Optimizer
  -Training Loop
  -Evaluation and Inference



- **Data Loading:** The Cityscapes dataset is used in this implementation. Ensure you have the dataset downloaded and properly set up as described in the notebook. This dataset has 34 classes of common objects that are seen on urban roads.
- **Model Training:** We will be using a modified U-net architecture where the encoder has been replaced by a pretrained RESNET network which was trained on RESNET network and we will just be training the decoder corresponding to it

One sample output of both the models has been posted  

## Assignment


- 
