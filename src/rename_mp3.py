import os
from art import text2art


def display_intro():
    # Display a stylish intro banner
    intro_text = text2art("Rename MP3 Tool")
    print(intro_text)
    print("=" * 50)
    print("Welcome to the Rename MP3 Tool!")
    print("This tool renames all MP3 files in a specified folder.")
    print("Files will be renamed sequentially as 001.mp3, 002.mp3, etc.")
    print("=" * 50)
    print("Author: Mohamed Ahmed Abdel Aziz")
    print("GitHub: https://github.com/abohalema98/rename_mp3_files \n")


def rename_mp3_files():
    try:
        # Display the intro
        display_intro()

        # Prompt the user to enter the folder path
        folder_path = input("Enter the folder path containing MP3 files: ").strip()

        # Check if the folder exists
        if not os.path.isdir(folder_path):
            print("The provided folder path does not exist. Please try again.")
            return

        # Change directory to the target folder
        os.chdir(folder_path)

        # Get all MP3 files in the folder
        mp3_files = sorted(
            [f for f in os.listdir(folder_path) if f.lower().endswith(".mp3")]
        )

        if not mp3_files:
            print("No MP3 files found in the specified folder.")
            return

        # Rename files sequentially
        for index, file_name in enumerate(mp3_files, start=1):
            # Create new name in the format 001.mp3, 002.mp3, etc.
            new_name = f"{index:03d}.mp3"

            # Rename the file
            os.rename(file_name, new_name)
            print(f"Renamed: {file_name} -> {new_name}")

        print("\nAll MP3 files renamed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Entry point
if __name__ == "__main__":
    rename_mp3_files()
