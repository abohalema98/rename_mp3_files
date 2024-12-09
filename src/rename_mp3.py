import os

# Folder containing your MP3 files
folder_path = r"D:\\New folder"  # Replace with the path to your folder


def rename_mp3_files(folder_path):
    try:
        # Change directory to the target folder
        os.chdir(folder_path)

        # Get all MP3 files in the folder
        mp3_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".mp3")])

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


# Call the function
rename_mp3_files(folder_path)


# import os


# def rename_mp3_files():
#     try:
#         # Prompt the user to enter the folder path
#         folder_path = input("Enter the folder path containing MP3 files: ").strip()

#         # Check if the folder exists
#         if not os.path.isdir(folder_path):
#             print("The provided folder path does not exist. Please try again.")
#             return

#         # Change directory to the target folder
#         os.chdir(folder_path)

#         # Get all MP3 files in the folder
#         mp3_files = sorted(
#             [f for f in os.listdir(folder_path) if f.lower().endswith(".mp3")]
#         )

#         if not mp3_files:
#             print("No MP3 files found in the specified folder.")
#             return

#         # Rename files sequentially
#         for index, file_name in enumerate(mp3_files, start=1):
#             # Create new name in the format 001.mp3, 002.mp3, etc.
#             new_name = f"{index:03d}.mp3"

#             # Rename the file
#             os.rename(file_name, new_name)
#             print(f"Renamed: {file_name} -> {new_name}")

#         print("\nAll MP3 files renamed successfully.")

#     except Exception as e:
#         print(f"An error occurred: {e}")


# # Call the function
# if __name__ == "__main__":
#     rename_mp3_files()
