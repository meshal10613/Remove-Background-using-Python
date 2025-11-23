## 📌 Background Remover (withoutbg)

This project removes the background from an image using the withoutbg library. It provides a very simple Python script (main.py) that takes an input image and outputs a clean, background-free version.

---

### 🚀 Features

- Uses withoutbg (open-source version)
- Very easy to use
- Outputs a clean PNG image with transparency
- Lightweight & beginner friendly

---

### 📂 Project Structure
```bash
project/
│── main.py
│── requirements.txt
│── input.png
│── outputt.png
```

---

### 🛠 Requirements
Your ```requirements.txt```:
```bash
withoutbg
```
Install this and you're basically good to go.

---

### 📥 Installation
```bash
git clone https://github.com/meshal10613/Remove-Background-using-Python

cd "Remove-Background-using-Python"

cd Method-2
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```
The first time you run the script, rembg will automatically download the U²-Net model.
Yes, that big file download is normal and safe — it’s required for background removal.

---

### ▶️ Usage

1. Put your input image as input.png (or change the name in the script).

2. Run:
```bash
python main.py
```
The output file will be saved as:
```bash
output.png
```
with the background removed.

---

### ❓ FAQ
**1. Does withoutbg download any model or large file?**
No — unlike rembg, this method generally works without downloading large models.

**2. Does it support PNG/JPG?**
Yes, both work.

**3. Do I need API keys?**
No. You’re using the open-source version.

---