import sys

from PIL import Image

import pytesseract

from wand.image import Image as wi

from tika import parser


def extract_text_image(from_file, lang='deu', image_type='jpeg', resolution=300):
    print("-- Parsing image", from_file, "--")

    print("---------------------------------")

    pdf_file = wi(filename=from_file, resolution=resolution)

    image = pdf_file.convert(image_type)

    for img in image.sequence:

        img_page = wi(image=img)

        image = Image.open(io.BytesIO(img_page.make_blob(image_type)))

        text = pytesseract.image_to_string(image, lang=lang)

        for part in text.split("\n"):
            print("{}".format(part))


def parse_text(from_file):
    print("-- Parsing text", from_file, "--")

    text_raw = parser.from_file(from_file)

    print("---------------------------------")

    print(text_raw['content'].strip())

    print("---------------------------------")


if __name__ == '__main__':
    parse_text("E:/博士 2021/0 智能家用健康管理机器人 ZXD/0 健康 家庭 移动 机器人 Soopat ZXD 20220706/")

    extract_text_image("E:/博士 2021/0 智能家用健康管理机器人 ZXD/0 健康 家庭 移动 机器人 Soopat ZXD 20220706/")
