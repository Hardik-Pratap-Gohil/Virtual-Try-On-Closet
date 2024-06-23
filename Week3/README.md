# Welcome to Week 3 
This consists of two parts, GAN and Pose Estimation. This week will be a bit intensive and requires lot of understanding and patience. The math underlying various functions and libraries has been provided, although not useful in assignment, it will help you get intuition of how things actually work inside the blackbox.

## Introduction to GAN
After having your concepts of Neural Networks and OpenCV clear, now it's the time to explore the realm of **Generative Adversarial Network (GAN)**. First published in 2014 by Ian Goodfellow and his colleagues, GAN has revolutionized the domain the image generation and sequence predection. The [introductory paper on GAN](https://arxiv.org/pdf/1406.2661) unravels the math behind the fundamental GAN architecture and gives great insights on how GAN actually manages to generate images so magically. To understand the paper better, these two youtube videos will help...
1) [Intro to GAN by IBM](https://youtu.be/TpMIssRdhco?si=MbwUR4CEJXVhSNax)
2) [Math behind GAN by Normalised Nerd](https://youtu.be/Gib_kiXgnvA?si=UZ8x0dZgRmzW95BQ)

### Hands-on GAN assignment
[Assignment link](https://colab.research.google.com/drive/11NjOgXZXK1dT_D1lt-5eyJ0Hnv-i0sgl?usp=sharing)
#### Assignment Instructions
1) Now we will build a GAN model using Convolutional Neural Networks in Pytorch. In the assignment we have uploaded, we have followed the architecture mentioned in the [DCGAN paper](https://arxiv.org/pdf/1511.06434) (Deep Convolutional Generative Adversarial Network). Go through the paper and for clarity and attempt the assignment without any aid based on your understanding of GAN and CNN (Hints provided for few block of code to get started :)). This will help in understanding the paper and GAN architecture better.
2) Make a copy of this assignment in your drive and attempt the objectives mentioned in the assignment in your copy of the assignment. In the submission form, upload the colab link of your assignment.
#### All the best!


## Pose Estimation
Pose estimation is an ever-evolving domain of computer vision and has been under research for quite some time. The present pose estimation models' high accuracy stand as a testimony to the recent developments. It fundamentally revolves around the task of identifying a person and his pose using the relative postions of his body parts and visualise it. The initial version of the [OpenPose](https://arxiv.org/pdf/1611.08050) paper contains architecture and mechanism of the initial pose detection algorithm. [This video](https://www.youtube.com/watch?v=OgQLDEAjAZ8) marks the introduction of this paper in a conference where they have given brief overview of the procedure. If you feel over-whelmed by the amount of content in the paper, I would suggest you to go through this video and read the short explanation coming ahead...

The problem of pose estimation as been divided into various sub-problems and, as taken from the paper, are- 
1) Identifying the 18 keypoints (They are the major locations/joints of body, e.g: head, chest, left arm, etc)
2) Connecting the keypoints in the right direction/manner
3) A global problem of grouping the connected pair beloning to a particular person 

To tackle these problems, the architecture devised is made up of [VGG-19](https://medium.com/@siddheshb008/vgg-net-architecture-explained-71179310050f), and a set of 2 parallel streams of many convolutional networks, the first stream of networks giving the confidence map (to locate the keypoints) and other for Part Affinity Fields or PAFs (encoding the predicted correspondence vector between the nodes). 
After having determined the values from 't' stages of refinement, loss function is used to calculate the difference from the ground truth (in this case, we use the mean squared error loss function) and this loss is backpropagated to networks in each stage. The loss function is separately calculated for the Confidence Map series of layers and PAF series of layers and backpropagated correspondingly.
Now, to problem of connecting all the edges can be modelled similar to [Maximum Bipartite Matching problem](https://www.geeksforgeeks.org/maximum-bipartite-matching/), as in our scenario we do not want two edges to meet at the same point, in case of any body part for instance. Our major final goal is classify all the keypoints of a particular human and create a skeleton of it. As Bipartite Matching problem is a NP Hard problem (The problem whose time complexity is non-polynomial kind and hence training takes longer and longer time if the number of keypoints substantially increase), we can make two reasonable assumptions to simplify the processing -
1) Bipartite matching of all the keypoints can be modelled as bipartite matching of 2 kinds of key points and ( for instance the connections between head and chest) and matching of this keypoint with others ( in this case, chest to left shoulder).
2) Greedy selection of the edge with highest value for a particular node using the PAF values.

This finally results in the skeleton which we will generate in the assignment.

### Developments
Another paper, a successor of the present one was relased in which they had observed that only the PAF refinement is crucial for maximizing accuracy, while body part prediction refinement is not that important. Focussing only on PAF refinement led to improvement of both accuracy and training period. Enthusiasts can refer to it [here](https://arxiv.org/pdf/1812.08008). 

And finally the most awaited section dropping...
### An interactive assignment on Pose Estimation
Although it would need hell lot of resources and time to build and train an OpenPose like model on our own, the OpenPose library comes to our rescue! This simplifies our task to a large extent  
As part of this assignment, you'll will need to download OpenPose from the [github repository](https://github.com/CMU-Perceptual-Computing-Lab/openpose.git) and referring to the documentation, generate pose skeleton for 5 of your favourite memes, and play with various functions of OpenPose and explore their functioning. As a bonus, make pose skeleton for a video meme
