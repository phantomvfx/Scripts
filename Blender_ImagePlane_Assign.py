import bpy
import os

def assign_background_images_to_cameras(image_folder_path):
    """
    Assigns background images to cameras based on their names and the given image folder path.

    Args:
        image_folder_path (str): Path to the folder containing image files.

    Raises:
        FileNotFoundError: If an image file cannot be found.
    """

    # Iterate through cameras
    for camera_obj in bpy.data.objects:
        if camera_obj.type == "CAMERA":
            camera_name = camera_obj.data.name

            # Construct image filename based on camera name
            image_filename = os.path.join(image_folder_path, camera_name + ".jpg")  # Adjust extension if needed

            # Check if image exists
            if os.path.isfile(image_filename):
                # Activate background image for the camera
                camera_obj.data.show_background_images = True

                # Load the image
                bpy.ops.image.open(filepath=image_filename)
                image = bpy.data.images[os.path.basename(image_filename)]

                # Assign the image to the camera's background image slot
                background_image_slot = camera_obj.data.background_images.new()
                background_image_slot.image = image

                # Print a success message
                print(f"Assigned background image '{image_filename}' to camera '{camera_name}'.")
            else:
                # Handle missing image (optional)
                print(f"Warning: Image file not found for camera '{camera_name}'.")

# Replace with your actual image folder path
image_folder_path = "X:\Photogrammetry\Calderon\projector\imageplanes"

# Call the function with the folder path
assign_background_images_to_cameras(image_folder_path)


