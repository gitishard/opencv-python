#图像的一些基础操作
##获取图像的属性
图像属性包括行，列，大小，深度，通道数，图像数据类型
```
let src = cv.imread("canvasInput");
console.log('image width: ' + src.cols + '\n' +
            'image height: ' + src.rows + '\n' +
            'image size: ' + src.size().width + '*' +                                                                          src.size().height + '\n' +
            'image depth: ' + src.depth() + '\n' +
            'image channels ' + src.channels() + '\n' +
            'image type: ' + src.type() + '\n');
```
*Note*
src.type()函数非常重要，在Opencv.js调试中，有大量的错误是由于数据类型错误引起的．

##如何创建Mat类型
####构造函数
```
// 1.默认构造函数
let mat = new cv.Mat();
// 2. 二维数组的大小和类型
let mat = new cv.Mat(size, type);
// 3. 二维数组行，列，类型
let mat = new cv.Mat(rows, cols, type);
// 4. 二维数组行，列，类型，及数组的默认值
let mat = new cv.Mat(rows, cols, type, new cv.Scalar());
```
####静态函数
```
// 1. 创建一个Mat，数值全是０
let mat = cv.Mat.zeros(rows, cols, type);
// 2. 创建一个Mat，数值全是１
let mat = cv.Mat.ones(rows, cols, type);
// 3. 创建一个Mat，是单位矩阵
let mat = cv.Mat.eye(rows, cols, type);
```
####工厂方法
```
// 1. 用JS的Array对象创建MAT数组
// For example: let mat = cv.matFromArray(2, 2, cv.CV_8UC1, [1, 2, 3, 4]);
let mat = cv.matFromArray(rows, cols, type, array);
// 2.用imgData创建mat
let ctx = canvas.getContext("2d");
let imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
let mat = cv.matFromImageData(imgData);
```
##拷贝Mat
```
// 1. Clone
let dst = src.clone();
// 2. CopyTo(only entries indicated in the mask are copied)
src.copyTo(dst, mask);
```
##转化Mat的类型
*convertTo(m, rtype, alpha = 1, beta = 0)*
```
参数
m	输出数组，如果数组大小或者类型不对应，会有相应的更改
rtype	确定输出数组的类型，或者深度(与输入图像的通道数相同)，如果此数是负的，输出矩阵的类型与输入的类型相同
alpha	可选的，规格因素.
beta	可选的，加在alpha上

src.convertTo(dst, rtype);
```
##使用MatVector
```
let mat = new cv.Mat();
// Initialise a MatVector
let matVec = new cv.MatVector();
// Push a Mat back into MatVector
matVec.push_back(mat);
// Get a Mat fom MatVector
let cnt = matVec.get(0);

mat.delete(); 
matVec.delete(); 
cnt.delete();
```
##数据类型
|Data Properties|C++ Type|JavaScript Typed Array|Mat Type|
|--|--|--|--|
|data|uchar|Uint8Array|CV_8U|
|data8S|char|Int8Array|CV_8S|
|data16U|	ushort|	Uint16Array	|CV_16U|
|data16S|	short	|Int16Array	|CV_16S|
|data32S|	int	|Int32Array	|CV_32S|
|data32F|	float	|Float32Array	|CV_32F|
|data64F|	double	|Float64Array	|CV_64F|
####1. data
```
let row = 3, col = 4;
let src = cv.imread("canvasInput");
if (src.isContinuous()) {
    let R = src.data[row * src.cols * src.channels() + col * src.channels()];
    let G = src.data[row * src.cols * src.channels() + col * src.channels() + 1];
    let B = src.data[row * src.cols * src.channels() + col * src.channels() + 2];
    let A = src.data[row * src.cols * src.channels() + col * src.channels() + 3];
}
```
####2. at
|Mat Type|At Manipulation|
|-|-|
|CV_8U|	ucharAt
|CV_8S|	charAt
|CV_16U|ushortAt|
|CV_16S|shortAt|
|CV_32S|intAt|
|CV_32F|floatAt|
|CV_64F|doubleAt|
```
let row = 3, col = 4;
let src = cv.imread("canvasInput");
let R = src.ucharAt(row, col * src.channels());
let G = src.ucharAt(row, col * src.channels() + 1);
let B = src.ucharAt(row, col * src.channels() + 2);
let A = src.ucharAt(row, col * src.channels() + 3);
```
####3. ptr
|Mat Type|Ptr Manipulation|JavaScript Typed Array|
|-|-|-|
|CV_8U|	ucharPtr|Uint8Array|
|CV_8S|	charPtr|Int8Array|
|CV_16U|ushortPtr|Uint16Array|
|CV_16S|shortPtr|Int16Array|
|CV_32S|intPtr|	Int32Array|
|CV_32F|floatPtr|Float32Array|
|CV_64F|doublePtr|Float64Array|
```
let row = 3, col = 4;
let src = cv.imread("canvasInput");
let pixel = src.ucharPtr(row, col);
let R = pixel[0];
let G = pixel[1];
let B = pixel[2];
let A = pixel[3];
```
mat.ucharPtr(k)获取k行.
mat.ucharPtr(i, j)获取i行j列

##ROI(Region of Interest)
有时你得在图像的特定区域操作，比如要找眼睛，就得先找到脸，在脸中找眼睛，这样可以提高精确度和效率
```
function:*roi (rect)*

参数
rect	rectangle Region of Interest.
```

