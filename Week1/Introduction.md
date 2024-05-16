## Virtual Try On (ViTON)

The first and foremost thing to do as part of this SOC is understanding better what the project's name means. The Virtual Try-On closet is an application that will allow users to overlay different outfits on themselves virtually.  
Now, let us understand what is the Virtual Try On problem, often summarized as ViTON. The ViTON problem, more specifically, is about pose and texture/style transfer in human body images, sometimes called person image synthesis as a whole.

- In pose transfer we want to generate an image of a person P in various poses. There are two images that we get as input: the person P’s image and the image of another person Q in the desired pose. Our goal is to generate P’s image in Q’s pose.
- In texture transfer, also called style transfer, we want to generate an image of a person in the same pose but with different style of body parts or garments. e.g. we might want to change the style of the shirt or the skin color of the person. Here the input is the image of the person, image containing the desired style and the region of the image that is to be changed.  
If a model does both of the tasks then we can generate images of a person in various poses and garments just from a single image of the person and reference pose and style images.

We will mostly be focusing on the texture transfer part initially, but can also implement pose transfer depending on the progress made.
