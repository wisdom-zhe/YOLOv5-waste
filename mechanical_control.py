import RPi.GPIO as GPIO
from time import sleep
 

GPIO.setmode(GPIO.BCM)  
GPIO.setwarnings(False)


# 获取角度
def get_angle(cls_name):
    # 分类角度
    cls_angle={
        'recyclable': 10,
        'hazardous': 90,
        'kitchen': 180,
        'other': 180,
    } 

    if cls_name=='recyclable':
        return cls_angle['recyclable']
    elif cls_name=='hazardous':
        return cls_angle['hazardous']
    elif cls_name=='kitchen':
        return cls_angle['kitchen']
    else:
        return cls_angle['other']


# servo_pin 舵机信号线接树莓派GPIO17
def complex_change(servo_pin):   
    GPIO.setup(servo_pin, GPIO.OUT, initial=False)
    p = GPIO.PWM(servo_pin, 50)    # 初始频率为50HZ
    # p.start(angleToDutyCycle(90))  # 舵机初始化角度为90
    p.start(angleToDutyCycle(80))  # 贺哥舵机初始化角度为90
    sleep(0.5)
    p.ChangeDutyCycle(0)   # 清空当前占空比，使舵机停止抖动
    
    return p


 
# 旋转角度转换到PWM占空比
def angleToDutyCycle(angle):
    return 2.5 + angle / 180.0 * 10

# 完成分类投放动作
def throw_waste_to_bucket(cls_name):
    # 获取类别角度
    angle = get_angle(cls_name)
    # 水平转动
    p = complex_change(17)
    p.ChangeDutyCycle(angleToDutyCycle(angle))

    # 垂直方向回正
    p = complex_change(18)
    p.ChangeDutyCycle(angleToDutyCycle(0))

    sleep(0.5)
    p.ChangeDutyCycle(0)  # 清空当前占空比，使舵机停止抖动