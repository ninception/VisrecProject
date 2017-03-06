## Projects 2016
The work to be done in the project can be based on implementation of any paper on the topic from the last 5 years proceedings of ICCV, CVPR or ECCV conferences. The other option is to implement an idea that is slightly different than the one published in the paper. 

The tentative list of project topics is as follows:

    Object Categorization
    Object Detection
    Object Segmentation
    Fine-grained recognition
    Attribute based recognition
    Image Captioning
    Visual Question Answering
    Image Retrieval
    Action Recognition
    Person Identification
    Anomaly Detection
    Image Inpainting
    Super-resolution
    Image Colorisation/ Image resizing
    Texture Synthesis
    Video Segmentation
    Video Summarisation
    Weakly Supervised Object Detection
    Weakly Supervised Object Segmentation

-----
-----
-----

## Projects 2014

### Large Scale Face Recognition 
around 13000 faces collected locally at security gate.
A dataset of around 13000 face images will be provided to you. For some
input image you'll have to identify the matching image in the dataset and
give it as an output.
Related papers:
Any of the recent papers from Labeled face in the wild challenge
http://vis-www.cs.umass.edu/lfw/results.html


-----

### Automatic colorization of IR camera
A dataset of colored images will be provided to you. Automatic
colorization of IR camera involves matching the colored images from the
dataset with the frames of the video from IR camera and mapping the colors
of objects to the corresponding objects in frames.

Related papers are:  Colorization by Example, -R.Irony, D.Cohen-Or, and
D.Lischinski,
Eurographics symposium on Rendering (2005)
and
Colorization using Optimization, -Anat Levin, D.Lischinski,  Yair
Weiss,SIGGRAPH (2004)

-----

###  Abnormal activity detection in video (local data available)
In an unsupervised sense, it is required to identify the unusual
events. The unusual events are identified based on statistical evaluation
of events and characterising rare or unseen events.

Work done in this area includes papers such as 
"Observe locally, Infer Globally: a Space-Time MRF for Detecting Abnormal Activities with Incremental Updates", J. Kim and K. Grauman, CVPR 2009
"What's going on? Discovering Spatio-Temporal Dependencies in Dynamic Scenes", 
D. Kuettel, M. Breitenstein, L. van Gool, and V. Ferrari, CVPR 2010

-----

###  License plate recognition from video data collected locally
License plate recognition is a practical application. For this problem,
we are interested in approaches that can deal with variations in pose,
orientation and also be able to efficiently detect the license plate
and recognize the characters.

Related Work that has been done includes:
"Real-Time License Plate Recognition on an Embedded DSP-Platform",
Clemens Arth, Florian Limberger, Horst Bischof
CVPR Workshop, ECW 2007

-----

###  Detection of pedestrians in videos (local data available)
In this project, the task is, given data collected locally of people on
the roads inside campus, to be able to detect pedestrians reliably in
real time.

Related papers are: 
P. Dollar, S. Belongie and P. Perona
The Fastest Pedestrian Detector in the West
BMVC 2010

Pedestrian detection at 100 frames per second
R. Benenson, M. Mathias, R. Timofte, L. Van Gool; presented at CVPR 2012.

-----

###  Making a synopsis of a video (local data available)
This involves identifying the key elements of the video and retaining only the relevant events. 
Related Video Synopsis work has been done over here:
http://www.vision.huji.ac.il/video-synopsis/

-----

###  3D reconstruction from several images
This is a project where we would be interested in implementation of 3D reconstruction techniques and methods to make the reconstructions dense.
The book Multiview Geometry in Computer Vision by Hartley and Zisserman considers this problem in great detail. There are also papers such as the work by Marc Pollefeys that solves this problem.

-----

###  Cutting out humans in real world videos
In this work, given videos, the task is to use detection to initialize a tracker and subsequently be able to cut-out complex human motions in videos.
Related work:
Efficient Extraction of Human Motion Volumes by Tracking
J. C. Niebles, B. Han and L. Fei-Fei

-----

###  Cartoonization of videos
It involves creating cartoon like animation of any photorealistic input
video. Creating non-photorealistic cartoon like effects can be done by
transforming the video using some filtering techniques.
Related papers are:
"Video Tooning" byJue Wang, Yingqing Xu, Heung-Yeung Shum and Michael F.
Cohen, Siggraph 2004
and "Image and Video segmentation by Anisotropic kernel mean shift",Jue
Wang, Bo Thiesson, Yingqing Xu and Michael F. Cohen  ECCV 2004

