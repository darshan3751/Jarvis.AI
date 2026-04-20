import asyncio
from random import randint
from PIL import Image
import requests
from dotenv import get_key
import os
from time import sleep


def open_images(prompt):
    folder_path = r"Data"
    prompt = prompt.replace(" ","_")

    Files = [f"{prompt}{i}.jpg" for i in range(1, 2)]

    for jpg_file in Files:
        image_path = os.path.join(folder_path, jpg_file)

        try:

            img = Image.open(image_path)
            print(f"opening image: {image_path}")
            img.show()
            sleep(1)

        except IOError:
            print(f"Unable to Open {image_path}")

async def query(url):
    try:
        response = await asyncio.to_thread(requests.get, url, timeout=15)
        return response.content
    except requests.exceptions.RequestException:
        print("Image API timed out or failed.")
        return b""

async def generate_images(prompt: str):
    tasks = []

    for _ in range(1):
        url = f"https://image.pollinations.ai/prompt/{prompt}?width=1024&height=1024&nologo=true&seed={randint(0, 1000000)}"
        task = asyncio.create_task(query(url))
        tasks.append(task)

    image_bytes_list = await asyncio.gather(*tasks)

    for i, image_bytes in enumerate(image_bytes_list):
        with open(fr"Data\{prompt.replace(' ','_')}{i + 1}.jpg", "wb") as f:
            f.write(image_bytes)

def GenerateImages(prompt: str):
    asyncio.run(generate_images(prompt))
    open_images(prompt)

while True:

    try:

        with open(r"Frontend\Files\ImageGeneration.data", "r", encoding='utf-8') as f:
            Data = f.read()

        Prompt, Status = Data.split(",")

        if Status == "True":
            print("Generating Images...")
            ImageStatus = GenerateImages(prompt=Prompt)

            with open(r"Frontend\Files\ImageGeneration.data", "w", encoding='utf-8') as f:
                f.write("False,False")
                
            break

        else:
            sleep(1)

    except :
        pass           

