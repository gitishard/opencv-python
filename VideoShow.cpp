#include<iostream>
#include<opencv2/core/core.hpp>
#include<opencv2/videoio.hpp>
#include<opencv2/highgui.hpp>
using namespace std;
using namespace cv;
int main(int argc, char* arg[]){
    VideoCapture capture(0);
	namedWindow("VIdeo",1);
    if(!capture.isOpened())
		return -1;
	
	Mat frame;
	for(;;){
		capture >> frame;
		imshow("VIdeo",frame);
		waitKey(1);
			//break;
	}
	
	capture.release();
    return 0;
}
