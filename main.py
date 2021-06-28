from imageai.Detection import VideoObjectDetection
import os 
import cv2
from time_stamp import get_timestamp
from video_size import get_video_length

# config application settings
dirname = os.getcwd()
output_filename = "AI_overlayed"

input_filename = "failure"
for t1, t2, files in os.walk("input"):
    for file in files:
        input_filename = file
        break
    break

if input_filename == "failure":
    print("No video file found in input folder.")


def end():
    log_file.close()
    print("Scan complete! View output in the local output folder which will contain vehicle-logs and the AI-overlayed video feed.")
    os._exit(1)
def bind(*args):
    result = ""
    for s in args:
        result += str(s) + " "
    result = result[:len(result) - 1]
    print(result)
    return result
def attempt(cmd):
    try:
        exec(cmd)
    except:
        return


output_filename += "_" + str(input_filename)
log_path = os.path.join("output", str(input_filename) + "_log.txt")
input_path = os.path.join(dirname, "input", input_filename)
input_size = get_video_length(input_path)
num_frames_per_second = 1   

attempt('os.remove(' + log_path + ')')
attempt('os.remove("output/" + output_filename)')
log_file = open(log_path, "w+")
log_file.truncate(0)


print("Scanning file from", input_path)

# initialize scan
camera = cv2.VideoCapture(input_path)
detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(dirname, "yolo.h5"))
detector.loadModel()
search_list = ["car", "motorcycle", "bus", "truck", "bicycle", "train"]
custom = detector.CustomObjects(car=True, motorcycle=True, bus=True, truck=True, bicycle=True, train=True)


log_file.write("LOGS:\n\n")

# detection handler
def for_frame(frame_number, output_array, detections, frame):
    seconds = frame_number * num_frames_per_second
    num_matches = 0
    entry_logged = False
    for object in detections:
        if object in search_list:
            num_matches += 1
            indent = "    "
            if not entry_logged:
                log_file.write("--> ")
                entry_logged = True
                indent = ""

            log_file.write(bind(indent, "[" + get_timestamp(seconds) + "]", detections[object], object, "(s)\n")) 
         
    if seconds >= input_size:
        end()

# scan loop with ImageAI
print("Starting scan...this could take a few minutes")
output_path = detector.detectCustomObjectsFromVideo(
    input_file_path=input_path,
    custom_objects = custom,
    output_file_path=os.path.join(dirname, "output", output_filename), 
    frames_per_second=num_frames_per_second, 
    log_progress=True,
    per_frame_function=for_frame,  
    return_detected_frame=True
)

end()


