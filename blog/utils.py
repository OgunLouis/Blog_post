import base64
import requests
import os

def upload_to_imagekit(file):
    print("🔄 Uploading to ImageKit...")

    url = "https://upload.imagekit.io/api/v1/files/upload"

    # Base64 with proper prefix
    file_content = f"data:{file.content_type};base64," + base64.b64encode(file.read()).decode()

    payload = {
        "file": file_content,
        "fileName": file.name,
    }

    headers = {
        "Authorization": "Basic " + base64.b64encode(
            (os.getenv("IMAGEKIT_PRIVATE_KEY") + ":").encode()
        ).decode()
    }

    response = requests.post(url, data=payload, headers=headers)

    print("🔁 Response status:", response.status_code)
    print("🧾 Response text:", response.text)

    if response.status_code == 200:
        image_url = response.json()["url"]
        print("✅ Image uploaded:", image_url)
        return image_url
    else:
        print("❌ Upload failed")
