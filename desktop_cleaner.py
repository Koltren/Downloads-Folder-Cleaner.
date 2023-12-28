import os
import shutil

def get_downloads_path():
    return os.path.join(os.path.expanduser("~"), "Downloads")

def list_files_in_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return files

def categorize_and_move_files(files, category_types, category_folder):
    for file in files:
        file_extension = os.path.splitext(file)[1].lower()

        if file_extension in category_types:
            move_to_folder(file, category_folder)

def move_to_folder(file, folder):
    folder_path = os.path.join(get_downloads_path(), folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    shutil.move(os.path.join(get_downloads_path(), file), os.path.join(folder_path, file))

def calculate_and_display_space_reclaimed(files, initial_size):
    total_size_before = initial_size
    total_size_after = sum(os.path.getsize(os.path.join(get_downloads_path(), file)) for file in files)
    space_reclaimed = total_size_before - total_size_after

    print(f"Space reclaimed: {space_reclaimed / (1024 * 1024):.2f} MB")

def delete_unwanted_files():
    unwanted_types = ['.tmp', '.log', '.bak']

    for file in os.listdir(get_downloads_path()):
        file_path = os.path.join(get_downloads_path(), file)
        file_extension = os.path.splitext(file)[1].lower()

        if os.path.isfile(file_path) and file_extension in unwanted_types:
            os.remove(file_path)

def main():
    print("Hello, Downloads Folder Cleaner!")

    # Display progress messages
    print("Listing files in Downloads...")

    # Get a list of files in Downloads
    files_in_downloads = list_files_in_folder(get_downloads_path())

    print(f"Found {len(files_in_downloads)} files in Downloads.")

    # Display progress message
    print("Organizing files into categories...")

    # Define category types and folders
    document_types = ['.txt', '.doc', '.docx', '.pdf']
    image_types = ['.png', '.jpg', '.jpeg', '.gif']  # Updated line
    video_types = ['.mp4', '.avi', '.mkv']
    music_types = ['.mp3', '.wav']
    app_types = ['.exe', '.msi']

    # Categorize and move the files
    categorize_and_move_files(files_in_downloads, document_types, 'Documents')
    categorize_and_move_files(files_in_downloads, image_types, 'Images')
    categorize_and_move_files(files_in_downloads, video_types, 'Videos')
    categorize_and_move_files(files_in_downloads, music_types, 'Music')
    categorize_and_move_files(files_in_downloads, app_types, 'Apps')

    # Display completion message
    print("Downloads folder cleaning process completed successfully!")

    # Calculate and display space reclaimed
    initial_size = sum(os.path.getsize(os.path.join(get_downloads_path(), file)) for file in files_in_downloads)
    calculate_and_display_space_reclaimed(files_in_downloads, initial_size)

    # Delete unwanted files
    delete_unwanted_files()

    # Display completion message
    print("Unwanted files deleted successfully!")

# Entry point of the program
if __name__ == "__main__":
    main()
