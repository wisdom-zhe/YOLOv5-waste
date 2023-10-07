import cv2
# 播放视频
def paly_video(recycle_video_path):
    cap = cv2.VideoCapture(recycle_video_path)
    while (cap.isOpened()):
        ret, frame = cap.read()
        if frame is not None:
            cv2.imshow('image', frame)
        k = cv2.waitKey(20)
        # q键退出
        if not ret:
            break
    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    # 开启电源时，设备处于待机模式，实现播放垃圾分类宣传视频
    # recycle_video_path='/home/pi/yolov5-waste/data/video/recyclable_video.mp4'
    recycle_video_path='/home/pi/yolov5-waste/data/video/2.mp4'
    # recycle_video_path = '/home/pi/yolov5-waste/data/video/detect_test.mp4'
    paly_video(str(recycle_video_path))
