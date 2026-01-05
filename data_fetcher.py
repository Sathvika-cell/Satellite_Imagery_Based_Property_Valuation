
import os
import requests
import pandas as pd
from tqdm import tqdm

API_KEY = os.getenv("MAPS_API_KEY")

IMG_DIR = "images"
IMG_SIZE = "400x400"
ZOOM = 18

def fetch_image(lat, lon, save_path):
    url = (
        "https://maps.googleapis.com/maps/api/staticmap"
        f"?center={lat},{lon}"
        f"&zoom={ZOOM}"
        f"&size={IMG_SIZE}"
        f"&maptype=satellite"
        f"&key={API_KEY}"
    )
    r = requests.get(url)
    if r.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(r.content)

def download_images(csv_path):
    df = pd.read_csv(csv_path)
    df = df.reset_index(drop=True)   # ⭐ FIX

    os.makedirs(IMG_DIR, exist_ok=True)

    for i, row in tqdm(df.iterrows(), total=len(df)):
        img_path = f"{IMG_DIR}/{i}.png"
        if not os.path.exists(img_path):
            fetch_image(row['lat'], row['long'], img_path)

if __name__ == "__main__":
    download_images("/content/drive/MyDrive/property_valuation/kc_house_data.csv")
