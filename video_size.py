import cv2
  
def get_video_length(file_path):
    # create video capture object
    data = cv2.VideoCapture(file_path)
    
    # count the number of frames
    frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = int(data.get(cv2.CAP_PROP_FPS))
    
    # calculate dusration of the video
    return int(frames / fps)

