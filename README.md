# Vehicle-Detection

## Setup
  Download the following libraries in your environment using pip:
  - keras
  - tensorflow
  - imageai
  - opencv
  
  Then create the following folders in the root directory of the project:
  - output
  - input
  
  Lastly, download the Yolo tensorflow model and insert into the root directory of the project.
  
  Download Link: https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5
  
  And your all set!
  
 ## Usage
  1. Paste the input video file to process in the input folder
  2. Run main.py. Progress in terms of frames-processed will be logged along with prelimary logs. 
  
  *Frames processed per second is defaulted to 0, and can be changed by altering the global variable num_frames_per_second
  
  4. Upon script completion message, check the output folder for the overlayed video file and complete logs!
  
  
