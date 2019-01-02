#简单使用例子
本节你讲了解如何在web页面使用Opencv.js
####创建一个页面
```
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Hello OpenCV.js</title>
</head>
<body>
<h2>Hello OpenCV.js</h2>
<div>
  <div class="inputoutput">
    <img id="imageSrc" alt="No Image" />
    <div class="caption">imageSrc <input type="file" id="fileInput" name="file" /></div>
  </div>
</div>
<script type="text/javascript">
let imgElement = document.getElementById("imageSrc")
let inputElement = document.getElementById("fileInput");
inputElement.addEventListener("change", (e) => {
  imgElement.src = URL.createObjectURL(e.target.files[0]);
}, false);
</script>
</body>
</html>
```
赋值上面的代码到index.html文件中，用浏览器打开即可．
#引入OpenCV.js
把页面`<script>`标签的src属性的URL改为你自己opencv.js文件的位置
***Note
本教程中opencv.js和index.html在一个目录中. `PS.在我的使用中分开后会有跨区问题`***
一个同步加载的例子:
`<script src="opencv.js" type="text/javascript"></script>`
同样你可以用异步加载在`<script>`标签中用async属性， 在onload属性上设置回调函数提醒Opencvjs已经加载好了．
`<script async src="opencv.js" onload="onOpenCvReady();" type="text/javascript"></script>`
#Use OpenCV.js
一旦opencv.js加载好了，就可以通过cv对象获取函数和OpenCV对象
举个例子，你可以通过cv.imread函数读取一个图像来创建一个cv.Mat对象
注意，在异步加载中，需要报cv.Mat的创建放在加载回调函数中
```
imgElement.onload = function() {
  let mat = cv.imread(imgElement);
}
```
许多OpenCV函数可以处理cv.Mat.详细可以参考Image Processing．在本节中只是展示如何创建cv.Mat,在此之前你需要添加canvas元素到页面中
`<canvas id="outputCanvas"></canvas>`
你可以用cv.imshow把cv.Mat展示在canvas上.
`cv.imshow(mat, "outputCanvas")`
#完整代码
```
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Hello OpenCV.js</title>
</head>
<body>
<h2>Hello OpenCV.js</h2>
<p id="status">OpenCV.js is loading...</p>
<div>
  <div class="inputoutput">
    <img id="imageSrc" alt="No Image" />
    <div class="caption">imageSrc <input type="file" id="fileInput" name="file" /></div>
  </div>
  <div class="inputoutput">
    <canvas id="canvasOutput" ></canvas>
    <div class="caption">canvasOutput</div>
  </div>
</div>
<script type="text/javascript">
let imgElement = document.getElementById('imageSrc');
let inputElement = document.getElementById('fileInput');
inputElement.addEventListener('change', (e) => {
  imgElement.src = URL.createObjectURL(e.target.files[0]);
}, false);
imgElement.onload = function() {
  let mat = cv.imread(imgElement);
  cv.imshow('canvasOutput', mat);
  mat.delete();
};
function onOpenCvReady() {
  document.getElementById('status').innerHTML = 'OpenCV.js is ready.';
}
</script>
<script async src="opencv.js" onload="onOpenCvReady();" type="text/javascript"></script>
</body>
</html>
```

***注意，谨记在使用后删除cv.Mat来清理内存***,详见[Memory management of Emscripten](https://kripken.github.io/emscripten-site/docs/porting/connecting_cpp_and_javascript/embind.html#memory-management).