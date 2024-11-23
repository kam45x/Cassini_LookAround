import cv2

if __name__ == "__main__":
    # Load images
    large_image = cv2.imread('../images/copernicus_image.png')
    template = cv2.imread('../images/fuzzzyfied_image.png')

    # Convert to grayscale
    large_gray = cv2.cvtColor(large_image, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Template matching
    result = cv2.matchTemplate(large_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Get position
    top_left = max_loc
    h, w = template_gray.shape
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # Draw rectangle around match
    cv2.rectangle(large_image, top_left, bottom_right, (0, 255, 0), 2)

    cv2.imshow("Image matched", large_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
