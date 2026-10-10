import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

from PIL import Image, ExifTags


def format_file_size(size_in_bytes):
    units = ["Bytes", "KB", "MB", "GB", "TB"]
    size = float(size_in_bytes)
    for unit in units:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"


def get_exif_data(image):
    exif_data = {}
    try:
        raw_exif = image.getexif()
        for tag_id, value in raw_exif.items():
            tag_name = ExifTags.TAGS.get(tag_id, tag_id)
            exif_data[tag_name] = value
    except Exception:
        pass
    return exif_data


def get_resolution(image):
    dpi = image.info.get("dpi")
    if dpi:
        return f"{dpi[0]} x {dpi[1]} DPI"
    return "Not Available"


def print_exif_metadata(exif_data):
    print("\nEXIF Metadata")
    print("-" * 31)

    important_fields = {
        "Camera": "Model",
        "Date Taken": "DateTimeOriginal",
        "Date Modified": "DateTime",
        "Orientation": "Orientation",
        "Make": "Make",
        "Software": "Software",
    }

    for display_name, exif_key in important_fields.items():
        value = exif_data.get(exif_key, "Not Available")
        print(f"{display_name:<16}: {value}")

    other_exif = {
        key: value
        for key, value in exif_data.items()
        if key not in important_fields.values()
    }

    if other_exif:
        print("\nOther EXIF Data")
        print("-" * 31)
        for key, value in other_exif.items():
            print(f"{str(key):<25}: {value}")


def analyze_image(image_path):
    if not os.path.exists(image_path):
        print("Error: File not found.")
        return

    supported_extensions = [".jpg", ".jpeg", ".png", ".tiff", ".tif", ".webp", ".bmp"]
    extension = os.path.splitext(image_path)[1].lower()

    if extension not in supported_extensions:
        print("Error: Unsupported image format.")
        print("Supported formats: JPG, JPEG, PNG, TIFF, WEBP, BMP")
        return

    try:
        with Image.open(image_path) as image:
            file_name = os.path.basename(image_path)
            file_size = os.path.getsize(image_path)
            width, height = image.size
            exif_data = get_exif_data(image)

            print("=" * 32)
            print("IMAGE METADATA REPORT")
            print("=" * 32)

            print(f"\nFile Name       : {file_name}")
            print(f"File Size       : {format_file_size(file_size)}")
            print(f"File Format     : {image.format}")
            print(f"Width           : {width} pixels")
            print(f"Height          : {height} pixels")
            print(f"Resolution      : {get_resolution(image)}")
            print(f"Color Mode      : {image.mode}")

            print_exif_metadata(exif_data)

            print("\n" + "=" * 32)
            print("REPORT COMPLETED")
            print("=" * 32)

    except Exception as error:
        print(f"Error while analyzing image: {error}")


def main():
    print("Image Analyzer")
    print("-" * 30)

    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        image_path = input("Enter image path (or press Enter for default): ").strip()
        if not image_path:
            # Find the image file dynamically using os.listdir
            script_dir = os.path.dirname(os.path.abspath(__file__))
            for fname in os.listdir(script_dir):
                if fname.lower().endswith('.png') and 'screenshot' in fname.lower():
                    image_path = os.path.join(script_dir, fname)
                    print(f"Using default: {fname}")
                    break
            else:
                image_path = input("No default image found. Please enter image path: ").strip()

    analyze_image(image_path)


if __name__ == "__main__":
    main()