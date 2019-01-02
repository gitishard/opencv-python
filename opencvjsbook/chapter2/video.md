# 原生Canvas API处理视频

#### 通过摄像头捕获视频流

在OpenCV.js中我们用WebRTC和canvas元素实现获取视频流．我们尝试用内置摄像头或者外接摄像头来获取视频并且灰度化然后显示出来．  
首先需要在页面中加入一个`<video>`,用来显示获取到的视频信息，两个`<canvas>`,一个用来一帧一帧的把视频转化为ImageDate数据格式，一个用来显示处理后的视频．  
首先获取视频流．

```
let video = document.getElementById("videoInput"); // video is the id of video tag
navigator.mediaDevices.getUserMedia({ video: true, audio: false })
    .then(function(stream) {
        video.srcObject = stream;
        video.play();
    })
    .catch(function(err) {
        console.log("An error occurred! " + err);
    });
```

#### 播放视频

现在浏览器获取到了视频流，我们可以用canvas的API，CanvasRenderingContext2D.drawImage\(\)放法来把是视频绘制到canvas上．我们可以用[Getting Started with Images](../images.md)节介绍的方法来读取和显示canvas中的视频．在播放视频时，cv.imshow\(\)每延迟数豪秒执行一次，所以建议使用setTimeout\(\)函数.如果视频是30fps,延迟时间　　应该是\(1000/30 - processing\_time\).

```
let canvasFrame = document.getElementById("canvasFrame"); // canvasFrame is the id of <canvas>
let context = canvasFrame.getContext("2d");
let src = new cv.Mat(height, width, cv.CV_8UC4);
let dst = new cv.Mat(height, width, cv.CV_8UC1);
const FPS = 30;
function processVideo() {
    let begin = Date.now();
    context.drawImage(video, 0, 0, width, height);
    src.data.set(context.getImageData(0, 0, width, height).data);
    cv.cvtColor(src, dst, cv.COLOR_RGBA2GRAY);
    cv.imshow("canvasOutput", dst); // canvasOutput is the id of another <canvas>;
    // schedule next one.
    let delay = 1000/FPS - (Date.now() - begin);
    setTimeout(processVideo, delay);
}
// schedule first one.
setTimeout(processVideo, 0);
```

# 用OpenCV.js的API来获取视频

OpenCV.js用`cv.VideoCapture (videoSource)`封装了上述方法．你不必手动加一个隐藏的canvas.

```
参数
videoSource    video元素或者id.
返回值
cv.VideoCapture 实例
```

用`read(image)`获取视频的一帧.由于显示原因，应该把图像构建为cv.CV\_8UC4类型且与视频同大小．

```
参数
image    cv.CV_8UC4类型的图像且与视频同大小
```

之前的代码可以简化为：

```
let src = new cv.Mat(height, width, cv.CV_8UC4);
let dst = new cv.Mat(height, width, cv.CV_8UC1);
let cap = new cv.VideoCapture(videoSource);
const FPS = 30;
function processVideo() {
    let begin = Date.now();
    cap.read(src);
    cv.cvtColor(src, dst, cv.COLOR_RGBA2GRAY);
    cv.imshow("canvasOutput", dst);
    // schedule next one.
    let delay = 1000/FPS - (Date.now() - begin);
    setTimeout(processVideo, delay);
}
// schedule first one.
setTimeout(processVideo, 0);
```

# 完整代码



