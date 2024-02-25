import requests
import os
from urllib.parse import urlparse
from PIL import Image

# List of image URLs from text file that you downloaded after running the script from the console.txt in console
image_urls = [
"https://cdn.discordapp.com/emojis/a1.webp?size=80&quality=lossless", #example
"https://cdn.discordapp.com/emojis/b2.gif?size=80&quality=lossless", #example
"https://cdn.discordapp.com/emojis/c3.webp?size=44&quality=lossless" #example
]

# Folder to save downloaded images
download_folder = r"C:\xyz" #Write your desired path

# Create the folder if it doesn't exist
os.makedirs(download_folder, exist_ok=True)

# Download each image
for url in image_urls:
    response = requests.get(url)
    if response.status_code == 200:
        # Extract the filename from the URL
        parsed_url = urlparse(url)
        filename_webp = os.path.join(download_folder, os.path.basename(parsed_url.path))

        # Save the WebP image to the folder
        with open(filename_webp, 'wb') as file:
            file.write(response.content)

        # Convert WebP to JPEG for using in Discord to add stickers in another server
        filename_jpg = os.path.splitext(filename_webp)[0] + ".jpg"
        img = Image.open(filename_webp).convert('RGB')
        img.save(filename_jpg)
        os.remove(filename_webp)  # Remove the original WebP file

        print(f"Converted and saved as: {filename_jpg}")
    else:
        print(f"Failed to download: {url}")