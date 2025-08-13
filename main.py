from PIL import Image

def encrypt_decrypt_image(input_path, output_path, key):
    try:
        # Open the image
        img = Image.open(input_path)
        pixels = img.load()  # Access pixel data

        # Loop through every pixel
        for x in range(img.width):
            for y in range(img.height):
                r, g, b = pixels[x, y]
                # XOR operation on each RGB value
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)

        # Save the modified image
        img.save(output_path)
        print(f"\n Process completed successfully!")
        print(f"Input Image : {input_path}")
        print(f"Output Image: {output_path}")
        print(f"Key Used    : {key}")
    except FileNotFoundError:
        print("\n Error: The specified input file was not found.")
    except Exception as e:
        print(f"\n An error occurred: {e}")

# ---------------- Main Program ----------------
print("=" * 45)
print("       Simple Image Encryption Tool")
print("=" * 45)
print("1) Encrypt Image")
print("2) Decrypt Image (use same key)")
print("=" * 45)

choice = input("Select option (1 or 2): ")

# Ask for file paths and key
input_file = input("\nEnter input image path (e.g., mypic.png): ")
output_file = input("Enter output image path (e.g., encrypted.png): ")
key = int(input("Enter numeric key (0-255): "))

# Perform operation
encrypt_decrypt_image(input_file, output_file, key)

print("\n💡 Note: For decryption, use the encrypted image as input and the SAME key used for encryption.")