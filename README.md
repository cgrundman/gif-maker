# 🖼️ GIF Maker

A simple Python utility to create an animated GIF from a folder of images, sorted by filename.

---

## 📦 Installation

You can install this package directly from GitHub using pip:

```bash
pip install git+https://github.com/cgrundman/gif-maker.git
```
Make sure you have Pillow installed (it’s included automatically when you install the package).

## 🧰 Usage

### 1. Import and use in your Python code:

```bash
from gifmaker import create_gif

# Parameters:
# - input_folder: path to your folder of images
# - output_gif: filename for the resulting GIF
# - duration: time per frame in milliseconds (optional)

create_gif("path/to/images", "output.gif", duration=150)
```
### 2. Example Folder Structure

```bash
my-project/
├── my-script.py
└── images/
    ├── frame001.jpg
    ├── frame002.jpg
    ├── frame003.jpg
```

## 📝 Notes

<ul>
    <li>Supports .jpg, .jpeg, and .png files</li>
    <li>Images are automatically sorted by filename</li>
    <li>Output GIF loops forever (loop=0)</li>
    <li>All images are resized to the dimensions of the first image to ensure consistency</li>
</ul>

## 🛠️ Development

Clone the repo and install it locally for development:

```bash
git clone https://github.com/cgrundman/gif-maker.git
cd gif-maker
pip install -e .
```

## 📄 License

MIT License
