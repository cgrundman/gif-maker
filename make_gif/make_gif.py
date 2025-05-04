import os
from PIL import Image

def create_gif(input_folder, output_gif, duration=200):
    image_files = sorted([
        f for f in os.listdir(input_folder)
        if f.lower().endswith(('.png', '.jpg', '.jpeg'))
    ])

    if not image_files:
        raise ValueError("No image files found in the folder.")

    images = [Image.open(os.path.join(input_folder, file)).convert('RGB') for file in image_files]
    width, height = images[0].size
    images = [img.resize((width, height)) for img in images]

    images[0].save(
        output_gif,
        save_all=True,
        append_images=images[1:],
        duration=duration,
        loop=0
    )
    print(f"GIF saved as {output_gif}")