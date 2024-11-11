from PIL import Image
import os

def convert_webp_to_jpg(webp_path, jpg_path):
    # 打开WebP图片
    img = Image.open(webp_path).convert("RGB")
    # 保存为JPG格式
    img.save(jpg_path, "JPEG")

# 示例：将单个文件转换
convert_webp_to_jpg(r"F:\公众号\注册材料\1.webp", r"F:\公众号\注册材料\1.jpg")
