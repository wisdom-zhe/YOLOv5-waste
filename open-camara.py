import cv2


def CatchUsbVideo(window_name, camera_idx):
	cv2.namedWindow(window_name)  # 写入打开时视频框的名称
	# 捕捉摄像头
	cap = cv2.VideoCapture(camera_idx)  # camera_idx 的参数是0代表是打开笔记本的内置摄像头，也可以写上自己录制的视频路径
	while cap.isOpened():  # 判断摄像头是否打开，打开的话就是返回的是True
		# 读取图像
		ok, frame = cap.read()  # 读取一帧图像，该方法返回两个参数，ok true 成功 flase失败，frame一帧的图像，是个三维矩阵，当输入的是一个是视频文件，读完ok==flase
		if not ok:  # 如果读取帧数不是正确的则ok就是Flase则该语句就会执行
			break

		# 显示图像
		cv2.imshow(window_name, frame)  # 显示视频到窗口
		c = cv2.waitKey(10)
		if c & 0xFF == ord('q'):  # 键盘按q退出视频
			break

	cap.release()  # 释放摄像头
	cv2.destroyAllWindows()  # 销毁所有窗口


if __name__ == '__main__':
	CatchUsbVideo("camera", 0)