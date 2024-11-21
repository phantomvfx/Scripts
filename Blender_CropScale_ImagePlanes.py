import bpy

# Iterate over objects in the current view layer
for obj in bpy.context.view_layer.objects:
    # Check if the object is a camera
    if obj.type == 'CAMERA':
        # Access all background images (if any)
        for background_image in obj.data.background_images:
            # Set the frame method to 'CROP'
            background_image.frame_method = 'CROP'
            # Set the scale of the background image
            background_image.scale = 1.03

        # Optional: Handle potential case of no background image
        if not obj.data.background_images:
            print(f"Camera '{obj.name}' has no background image.")

# Print a confirmation message
print("Frame method of background images in all cameras set to 'CROP' and background image scale set to 1.03 (if applicable)")
