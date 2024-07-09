import rgbtohsi_histequ
import smoothing
import sobelsharpening
import morphoper
import colorslicing
import cv2
import numpy as np

def main():
    # Accept path to image
    image_path_user = rgbtohsi_histequ.user_img_input()

    # Verify that the path entered by the user is a valid one
    valid_path = rgbtohsi_histequ.path_validity(image_path_user)

    # Tries to open the image at the path in the OpenCV grayscale mode
    if valid_path:
        #Read image from path
        image = cv2.imread(image_path_user)

        #Convert image to float
        image_float = np.float32(image)
  
        #Intensity Image in [0,255]
        intensity_image = rgbtohsi_histequ.intensity_calculation(image_float)

        #Display Intensity Image
        cv2.imshow("Intensity Image", intensity_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #Normalize the histogram to get the PDF in [0,255]
        pdf = rgbtohsi_histequ.normalize_histogram(intensity_image)
        
        # Perform histogram equalization using the PDF in [0,255]
        intensity_histogram_equalized_image = rgbtohsi_histequ.histogram_equalization(intensity_image, pdf)

        #Display Intensity Image
        cv2.imshow("Equalized Image", intensity_histogram_equalized_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #smoothed_image = smoothing.gaussian_filter(intensity_histogram_equalized_image) #Hist equ preformed before

        smoothed_image = smoothing.gaussian_filter(intensity_image) #Gaussian Filter

        #Step 3
        sharpened_img = sobelsharpening.sobel_sharpening(smoothed_image)

        #Step 4
        eroded_img = morphoper.erosion_operation(sharpened_img)

        normalized_eroded_img = rgbtohsi_histequ.pixel_normalize_image(eroded_img)

        #Normalize original RGB from [0,255] -> [0,1]
        normalized_rgb = rgbtohsi_histequ.normalize(image_float)
       
        #Step 5 Calculate the hue of the image from RGB -> Hue
        hue_image = rgbtohsi_histequ.hue_calculation(normalized_rgb)

        #Step 6 Calculate saturation of the color image from RGB -> Saturation
        saturation_image = rgbtohsi_histequ.saturation_calculation(normalized_rgb)
 
        #Step 7 Calculate the RGB normalized in [0,1] using HSI -> RGB equations provided in class
        rgb_normalized_image = rgbtohsi_histequ.hsi_conversion_rgb(hue_image, saturation_image, normalized_eroded_img)

        #Calculate the RGB normalized in [0,255]
        rgb_scaled_image = rgbtohsi_histequ.scale_image(rgb_normalized_image)

        #Display Resulting Image
        cv2.imshow("RGB Histogram Equalized Resultant Image", rgb_scaled_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #Step 8 Color Slicing
        color_sliced_img = colorslicing.color_slicing(rgb_scaled_image)

        #Define path of resultant image
        output_file_path = "RGB_Result.jpg"

        # Save the image
        cv2.imwrite(output_file_path, color_sliced_img)

if __name__ == "__main__":
    main()