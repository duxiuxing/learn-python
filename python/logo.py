# -- coding: UTF-8 --

from PIL import Image


class Logo:
    @staticmethod
    def check_logo_left(logo, pixel_test):
        for x in range(logo.width):
            for y in range(logo.height):
                if logo.getpixel((x, y)) != pixel_test:
                    return x
        return 0

    @staticmethod
    def check_logo_top(logo, pixel_test):
        for y in range(logo.height):
            for x in range(logo.width):
                if logo.getpixel((x, y)) != pixel_test:
                    return y
        return 0

    @staticmethod
    def check_logo_right(logo, pixel_test):
        for x_offset in range(1, logo.width + 1):
            for y in range(logo.height):
                if logo.getpixel((logo.width - x_offset, y)) != pixel_test:
                    return logo.width - x_offset
        return logo.width - 1

    @staticmethod
    def check_logo_bottom(logo, pixel_test):
        for y_offset in range(1, logo.height + 1):
            for x in range(logo.width):
                if logo.getpixel((x, logo.height - y_offset)) != pixel_test:
                    return logo.height - y_offset
        return logo.height - 1

    @staticmethod
    def crop(png_file_path):
        logo = Image.open(png_file_path)
        pixel_test = logo.getpixel((0, 0))

        left = Logo.check_logo_left(logo, pixel_test)
        top = Logo.check_logo_top(logo, pixel_test)
        right = Logo.check_logo_right(logo, pixel_test)
        bottom = Logo.check_logo_bottom(logo, pixel_test)

        if (
            left == 0
            and top == 0
            and right == logo.width - 1
            and bottom == logo.height - 1
        ):
            return logo

        return logo.crop((left, top, right + 1, bottom + 1))

    @staticmethod
    def resize(png_file_path, max_width, max_height, min_width=0, min_height=0):
        src_logo = Logo.crop(png_file_path)
        if src_logo.width < max_width and src_logo.height < max_height:
            print(
                "【警告】源 Logo 分辨率较低，建议使用更高分辨率的图片\n"
                f"{src_logo.width} x {src_logo.height}：{png_file_path}"
            )

        if (src_logo.height * max_width / max_height) < src_logo.width:
            dst_logo_width = max_width
            dst_logo_height = int(dst_logo_width * src_logo.height / src_logo.width)
            if dst_logo_height < min_height:
                dst_logo_height = min_height
            return src_logo.resize((dst_logo_width, dst_logo_height))
        elif (src_logo.height * max_width / max_height) == src_logo.width:
            return src_logo.resize((max_width, max_height))
        else:
            dst_logo_height = max_height
            dst_logo_width = int(dst_logo_height * src_logo.width / src_logo.height)
            return src_logo.resize((dst_logo_width, dst_logo_height))
