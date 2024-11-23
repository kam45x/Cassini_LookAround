#include "../include/fuzzyfication.hpp"

cv::Mat blur_image(const cv::Mat& image, unsigned int block_size){
    auto output_image = cv::Mat(image.rows / block_size, image.cols / block_size,CV_8UC3, cv::Scalar(0, 0, 0));


    for (int i = 0; i < image.rows - block_size; i += block_size) {
        for (int j = 0; j < image.cols - block_size; j += block_size) {
            cv::Rect block_rect(j, i, block_size, block_size);
            cv::Mat block = image(block_rect);

            cv::Scalar avg_color = cv::mean(block);

            output_image.at<cv::Vec3b>(i / block_size, j / block_size) = cv::Vec3b(avg_color[0], avg_color[1], avg_color[2]);
        }
    }
    return output_image;
}
