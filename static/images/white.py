from PIL import Image

def remove_white_bg(img_path, output_path, threshold=240):
    img = Image.open(img_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        # 如果 RGB 值都大于阈值，则认为是白色，设为透明
        if item[0] >= threshold and item[1] >= threshold and item[2] >= threshold:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path, "PNG")

remove_white_bg("framework.png", "output.png")
