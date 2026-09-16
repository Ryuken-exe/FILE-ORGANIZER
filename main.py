from pathlib import Path
import shutil


# File categories and extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "PDFs": [".pdf"],
    "Music": [".mp3", ".wav"],
    "Docx": [".docx"],
    "Excel": [".xlsx", ".csv"],
    "Others Files": [".exe", ".zip"],
    "Python Files": [".py"],
    "Java Files": [".java"],
    "C++ Files": [".cpp"],
    "HTML": [".html", ".css", ".js"],
    "NOTES" : [".txt"]
}


def get_category(extension):
    """Return the category for a file extension."""

    extension = extension.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_path(destination):
    """Return a unique path if the destination file already exists."""

    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = f"{destination.stem}_{counter}{destination.suffix}"
        new_path = destination.parent / new_name

        if not new_path.exists():
            return new_path

        counter += 1


def organize_files(folder):
    """Organize files inside the given folder."""

    moved = 0
    skipped = 0
    errors = 0

    for file in folder.iterdir():

        # Ignore folders
        if not file.is_file():
            continue

        extension = file.suffix.lower()
        category = get_category(extension)

        # Create category folder
        category_folder = folder / category
        category_folder.mkdir(exist_ok=True)

        # Create destination path
        destination = category_folder / file.name

        # Handle duplicate filenames
        destination = get_unique_path(destination)

        try:
            shutil.move(str(file), str(destination))

            print(f"✓ {file.name} → {category}/{destination.name}")
            moved += 1

        except PermissionError:
            print(f"✗ Permission denied: {file.name}")
            errors += 1

        except OSError as error:
            print(f"✗ Could not move {file.name}: {error}")
            errors += 1

    return moved, skipped, errors


def main():
    while True:

        print("\n==============================")
        print("       FILE ORGANIZER")
        print("==============================")
        print("1. Organize Folder")
        print("2. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "2":
            print("\nGoodbye!")
            break

        if choice != "1":
            print("Invalid choice. Please try again.")
            continue

        path = input("\nEnter folder path: ").strip()

        folder = Path(path)

        # Validate path
        if not folder.exists():
            print("✗ Invalid path.")
            continue

        if not folder.is_dir():
            print("✗ The provided path is not a folder.")
            continue

        print("\nOrganizing files...\n")

        moved, skipped, errors = organize_files(folder)

        print("\n==============================")
        print("      ORGANIZATION DONE")
        print("==============================")
        print(f"Files moved : {moved}")
        print(f"Files skipped: {skipped}")
        print(f"Errors      : {errors}")


if __name__ == "__main__":
    main()