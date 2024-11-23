#include <iostream>
#include <opencv2/opencv.hpp>
#include "include/fuzzyfication.hpp"

int main(){

    cv::Mat image = cv::imread("../images/google_maps_mockup.png", cv::IMREAD_COLOR);

    // Check if the image was loaded successfully
    if (image.empty()) {
        std::cerr << "Error: Could not load image!" << std::endl;
        return -1;
    }

    cv::imshow("Original image", image);
    auto fuzzyfied = blur_image(image, 5);

    cv::imwrite("../images/google_maps_mockup_cpp_fuzzyfied.png", fuzzyfied);

    cv::imshow("Averaged image", fuzzyfied);
    cv::waitKey(0);
    return  0;
}