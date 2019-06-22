超大分辨率图片读取模块：openslide

**一共分为两步：**

**1.** 先安装openslide二进制文件，位于http://openslide.org/download/；
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190620102600621.png)
下载64-bit后解压，文件夹中有一个bin目录，记下这bin目录的地址。

**2.** 执行pip install openslide-python
进入该openslide的目录，找到lowlevel.py文件，打开，在前面加入：

```
import os
os.environ['PATH'] = "F:/openslide-win64-20171122/bin/" + ";" + os.environ['PATH']
```

使得该文件可以找到步骤1中得到的bin目录文件。
运行python lowlevel.py不报错则成功。

**后续：** 当图片中得像素点达到PIL中设定得阈值后，将会报错，所以需要修改一下阈值。当然，内存大小才是硬伤。

```
from PIL import Image
Image.MAX_IMAGE_PIXELS = 3000000000
```

## 使用

```
import openslide
import numpy
import matplotlib.pyplot as plt

train_dir = "./"
slide = openslide.open_slide(train_dir + 'image_1_label.png')
ds = slide.level_downsamples
size = 900
# 这里选取了图片中x=0，y=45100得开始位置，图片大小为(size,size)
tile = numpy.array(slide.read_region((0,45100), 0, (size,size) ))

## 修改值为1得部分为200，为了清晰显示mask。(非重点)
# tile[tile==1]=200

# 修改显示窗口得大小
plt.figure(figsize=(18,9))

plt.imshow(tile)
plt.axis('off')
plt.show()
```

关注微信公众号，持续更新相关内容。

**公众号：知识交点**
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190621124554523.png)
