import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# servo_pin 舵机信号线接树莓派GPIO17
def complex_change(servo_pin):
	GPIO.setup(servo_pin, GPIO.OUT, initial = False)
	p = GPIO.PWM(servo_pin, 50)  # 初始频率为50HZ
	p.start(angleToDutyCycle(90))  # 舵机初始化角度为90
	sleep(0.5)
	p.ChangeDutyCycle(0)  # 清空当前占空比，使舵机停止抖动

	return p


# 旋转角度转换到PWM占空比
def angleToDutyCycle(angle):
	return 2.5 + angle / 180.0 * 10


if __name__ == '__main__':
	print('当前为90度')
	while True:
		angle = int(input('旋转度数：'))
		# 水平转动
		p = complex_change(17)

		p.ChangeDutyCycle(angleToDutyCycle(angle))

		# 垂直方向回正
		p = complex_change(18)
		p.ChangeDutyCycle(angleToDutyCycle(0))

		sleep(0.1)
		p.ChangeDutyCycle(0)  # 清空当前占空比，使舵机停止抖动