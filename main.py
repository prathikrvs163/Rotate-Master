import cv2
import os
import shutil


def auto_rotate_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        if os.path.isfile(file_path):
            image = cv2.imread(file_path)
            if image is None:
                continue

            height, width = image.shape[:2]

            # If the image is landscape but stored as portrait
            if width > height:
                rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
                output_path = os.path.join(output_folder, filename)
                cv2.imwrite(output_path, rotated_image)
                print(f"Rotated and moved: {filename}")
            else:
                print(f"No rotation needed: {filename}")


# Example usage
input_folder = r"Your folder path"  # Folder containing original images
output_folder = "rotated_images"  # Folder for corrected images
auto_rotate_images(input_folder, output_folder)