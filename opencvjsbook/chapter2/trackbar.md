#目标
用Input Range创建trackbar（轨迹条）.
#样例
我们把两个图片绑定到一起，通过轨迹条来改变对应权重．
首先创建三个canvas元素，一个用来输出，两个用来输入.
```
let src1 = cv.imread('canvasInput1');
let src2 = cv.imread('canvasInput2');
```
然后，我们用HTML的Input Range 对象来实现trackbar
![](/assets/Trackbar_Tutorial_Range.png)
***注意，在IE9以及早期版本中不支持`<input>`标签的type="range"属性***
你可以用document.createElement()方法创建待type="range"属性`<input>`标签:
```
let x = document.createElement('INPUT');
x.setAttribute('type', 'range');
```
您可以通过getElementById()函数获取type="range"的`<input>`标签
```
let x = document.getElementById('myRange');
```
一个trackbar需要一个名字，最大值，最小值，默认值，变化步长和一个在trackerbar值改变时处理的回调函数． 回调函数的默认参数是trackerbar的位置，当然也可以加上一个文本显示当前值．

```
Weight:　<input type="range" id="trackbar" value="50" min="0" max="100" step="1" oninput="callback()">
```
我们可以通过回调函数中trackerbar中的值来融合两幅图片．

```
let weightValue = document.getElementById('weightValue');
let trackbar = document.getElementById('trackbar');
weightValue.setAttribute('value', trackbar.value);
let alpha = trackbar.value/trackbar.max;
let beta = ( 1.0 - alpha );
let src1 = cv.imread('canvasInput1');
let src2 = cv.imread('canvasInput2');
let dst = new cv.Mat();
cv.addWeighted( src1, alpha, src2, beta, 0.0, dst, -1);
cv.imshow('canvasOutput', dst);
dst.delete();
src1.delete();
src2.delete();
```
#完整代码