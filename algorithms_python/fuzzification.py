import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    file_name = '../images/google_maps_mockup.png'
    image = cv2.imread(file_name)

    # Define the block size
    block_size = 4

    # Create an empty output image with the same number of channels
    output_image = np.zeros((image.shape[0] // block_size, image.shape[1] // block_size, 3), dtype=np.uint8)

    # Loop over the image in steps of block_size
    for i in range(0, image.shape[0] - block_size + 1, block_size):
        for j in range(0, image.shape[1] - block_size + 1, block_size):
            block = image[i:i + block_size, j:j + block_size]

            # Compute the average of the block
            avg_color = np.mean(block, axis=(0, 1)).astype(np.uint8)

            output_image[i // block_size, j // block_size] = avg_color

    # Display the original and fuzzified image
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.subplot(1, 2, 2)
    plt.title("Fuzzified Image")
    plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
    plt.savefig("../images/fuzzy_compare.png", dpi=400)
    plt.show()

    cv2.imwrite("../images/fuzzzyfied_image.png", output_image)

