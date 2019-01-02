# OpenCV的简介

## OpenCV

Opencv是Gary Bradski 1999年在Intel发起的．2000发布了第一个发行版．OpenCV现在支持许多计算机视觉和机器学习的算法，支持多种计算机语言，如python,c++ 和Java并且兼容多种平台包括Windows, Linux, OS X, Android, and iOS.对于基于CUDA and OpenCL的高速GPU操作接口仍在积极的开发中．OpenCV.js把OpenCV带到了web平台上，使程序员可以用JavaScript开发.

## OpenCV.js:给JavaScript程序员的OpenCV

Web是最普遍的计算平台，随着HTML5的标准被各个浏览器的支持，web应用现在可以通过video标签渲染视频，通过WebRTC API来扑捉视频流，通过canvas API来得到视频帧的像素．拥有如此多的多媒体资源，web开发者确实需要大量的可用JavaScript实现的图像和视频处理算法来构建新颖的应用．这种需求对于web应用如WebVR,WebAR是必要的．所有这些用例要求计算密集型视觉内核在web上高效的实现．

[Emscripten](http://kripken.github.io/emscripten-site)是LLVM-to-JavaScript编译器. 它用clang把C/C++转化为LLVM bitcode，然后编译为asm.js或者可以直接在浏览器上直接运行的WebAssembly.   
Asm.js是Javascript高度优化的底层的Javascript子集，可以提前编译并在javascript引擎上优化提供几近原生的执行速度．

WebAssembly是一个轻便，大小和加载时间高效的二进制格式，适用于向web的编译．旨在执行速度快如原生版．WebAssembly目前正在作为W3C的标准而设计．  
OpenCV.js 是对Opencv的一部分函数在web平台上的实现，它允许在web应用中嵌入多媒体处理用大量Opencv的视觉函数来优化应用．  
OpenCV.js用Emscripten把OpenCV的函数编译为asm.js或者 WebAssembly 并且提供JavaScript APIs 来调用．以后的视觉库会借着积累webAPI的好处在Web实现如SIMD和多进程处理.

OpenCV.js最初Inter公司捐助由California Irvine \(UCI\)大学Parallel Architectures and Systems小组作为一个研究项目发起．OpenCV.js后来作为Google Summer of Code 2017 program的一部分被提升并整合到Opencv项目中．

***本书使用Opencv3.X版本．***

