import os
import cv2
import numpy as np

'''
Accepts a string input of the user's image path file 
and parses the '~' from the path to the user's root directory
'''
def user_img_input():

    path = input("Hello! Please enter the path to your image file:  ")
    img_path = os.path.expanduser(path)
    return img_path

'''
Verifies that a file exists at the path that has been parsed from the user input
'''
def path_validity(img_path):

    if os.path.isfile(img_path):
        print("\nFile path found at: " + str(img_path))
        return img_path
    else:
        print("File path not found. Path was: " + str(img_path))
        return None


'''
If the image exists, uses OpenCV's grayscale mode to display the image
and waits one second before closing it. Returns the image height and width.
If image does not exist, returns none.
RaisesException: Depending on error in opening image
'''
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
'''
Performs a log transformation on the grayscalegiven image
'''
def log_transformation(image):

    log_image = np.log1p(image)  # Apply log transformation
    log_image = np.array(log_image, np.uint8) # Convert to uint8 array. Used the line from https://www.geeksforgeeks.org/log-transformation-of-an-image-using-python-and-opencv/ to convert to uint8
    log_image = cv2.normalize(log_image, None, 0, 255, cv2.NORM_MINMAX)  # Normalize to 0-255

    # Display the log-transformed image
    cv2.imshow("Log Transformed Image", log_image)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    
    return log_image

def main():
    # Accept path to image
    image_path_user = user_img_input()

    # Verify that the path entered by the user is a valid one
    valid_path = path_validity(image_path_user)

    # Tries to open the image at the path in the OpenCV grayscale mode
    if valid_path:
        grayscale_img, img_height, img_width = img_grayscale_conversion(image_path_user)
        
        if grayscale_img is not None:
            # Apply log transformation
            log_img = log_transformation(grayscale_img)

if __name__ == "__main__":
    main()