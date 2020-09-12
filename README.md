# jetson_picamera_record_openCV_gstreamer
Using the Raspberry Pi Camera Module and OpenCV in Jetson Nano to record unique or multiple streams.
OpenCV has to be compiled in the Jetson Nano device before using this project.
Gstreamer is used because the Rasp Camera is not self recognized as a video input in Jetson Nano.
The code "stream_record_unique" saves a single .avi or .mp4 file. Default file name is output, it may be changed in the "writer" section. 
The code "stream_record_multiple" saves endless .avi or .mp4 files, until the proccess is killed. File names are provided by the sistem date and time, to avoid overwriting video files when the script is used later. 

The video file length is configurable in seconds. The resolution is fully configurable ("H" and "W" in cv2.VideoCapture).
Default framerate is 5 FPS. In order to change, the framerate has to be the same in the "VideoCapture" and "VideoWriter" sections. Otherwise, the output file becomes too fast / too slow.

Using PM2 you may start this script in system boot, creating an automated solution.
