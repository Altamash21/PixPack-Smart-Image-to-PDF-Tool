import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

INPUT_DIR = "input_images"
OUTPUT_PDF = "output.pdf"
PAGE_SIZE = A4
MARGIN = 10

def preprocess_image(image_path: str):
    img = Image.open(image_path).convert("RGBA")
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
    return img

def compress_image(image: Image.Image, quality: int = 85) -> Image.Image:
    return image.convert("RGB")

def pack_images(images, page_width, page_height, margin):
    pages = []
    current_page = []
    x, y = margin, margin
    max_row_height = 0
    for img in images:
        iw, ih = img.size
        if x + iw + margin > page_width:
            x = margin
            y += max_row_height + margin
            max_row_height = 0
        if y + ih + margin > page_height:
            pages.append(current_page)
            current_page = []
            x, y = margin, margin
            max_row_height = 0
        current_page.append((img, x, y))
        x += iw + margin
        max_row_height = max(max_row_height, ih)
    if current_page:
        pages.append(current_page)
    return pages

def generate_pdf(input_dir: str, output_pdf_path: str, page_size):
    images = []
    if not os.path.exists(input_dir):
        print(f"Run sample_data_generation.py first to create images.")
        return
    for fname in sorted(os.listdir(input_dir)):
        if fname.lower().endswith((".png", ".jpg", ".jpeg")):
            img = preprocess_image(os.path.join(input_dir, fname))
            img = compress_image(img)
            images.append(img)
    if not images:
        print("No images found.")
        return
    page_width, page_height = page_size
    pages = pack_images(images, page_width, page_height, MARGIN)
    c = canvas.Canvas(output_pdf_path, pagesize=page_size)
    for page in pages:
        for img, x, y in page:
            temp_path = "temp_img.jpg"
            img.save(temp_path, "JPEG", quality=85)
            c.drawImage(temp_path, x, page_height - y - img.height, width=img.width, height=img.height)
            os.remove(temp_path)
        c.showPage()
    c.save()
    print(f"✅ PDF ready: {output_pdf_path}")

if __name__ == "__main__":
    generate_pdf(INPUT_DIR, OUTPUT_PDF, PAGE_SIZE)
