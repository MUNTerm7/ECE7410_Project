import os
import cv2
import numpy as np

def user_img_input():
    path = input("Hello! Please enter the path to your image file:  ")
    img_path = os.path.expanduser(path)
    return img_path

def path_validity(img_path):
    if os.path.isfile(img_path):
        print("\nFile path found at: " + str(img_path))
        return img_path
    else:
        print("File path not found. Path was: " + str(img_path))
        return None

def img_grayscale_conversion(img_path):
    try:
        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if image is not None:
            cv2.imshow("Grayscale Image", image)
            cv2.waitKey(1000)
            cv2.destroyAllWindows()
            img_height = image.shape[0]
            img_width = image.shape[1]
            return image, img_height, img_width
        else:
            print("\nSorry, the image could not be loaded\n")
            return None
    except Exception as e:
        print("\nError encountered while opening image using OpenCV:  "+ str(e)+'\n')
        return None

def gaussian_filter(image, kernel_size=7):
    # Apply Gaussian filter for smoothing
    smoothed_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    # Display the smoothed image
    cv2.imshow("Smoothed Image", smoothed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return smoothed_image

def median_filter(image, kernel_size=7):
    # Apply median filter for smoothing
    smoothed_image = cv2.medianBlur(image, kernel_size)
    
    cv2.imshow("Smoothed Image", smoothed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return smoothed_image

def main():
    # Accept path to image
    image_path_user = user_img_input()

    # Verify that the path entered by the user is a valid one
    valid_path = path_validity(image_path_user)

    # Tries to open the image at the path in the OpenCV grayscale mode
    if valid_path:
        grayscale_img, img_height, img_width = img_grayscale_conversion(image_path_user)
        
        if grayscale_img is not None:
            # Apply Gaussian filter for smoothing
            smoothed_img = gaussian_filter(grayscale_img)

if __name__ == "__main__":
    main()