-----

###  Image inpainting
Given an image and a mask, the task is to remove the elements in the mask
and replace it with elements that respect the statistical regularity in
the image. Basically this involves synthesising texture related to the
image to cover the area in the mask.

Related papers:
Object Removal by Exemplar-Based Inpainting
Criminisi, Perez and Toyama, CVPR 2003

-----

###  Exact instance detector amidtst clutter or "where is my cup?"
In this project, the task is to learn specific object templates for textureless objects that allows real time detection of these objects in the presence of clutter.

The relevant paper is:
Dominant Orientation Templates for Real-Time Detection of Texture-Less Objects 
S. Hinterstoisser, V. Lepetit, S. Ilic, P. Fua, N. Navab 
CVPR 2010
and subsequent work by the authors on this topic

-----

###  Action recognition in videos
There exist many works for recognizing actions in videos. One particular
aspect that the project could explore is how action recognition can be
done by using features such as HoG-HoF or dense trajectories combined
with fisher vector encoding.

-----

###  Similar category differentiation (like motorbikes and cycles)
In this project, the aim is to consider methods for fine-grained image categorization. The methods that work well use either mid-level representations such as "Frequent Local Histograms" or perform unsupervised alignments. The aim is to consider any such method for fine-grained image categorization in detail and evaluate it against some standard fine-grained dataset.

Related Papers:
Effective Use of Frequent Itemset Mining for Image Classification
Basura Fernando, Elisa Fromont and Tinne Tuytelaars
ECCV 2012

Fine-Grained Categorization by Alignments 
Efstratios Gavves, Basura Fernando, Cees Snoek, Arnold Smeulders and Tinne Tuytelaars
ICCV 2013 

-----

###  Tracking sport players in videos
In this project, the task is to consider some method that is robust to occlusions and can robustly track multiple people in realistic scenarios.

Related work
http://cvlab.epfl.ch/research/body/surv/
Tracking Multiple People under Global Appearance Constraints
Horesh Ben Shitrit, JÃ©rÃ´me Berclaz, FranÃ§ois Fleuret, Pascal Fua
International Conference on Computer Vision, 2011

-----

###  Organizing photo collections
Now, with large collections of photos being available, the challenge lies in being able to think of nice ways for organizing the photo collections and navigating them

One of the interesting works done in this area is photobios, where face animation is generated by finding out paths through the face space of people
Related work:
http://grail.cs.washington.edu/photobios/

Similarly, for scenes, something done on these lines is:
http://phototour.cs.washington.edu/findingpaths/

-----

###  Spatio temporal super-resolution of videos
In this project, the task is, given an input video to generate a spatio-temporal super-resolution of the video.

Related papers:
http://www.wisdom.weizmann.ac.il/~vision/SingleVideoSR.html
Space-Time Super-Resolution from a Single Video
Oded Shahar, Alon Faktor, Michal Irani 
CVPR 2011
Space-time Super-Resolution Using Graph-cut Optimization.
Uma Mudenagudi, Subhashis Banerjee and Prem Kalra
 IEEE Trans. Pattern Anal. Mach. Intell. 33(5): 995-1008 (2011)

-----

###  Pose estimation for gesture interface
In this project, the task is to consider the method used in Kinect for pose estimation and to implement a similar pose estimation with the dataset provided using decision trees

Jamie Shotton, Andrew Fitzgibbon, Mat Cook, Toby Sharp, Mark Finocchio,
Richard Moore, Alex Kipman, and Andrew Blake, 
Real-Time Human Pose Recognition in Parts from a Single Depth Image, 
in CVPR, IEEE, June 2011

-----

###  Photo-collage from holiday collection
Given a collection of pictures, the aim is to create a single photo collage that blends the multiple images together in a seamless fashion.

Related papers
 AutoCollage
 by  Carsten Rother, Lucas Bordeaux, Youssef Hamadi, and Andrew Blake
 in ACM Transactions on Graphics (SIGGRAPH), August 2006

Digital Tapestry, 
Carsten Rother, Sanjiv Kumar, Vladimir Kolmogorov, and Andrew Blake, 
in CVPR, 2005



