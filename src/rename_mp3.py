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


def get_folder_path():
    display_intro()
    folder_path = input("Enter the folder path containing files: ").strip()
    if not os.path.isdir(folder_path):
        raise ValueError("The provided folder path does not exist.")
    return folder_path


def get_file_extension():
    file_extension = (
        input("Enter the desired file extension (e.g., 'mp3', 'png'): ")
        .strip()
        .lstrip(".")
    )
    if not file_extension:
        raise ValueError("Invalid file extension.")
    return file_extension


def rename_files(folder_path, file_extension):
    os.chdir(folder_path)
    files = sorted(os.listdir(folder_path))

    if not files:
        print("No files found in the specified folder.")
        return

    for index, file_name in enumerate(files, start=1):
        _, current_extension = os.path.splitext(file_name)
        if not current_extension or current_extension.lstrip(".") == file_extension:
            continue

        new_name = f"{index:03d}.{file_extension}"
        os.rename(file_name, new_name)
        print(f"Renamed: {file_name} -> {new_name}")

    print("\nAll files renamed successfully.")


def rename_files_with_chosen_extension():
    try:
        folder_path = get_folder_path()
        file_extension = get_file_extension()
        rename_files(folder_path, file_extension)
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    rename_files_with_chosen_extension()
