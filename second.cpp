#include<opencv2/core.hpp>
#include<opencv2/imgcodecs.hpp>
#include<opencv2/imgproc.hpp>
#include<opencv2/highgui.hpp>

#include <iostream>
#include<fstream>
#include <string>


using namespace cv;
using namespace std;

int main(){
    ifstream myfile ("/home/neha/Documents/imagepathlistph.txt");
    for (int k = 0; k<159; k++){
        char temp[40];
        char* temp2 = temp;
        char x;
        int i = 0;
        while(1){
            myfile.get(x);
            if(x == '\n') break;
            else{
                *temp2 = x;
                i++;
                temp2++;
            }
        }
        int n = i;
        char imageName[n+1];
        char* temp1 = temp;
        char* name = imageName;
        for (int j =0; j < n; j++){
              *name = *temp1;
              if(j == n-1) break;
              name++;
              temp1++;
        }
        imageName[n]='\0';

        Mat image;
        image = imread( imageName, IMREAD_COLOR ); // Read the file
        if( image.empty() )                      // Check for invalid input
        {
             cout <<  "Could not open or find the image" << std::endl ;
        }
        else{
            uchar* rowPtr = image.ptr<uchar>(375);
            int B = rowPtr[(3*775) + 0];
            cout << B << endl;
        } 
    }

    return 0;
}


