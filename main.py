import requests
from PIL import Image
import os
import sys

def show_update_message():
    print("\033[92mWelcome to the Watermark Script!\033[0m")  # Print the message in green color
    print("\033[92mCurrent Version : 1.0.0\033[0m")  # Print the message in green color


    # Print the rest of the message
    print("\n--------------------------------------------------------------")
    print("Please visit \033[91mhttps://erfannoyon.com/water-mark-script-update.php\033[0m")
    print("to check for the latest updates of this script before proceeding.")
    print("--------------------------------------------------------------\n")

def watermark_images(image_folder, logo_path, output_folder):
    # Open the logo image
    logo = Image.open(logo_path)
    logo = logo.convert("RGBA")  # Convert logo to RGBA mode
    logo_width, logo_height = logo.size

    # Iterate through images in the folder
    for filename in os.listdir(image_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Open the image
            image_path = os.path.join(image_folder, filename)
            image = Image.open(image_path)
            image_width, image_height = image.size

            # Calculate position for the watermark (bottom-right corner with padding)
            position = (image_width - logo_width - 10, image_height - logo_height - 10)

            # Paste the logo onto the image
            image.paste(logo, position, logo)

            # Save the watermarked image to the output folder
            output_path = os.path.join(output_folder, filename)
            image.save(output_path)

            print(f"✓ Watermark added to {filename}")

def confirm_execution():
    while True:
        user_input = input("\nDo you wish to start with this version? (yes/no): ").strip().lower()
        if user_input in ['yes', 'y']:
            return True
        elif user_input in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    # Print the update message
    show_update_message()

    # Ask for confirmation
    if confirm_execution():
        # Define input and output folders
        image_folder = "images"
        logo_path = "logo.png"
        output_folder = "watermarked_images"

        # Create output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Call the function to watermark images
        watermark_images(image_folder, logo_path, output_folder)
    else:
        print("Script execution aborted.")
