# 读取图像

OpenCV.js把图像存储为cv.Mat类型. 我们用canvas元素来实现cv.Mat格式与web数据之间的转化．

## Mat类型介绍

Opencv原生编写语言是c，图像的存储结构是C语言的数据结构[IplImage](https://docs.opencv.org/master/d6/d5b/structIplImage.html),这种数据结构在大多数老版本的书籍或者教程中比较常见，但最大的问题是手动内存管理，它建立在用户负责处理内存分配和释放的假设之上。使用Mat您不再需要手动分配其内存并在不需要时立即释放它，Mat基本上是一个包含两个数据部分的类：矩阵头（包含矩阵大小，用于存储的方法，存储矩阵的地址等信息）和指向包含矩阵的矩阵的指针。像素值（取决于选择存储的方法取任何维度）。矩阵头大小是恒定的，但是矩阵本身的大小可能随图像而变化，并且通常大几个数量级。[Mat官方介绍](https://docs.opencv.org/master/d6/d6d/tutorial_mat_the_basic_image_container.html)

## 用ImageData接口实现加载和显示图像

ImageData接口可以展示和设置canvas元素中的像素数据．您可以详情参考canvas文档．  
1.首先，我们由canvas元素创建一个ImageData对象，

```
let canvas = document.getElementById(canvasInputId);
let ctx = canvas.getContext('2d');
let imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
```

然后用cv.matFromImageData创建一个cv.Mat对象:

```
let src = cv.matFromImageData(imgData);
```

_**注意cavas只支持连续存储的-bit RGBA图像，**_[_**cv.Mat**_](https://docs.opencv.org/master/d3/d63/classcv_1_1Mat.html)_**的格式是cv.CV\_8UC4. 这与原生Opencv读取和显示图像时用的BGR格式不同．**_  
2.首先把原图像的数据格式改为cv.CV\_8UC4:

```
let dst = new cv.Mat();
// scale and shift are used to map the data to [0, 255].
src.convertTo(dst, cv.CV_8U, scale, shift);
// *** is GRAY, RGB, or RGBA, according to src.channels() is 1, 3 or 4.
cv.cvtColor(dst, dst, cv.COLOR_***2RGBA);
```

3.然后从目标dst图像中创建新的ImageData对象

```
let imgData = new ImageData(new Uint8ClampedArray(dst.data, dst.cols, dst.rows)
```

4.最终显示图像

```
let canvas = document.getElementById(canvasOutputId);
let ctx = canvas.getContext('2d');
ctx.clearRect(0, 0, canvas.width, canvas.height);
canvas.width = imgData.width;
canvas.height = imgData.height;
ctx.putImageData(imgData, 0, 0);
```

## 用OpenCV.js实现图像加载和显示

OpenCV.js就用上面的方法实现的图像读取和显示  
我们可以用[cv.imread \(imageSource\)](https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56)从函数`canvas`或者`img`标签来读取图像.  
_**Parameters**_

```
imageSource    canvas或img元素或者对应id.
```

_**Returns**_

```
以RGBA顺序存储的mat类型.
```

我们可以用[cv.imshow \(canvasSource, mat\)](https://docs.opencv.org/master/d7/dfc/group__highgui.html#ga453d42fe4cb60e5723281a89973ee563)函数显示.这个函数可能会根据图像的深度改变mat的大小

> 如果mat是8为无符号整数，直接显示  
> 如果是16无符号或者32为整数，所有像素除以256,也就是把\[0,255\_256\]映射为\[0,255\].  
> 如果mat是32为浮点数，则乘以255，即\[0,1\]映射为\[0,255\].

_**Parameters**_

```
canvasSource    canvas元素或id.
mat                要显示的图像.
```

用ImageDate接口实现的可以简化为:

```
let img = cv.imread(imageSource);
cv.imshow(canvasOutput, img);
img.delete();
```

### 完整代码

```
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Hello OPencv.js</title>
    <style>
        .inp{
            display:inline-block;
            margin:10px 20px 0 10px;
            width:300px;
            height:300px;
            border:2px solid black;
            position:relative;
        }
        .caption{
            position:absolute;
            bottom:-25px;
            height:20px;
            margin:auto;
        }
        img{width:300px;height:300px;}
    </style>
</head>
<body>
<h2>Hello OpenCV.js</h2>
<p id="status">Opencv is loading...</p>
<div>
    <div class="inp" style="float:left;">
        <img id="imgSrc" alt="No Image"/>
        <div class="caption"><input type="file" id="fileIn" name="file"></div>
    </div>
    <div class="inp">
        <canvas id="canvasout"></canvas>
        <div class="caption">CanvasOutPut</div>
    </div>
</div>
<script type="text/javascript">
    let img = document.getElementById('imgSrc');
    let inputEle = document.getElementById('fileIn');
    inputEle.addEventListener('change', (e)=>{
                img.src = URL.createObjectURL(e.target.files[0]);
            }, false);
    img.onload = function(){
        let mat = cv.imread(img);
        cv.imshow('canvasout', mat);
    };
    function onOpenCvReady(){
        document.getElementById('status').innerHTML = 'OpenCv.js is ready';
    }
</script>
<script async src="./opencv.js" onload="onOpenCvReady()" type="text/javascript"></script>
</body>
</html>
```

# 可能遇到的错误

１．注意文件目录，opencv.js,opencv\_js.js,opencv\_js.wasm与＊.html必须放在用一个目录中，否则会有跨域访问的问题．  
![](/assets/tree.png)  
２．在加载文件后显示  
![](/assets/bug.png)  
上面这个是在ubuntu16.04中的firefox上的显示信息，在chromeium中显示信息![](/assets/bug2.png)  
比较麻烦的是，chromeium的问题比较多且都是源码加载的问题，这里不考虑了，在火狐中显示的是编译时的错误，但不影响显示．对此，在火狐中直接忽略此问题．这里建议下载chrome浏览器．其他的浏览器我没有尝试，想试试的可以试试．  
３．结果展示  
![](/assets/result.png)

图片必须动态加载，在脚本中把图片加载写入函数，还是直接过程式的写脚本都不行，必须通过事件触发来调用．

