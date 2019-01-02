#Important
首先说说，其实没有必要下载这个编译器，它最终的结果是要得到opencv.js和opencvjs.wasm文件，各两个文件在使用时必须放在同一个目录中．因为OpenCV是用C++编写的，而这个编译器就是把c++的代码转化为javascript,所以没有必要安装这个编译器和python,我会把我已经编译好的文件分享出来．能直接用现成文件就用现成文件，因为这个安装和编译过程出错太多了．[下载OpneCVJ文件](https://download.csdn.net/download/sb985/10608997)
#安装Emscripten
[Emscripten](https://github.com/kripken/emscripten)是LLVM-to-JavaScript编译器.我们将用Emscripten编译OpenCV.js.按照[Emscripten SDK](https://kripken.github.io/emscripten-site/docs/getting_started/downloads.html)的介绍安装Emscripten
For example:
>./emsdk update
>./emsdk install latest
>./emsdk activate latest

***注意
要编译成WebAssembly,你得用emsdk安装并激活[Binaryen](https://github.com/WebAssembly/binaryen)． 更多细节请参考[Developer's Guide](http://webassembly.org/getting-started/developers-guide/)***

安装完后请确保EMSCRIPTEN正确安装.
For example:
>source ./emsdk_env.sh
>echo ${EMSCRIPTEN}

#获取OpenCV源码
你可以使用最新版的OpneCV，到官网下载zip包并解压
或者从[git仓库抓取](https://github.com/opencv/opencv.git)
For example:
`git clone https://github.com/opencv/opencv.git`
#源码构建OpenCV.js
执行pytohn脚本构建opencv.js.
例如，创建到build_js目录(提前创建此目录)
```
cd opencv
python ./platforms/js/build_js.py　 build_js
```
***注意
这个要求你的开发环境已经安装了python和cmake.
这个脚本默认构建为asm.js版本. 要想构建为WebAssembly版本追加参数--build_wasm.***

例如, 构建 wasm 版本到build_wasm目录:
`python ./platforms/js/build_js.py build_wasm --build_wasm`
如下是我的博客，关于编译和安装过程和期间遇到的错误[MyBlog](https://blog.csdn.net/sb985/article/details/81713088)