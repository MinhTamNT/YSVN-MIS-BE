import base64


def save_base64_image(base64_str, output_file):
    header, data = base64_str.split(',', 1)
    image_data = base64.b64decode(data)

    with open(output_file, 'wb') as f:
        f.write(image_data)
