import os
from PIL import Image, ImageDraw

DIRECTIONS = ("^", "v", "<", ">")


def generate_image_from_text(pattern):
    lines = pattern.strip().split("\n")
    height = len(lines)
    width = max(len(line) for line in lines)

    cell_size = 10
    img_width = width * cell_size
    img_height = height * cell_size
    image = Image.new("RGB", (img_width, img_height), "lightgrey")
    draw = ImageDraw.Draw(image)

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            x0 = x * cell_size
            y0 = y * cell_size
            x1 = x0 + cell_size
            y1 = y0 + cell_size

            if char == "#":
                draw.rectangle([x0, y0, x1, y1], fill="grey")
            elif char in DIRECTIONS:
                draw.rectangle([x0, y0, x1, y1], fill="lightgrey")
                if char == "^":
                    points = [(x0 + cell_size // 2, y0), (x0, y1), (x1, y1)]
                elif char == "v":
                    points = [(x0, y0), (x1, y0), (x0 + cell_size // 2, y1)]
                elif char == "<":
                    points = [(x0, y0 + cell_size // 2), (x1, y0), (x1, y1)]
                elif char == ">":
                    points = [(x0, y0), (x1, y0 + cell_size // 2), (x0, y1)]
                draw.polygon(points, fill="red")
            elif char == " ":
                draw.rectangle([x0, y0, x1, y1], fill="purple")

    return image


def generate_gif_from_patterns(directory, output_path, duration=500):
    frames = []
    files = sorted(
        [f for f in os.listdir(directory) if f.endswith(".txt")],
        key=lambda x: int(os.path.splitext(x)[0])
    )

    for file in files:
        print(f"Processing {file}")
        file_path = os.path.join(directory, file)
        with open(file_path, "r") as f:
            pattern = f.read()
        frame = generate_image_from_text(pattern)
        frames.append(frame)

    if frames:
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            duration=duration,
            loop=0
        )
        print(f"Output file: {output_path}")
    else:
        print(f"There are no valid patterns in directory {directory}.")


directory = "./output"
output_path = "output.gif"
generate_gif_from_patterns(directory, output_path, duration=10)
