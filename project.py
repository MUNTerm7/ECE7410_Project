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
        image = cv2.imread(image_path_user)

        image_float = np.float32(image)
  
        intensity_image = rgbtohsi_histequ.intensity_calculation(image_float)

        smoothed_image = smoothing.gaussian_filter(intensity_image)

        sharpened_img = sobelsharpening.sobel_sharpening(smoothed_image)

        eroded_img = morphoper.erosion_operation(sharpened_img)

        opening_img = morphoper.dilation_operation(eroded_img)

        #Normalize the intensity_img[0,255] to [0,1] to be used for HSI -> RGB conversion
        normalized_opening_img = rgbtohsi_histequ.pixel_normalize_image(opening_img)

        cv2.imshow("Normalized Intensity Image", normalized_opening_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #Normalize original RGB from [0,255] -> [0,1]
        normalized_rgb = rgbtohsi_histequ.normalize(image_float)

        cv2.imshow("Normalized RGB Input Image", normalized_rgb)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
 
        hue_image = rgbtohsi_histequ.hue_calculation(normalized_rgb)
        
        saturation_image = rgbtohsi_histequ.saturation_calculation(normalized_rgb)
 
        #Calculate the RGB normalized in [0,1] using HSI -> RGB equations provided in class
        rgb_normalized_image = rgbtohsi_histequ.hsi_conversion_rgb(hue_image, saturation_image, normalized_opening_img)

        cv2.imshow("RGB Normalized Image", rgb_normalized_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        #Calculate the RGB normalized in [0,255]
        rgb_scaled_image = rgbtohsi_histequ.scale_image(rgb_normalized_image)

        cv2.imshow("RGB Scaled Image", rgb_scaled_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        color_sliced_img = colorslicing.color_slicing(rgb_scaled_image)

        output_file_path = "RGB_Result.jpg"
        cv2.imwrite(output_file_path, color_sliced_img)

if __name__ == "__main__":
    main()