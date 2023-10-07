<<<<<<< HEAD
<<<<<<< HEAD
# [-----------------------------参考博文------------------------](https://blog.csdn.net/qq_44231797/article/details/133270195)
# 前言

> 型号：树莓派4B
>
> 环境：Python3.7
>
> 远程控制软件：VNC Viewer(远程控制时，需要保证都处于同一个局域网中)

# 1、部署过程

## 1.1、下载YOLOv5

1. 先去YOLOv5官网下载文件代码，然后在树莓派新建一个YOLOv5文件夹并把下载好的文件传输到里面
2. 这里采用[YOLOv5-6.0](https://github.com/ultralytics/yolov5/tree/v6.0)

![在这里插入图片描述](https://img-blog.csdnimg.cn/775f5380808e4b7dac70bba996bbacdd.png#center)


3.然后安装依赖：

```vim
sudo apt-get install libopenblas-dev libblas-dev m4 cmake cython python3-dev python3-yaml python3-setuptools python3-wheel python3-pillow python3-numpy
```

## 1.2、安装opencv、pytorch和numpy

### 1.2.1、安装opencv

```routeros
sudo apt-get install python3-opencv
```

`建议是否安装成功：`
![在这里插入图片描述](https://img-blog.csdnimg.cn/f1146dedd35148d08f0cc7f7314aa7d4.png)



### 1.2.2、安装pytorch&numpy

**首先查看Python版本对应哪个Torch版本和torchvision版本**
![在这里插入图片描述](https://img-blog.csdnimg.cn/062d6054c086427d94660f838eaaf311.png)





1. [whl文件官网](https://download.pytorch.org/whl/torch_stable.html)
2. [numpy文件官网](https://pypi.tuna.tsinghua.edu.cn/simple/numpy/)
3. [本文用到的torch和torchvision版本](https://download.csdn.net/download/qq_44231797/88372064)

> 找到对应的torch和torchvision版本后，下载到树莓派中并安装

```sh
# 这里采用torch1.6.0的版本依旧能运行，所以也不一定得按版本对照来，不过能按照版本来就按照版本来
pip3 install torch-1.6.0a0+b31f58d-cp37-cp37m-linux_armv7l.whl

pip3 install torchvision-0.8.0a0+10d5a55-cp37-cp37m-linux_armv7l.whl

pip3 install numpy==1.18.5 -i https://mirrors.aliyun.com/pypi/simple/
```

## 1.3、YOLOv5安装

> 去到YOLOv5项目，找到requirements.txt把 numpy、opencv-python、torch和torchvision注释

![在这里插入图片描述](https://img-blog.csdnimg.cn/1f7f56562a754b0baf8e320e8088f729.png#pic_center)


```sh
cd /home/pi/yolov5-waste  #那个pi是我的用户名，注意要填自己的用户名
sudo nano requirements.txt
# 按ctrl+o并回车完成写入，按ctrl+x退出。

# YOLOv5其他环境一键安装
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

> 安装完成图

![在这里插入图片描述](https://img-blog.csdnimg.cn/aa2fc0749a7e439ab6ccc035d7b46cb6.png#pic_center)


## 1.4、运行detect.py

```sh
cd /home/pi/yolov5-waste  #那个pi是我的用户名，注意要填自己的用户名
# 确保根目录有yolov5s.pt
python3 detect.py    # 成功检测！
```



# 2、开机自动运行脚本

在终端上输入：

```sh
sudo vi /etc/rc.local  
```

就会出现一个文本编辑器，在文本内容的exit 0 上面添加一行：

```shell
python3 /home/pi/picam.py  
```

然后保存更改, 重启树莓派：

```sh
# 重启树莓派方式1：
sudo reboot  
# 重启树莓派方式2：
sudo shutdown -r now
```



# 3、遇到的问题

## 3.1、pip3下载缓慢

`如果你没有换成国内源话，下载速度有时候会很慢，甚至直接报错 Read timed out`

**解决办法：** 使用国内源去下载

### 3.1.1、国内源

1. 阿里云：`https://mirrors.aliyun.com/pypi/simple/`
2. 清华：`https://pypi.tuna.tsinghua.edu.cn/simple`
3. 中国科技大学 `https://pypi.mirrors.ustc.edu.cn/simple/`
4. 华中理工大学：`https://pypi.hustunique.com/`
5. 山东理工大学：`https://pypi.sdutlinux.org/`
6. 豆瓣：`https://pypi.douban.com/simple/`

### 3.1.2、单次使用

1. pip install -r requirements.txt -i https://mirrors.aliyun.com/[pypi](https://so.csdn.net/so/search?q=pypi&spm=1001.2101.3001.7020)/simple/
2. pip install 单个包名 -i https://mirrors.aliyun.com/pypi/simple/



### 3.1.3、永久修改

`设置`

```python
$ pip3 config set global.index-url http://mirrors.aliyun.com/pypi/simple/
Writing to /root/.config/pip/pip.conf

$ pip3 config set install.trusted-host mirrors.aliyun.com
Writing to /root/.config/pip/pip.conf
```

`查看效果`

```python
$ cat /root/.config/pip/pip.conf
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host = mirrors.aliyun.com

$ pip config list
global.index-url='http://mirrors.aliyun.com/pypi/simple/'
install.trusted-host='mirrors.aliyun.com'
```

`删除设置`

```python
pip config unset global.index-url 

Writing to /root/.config/pip/pip.conf

cat /root/.config/pip/pip.conf

[install]
trusted-host = mirrors.aliyun.com
```



## 3.2、手动安装whl文件失败

> 将下载好的Twisted-18.4.0-cp36-cp36m-win_amd64.whl放在E盘下面

**包名中间的cp36是python3.6的意思，amd64是python的位数。**

在安装python的whl包时，出现了以下问题：

![在这里插入图片描述](https://img-blog.csdnimg.cn/b8cc7f6bf1e342f7bc53a491bead0d5b.png)


**解决办法：** 查看当前环境支持包的类型

```python
# 进入python，输入以下代码，查看pip支持的类型
import pip._internal
print(pip._internal.pep425tags.get_supported())
运行结果：
[('cp38', 'cp38m', 'win32'), ('cp38', 'none', 'win32'), ('py3', 'none', 'win32'), ('cp38', 'none', 'any'), ('cp3', 'none', 'any'), ('py38', 'none', 'any'), ('py3', 'none', 'any'), ('py37', 'none', 'any'), ('py36', 'none', 'any'), ('py35', 'none', 'any'), ('py34', 'none', 'any'), ('py33', 'none', 'any'), ('py32', 'none', 'any'), ('py31', 'none', 'any'), ('py30', 'none', 'any')]
```

可以看到，我们下载的whl包，命名不符合python3.8.0的安装支持，按照('cp38', 'cp38m', 'win32')，将其命名为：**Twisted-20.3.0-cp38-cp38m-win32.whl** 即可。



## 3.3、树莓派无法检测到摄像头

### 3.3.1、判断是否正确加载摄像头

`方式1：`检测摄像头

```sh
vcgencmd get_camera 
 # 输出supported=1 说明支持外设摄像头
# supported=1 detected=0.  
```

`方式2：`检测video设备

```sh
ls /dev/video*
#正确连接时，第一个设备会是video0 
#/dev/video0  /dev/video1  /dev/video10  /dev/video11  /dev/video12
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/753df5365be64ce2873563d19ddb98bb.png)


### 3.3.2、开启摄像头

**方法一：** 系统开启摄像头

```sh
sudo raspi-config
```

**将光标移动到摄像头选项（ Interface Options）处，并选择启用（Enable）。**

![在这里插入图片描述](https://img-blog.csdnimg.cn/688f9d18261c4d8e80f1e7352e75e1b2.png)




**将光标移动到摄像头选项（Camera option）处，并选择启用（Enable）。**在退出 raspi-config 时会要求您**重新启动**。启用选项是为了确保重启后 GPU 固件能够正确运行（包括摄像头驱动和调节电路），并且 GPU 从主内存划分到了足够的内存使摄像头能够正确运行。

![在这里插入图片描述](https://img-blog.csdnimg.cn/8a8b218a119a4e69a888a841dc55ebc2.png)


**方法二：** 加载摄像头驱动

```sh
sudo nano /etc/modules  # 在编写的文件后面加上 bcm2835-v4l2
# 按ctrl+o并回车完成写入，按ctrl+x退出。
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/e76f92ad417f4920867b7772efe0411f.png)




# 参考文章

 1. [YOLOv5s网络模型讲解(一看就会)](https://blog.csdn.net/qq_44231797/article/details/129408786)

 2. [生活垃圾数据集（YOLO版）](https://blog.csdn.net/qq_44231797/article/details/133203722)

 3. [YOLOv5如何训练自己的数据集](https://blog.csdn.net/qq_44231797/article/details/133206747)

 4. [双向控制舵机（树莓派版）](https://blog.csdn.net/qq_44231797/article/details/132955718)
    

=======
# YOLOv5-waste
>>>>>>> 6a2ffb91fd05bb26c9818105ed8786cc87c8e450
=======
# YOLOv5-waste
>>>>>>> 6a2ffb91fd05bb26c9818105ed8786cc87c8e450
