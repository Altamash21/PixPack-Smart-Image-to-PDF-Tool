# 📦 PixPack – Smart Image to PDF Tool

PixPack ek smart Python tool hai jo multiple images (random sizes aur shapes wali) ko **automatically pack karke ek optimized PDF** me arrange karta hai.
Yeh project image processing, rectangle packing algorithm, aur efficient PDF generation ka ek demo hai.

---

## 🚀 Features

* 🖼️ Automatically arrange random-size images in pages (A4, Letter, etc.)
* ✂️ Crops and cleans images (removes transparent background)
* 📏 Preserves original aspect ratio
* 🧠 Uses smart packing to minimize empty space
* 📄 Generates a high-quality, compact PDF output
* ⚡ Compresses images for smaller file size

---

## 🧰 Tech Stack

* **Language:** Python 3
* **Libraries:**

  * Pillow (PIL) – Image processing
  * ReportLab – PDF generation
  * NumPy (optional) – Efficient packing calculations

---

## 📁 Folder Structure

```
PixPack/
│
├── input_images/          # Folder with input images
├── output.pdf             # Generated PDF file
├── requirements.txt       # Dependencies list
├── sample_data_generation.py  # (Optional) To create random sample images
└── README.md              # Project documentation
```

---

## ⚙️ Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/pixpack-image-pdf.git
cd pixpack-image-pdf
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate       # (Windows)
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Add Images

Add your images inside the `input_images/` folder.

### Step 5: Run the Script

```bash
python main.py
```

---

## 🧩 Output

A new file named `output.pdf` will be generated in the root directory containing all packed images.

---

## 🧠 Future Enhancements

* Add GUI interface for drag-and-drop images
* Add different packing modes (tight, uniform, grid)
* Add background color and margins customization

---

## 🏗️ Author

**Altamash Pinjari**
📧 (altamashpinjari90@gmail.com)

---

### ⭐ Don’t forget to star the repo if you like this project!


