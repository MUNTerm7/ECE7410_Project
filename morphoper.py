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
Performs an erosion operation on the given grayscale image
'''
def erosion_operation(image):
    # Morphological Operations Documentation https://docs.opencv.org/4.x/d9/d61/tutorial_py_morphological_ops.html
    # Define a cross-shaped structuring element
    cross_kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
    erosion_image = cv2.erode(image, cross_kernel, iterations=1)  # Apply the erosion operation

    # Display the eroded image
    cv2.imshow("Eroded Image", erosion_image)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    
    return erosion_image

def main():
    # Accept path to image
    image_path_user = user_img_input()

    # Verify that the path entered by the user is a valid one
    valid_path = path_validity(image_path_user)

    # Tries to open the image at the path in the OpenCV grayscale mode
    if valid_path:
        grayscale_img, img_height, img_width = img_grayscale_conversion(image_path_user)
        
        if grayscale_img is not None:
            # Apply erosion operation
            eroded_img = erosion_operation(grayscale_img)

if __name__ == "__main__":
    main()