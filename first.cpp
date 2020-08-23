#include<opencv2/core.hpp>
#include<opencv2/imgcodecs.hpp>
#include<opencv2/imgproc.hpp>
#include<opencv2/highgui.hpp>

#include <iostream>
#include<fstream>
#include <string>


using namespace cv;
using namespace std;

int main()
{
    ifstream myfile ("/home/neha/Documents/imagepathlistph.txt");
    
    char imageName[40];
    int i = 0;
    char x;
    
    while(i<40){
         myfile.get(x);
         if(x=='\n') break;
         else {
              imageName[i] = x;
              i++;
         }
    }
    
    cout << imageName << endl;
  
    Mat image;
    image = imread( imageName, IMREAD_COLOR ); // Read the file
    if( image.empty() )                      // Check for invalid input
    {
        cout <<  "Could not open or find the image" << std::endl ;
        return -1;
    } 

    rectangle(image, Point(725,325), Point(825,425), Scalar(0,0,0), 4 , 8);  

    namedWindow( "Display window", WINDOW_NORMAL ); // Create a window for display.
    imshow( "Display window", image );                // Show our image inside it.
    waitKey(0); // Wait for a keystroke in the window

    int rows = image.rows;
    int cols = image.cols;
    cout << rows << endl << cols << endl ;

    uchar* rowPtr = image.ptr<uchar>(375);
    int B = rowPtr[(3*775) + 0];
    int G = rowPtr[(3*775) + 1];
    int R = rowPtr[(3*775) + 2];
    cout << B << endl << G << endl << R << endl;

    return 0;
}
