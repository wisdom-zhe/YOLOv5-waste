import RPi.GPIO as GPIO
from time import sleep
import cv2

GPIO.setmode(GPIO.BCM)  
GPIO.setwarnings(False)

# mock 
cls_list=['A','B','C','D','B','C','D']


# 分类角度
cls_angle={
    "A": 10,
    "B": 50,
    "C": 100,
    "D": 165,
} 

for item in cls_list:
    if item=='A':
        angle=cls_angle['A']
    elif item=='B':
        angle=cls_angle['B'] 
    elif item=='C':
        angle=cls_angle['C'] 
    else:
        angle=cls_angle['D'] 


def get_angle(cls_name):
    # 分类角度
    cls_angle={
        "A": 10,
        "B": 50,
        "C": 100,
        "D": 165,
    } 

    if cls_name=='A':
        return cls_angle['A']
    elif cls_name=='B':
        return cls_angle['B'] 
    elif cls_name=='C':
        return cls_angle['C'] 
    else:
        return cls_angle['D'] 


# servo_pin 舵机信号线接树莓派GPIO17
def complex_change(servo_pin):   
    GPIO.setup(servo_pin, GPIO.OUT, initial=False)
    p = GPIO.PWM(servo_pin, 50)    # 初始频率为50HZ
    p.start(angleToDutyCycle(90))  # 舵机初始化角度为90
    sleep(0.5)
    p.ChangeDutyCycle(0)   # 清空当前占空比，使舵机停止抖动
    
    return p

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

 
# 旋转角度转换到PWM占空比
def angleToDutyCycle(angle):
    return 2.5 + angle / 180.0 * 10

 
if __name__ == '__main__':
    # 开启电源时，设备处于待机模式，实现播放垃圾分类宣传视频
    # recycle_video_path = '/home/pi/yolov5-waste/data/video/recyclable_video.mp4'
    recycle_video_path = '/home/pi/yolov5-waste/data/video/detect_test.mp4'
    paly_video(recycle_video_path)

    for item in cls_list:

        # 获取类别角度
        angle=get_angle(item)

        # 水平转动
        p=complex_change(17)
        p.ChangeDutyCycle(angleToDutyCycle(angle))

        # 垂直方向回正
        p=complex_change(18)
        p.ChangeDutyCycle(angleToDutyCycle(0))

        sleep(0.5)
        p.ChangeDutyCycle(0) # 清空当前占空比，使舵机停止抖动    