## 📌 Background Remover (Python + rembg)

This is a simple Python script that removes the background from an image using rembg and Pillow. Just place your image in the project folder, run the script, and boom — background gone.

---

### 🚀 Features

- Removes image background using AI (U²-Net)
- Super simple script (main.py)
- Works offline after the model downloads once
- Outputs a transparent PNG file

---

###  📂 Project Structure

```bash
project/
│── main.py
│── requirements.txt
│── input.jpg    ← your input image
│── output.png   ← generated output
```
---
### 🛠 Requirements

Your requirements.txt contains:
```bash
rembg
pillow
onnxruntime
```
These will install the background removal engine + image processing support.

---

### 📥 Installation
1. Clone the Repository
```bash
git clone https://github.com/meshal10613/Remove-Background-using-Python

cd "Remove-Background-using-Python"

cd Method-1
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```
The first time you run the script, rembg will automatically download the U²-Net model.
Yes, that big file download is normal and safe — it’s required for background removal.

---

### ▶️ Usage
Place your input image as input.jpg (or change the filename in the script).

Then run:
```bash
python main.py
```

This will generate:
```bash
output.png
```
with the background removed.

---

### ❓ FAQ

**1. Why is rembg downloading a big .onnx file?**

Because it uses the U²-Net AI model for background removal. It's 150–180MB and completely safe.

**2. Does it work offline?**

Yes — after the model is downloaded once, you can run the script offline.

**3. Can I use PNG as input?**

Yes. JPG is recommended because rembg works slightly better on non-transparent images.

---