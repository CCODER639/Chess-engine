from PIL import Image, ImageDraw, ImageFont
import random
import os

os.makedirs("numbers", exist_ok=True)

# Change this if needed
font = ImageFont.truetype("arial.ttf", 24)

for number in range(10):

    for image_number in range(100):

        # Create 28x28 grayscale image
        image = Image.new("L", (28, 28), 0)
        draw = ImageDraw.Draw(image)

        # Random position
        x = random.randint(2, 6)
        y = random.randint(0, 4)

        # Draw digit
        draw.text(
            (x, y),
            str(number),
            font=font,
            fill=random.randint(180, 255)
        )

        # Save
        filename = f"numbers/{number}-{image_number}.png"
        image.save(filename)

print("Finished!")