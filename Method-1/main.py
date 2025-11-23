from rembg import remove
from PIL import Image

# use .jpg for better output & make sure your input image name is in the input_path
input_path = "input.jpg" 
output_path = "output.png"

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)