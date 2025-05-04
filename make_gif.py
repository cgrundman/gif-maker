import os
from PIL import Image

# Configuration
input_folder = "images"             # folder where your images are
output_gif = "output/output.gif"    # name of the resulting gif
duration = 200                      # time per frame in milliseconds

# Step 1: Get all image file paths sorted by filename
image_files = sorted([
    f for f in os.listdir(input_folder)
    if f.lower().endswith(('.png', '.jpg', '.jpeg'))
])

# Step 2: Load images
images = [Image.open(os.path.join(input_folder, file)) for file in image_files]

# Optional: Convert all images to same mode and size (GIFs require consistent frame sizes)
images = [img.convert('RGB') for img in images]
width, height = images[0].size
images = [img.resize((width, height)) for img in images]

# Step 3: Save as GIF
if images:
    images[0].save(
        output_gif,
        save_all=True,
        append_images=images[1:],
        duration=duration,
        loop=0
    )
    print(f"GIF saved as {output_gif}")
else:
    print("No images found.")
