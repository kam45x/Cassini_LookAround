#ifndef FUZZYFICATION_HPP
#define FUZZYFICATION_HPP

#include <opencv2/opencv.hpp>

cv::Mat blur_image(const cv::Mat& image, unsigned int block_size);

#endif //FUZZYFICATION_HPP
