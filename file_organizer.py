# ============================================
# Synent Technologies - Python Internship
# Task 5: File Organizer (Intermediate Level)
# Developer: Lincoln Adura
# ============================================

import os
import shutil

# File type categories and their extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx",
                  ".ppt", ".pptx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c",
             ".json", ".xml"],
    "Others": []
}

def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return

    print(f"\n📂 Organizing folder: {folder_path}")
    print("=" * 50)

    files_moved = 0
    files_skipped = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip directories and hidden files
        if os.path.isdir(file_path) or filename.startswith("."):
            files_skipped += 1
            continue

        # Get file extension and category
        _, extension = os.path.splitext(filename)
        if not extension:
            files_skipped += 1
            continue

        category = get_category(extension)

        # Create category folder if it doesn't exist
        category_folder = os.path.join(folder_path, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
            print(f"📁 Created folder: {category}")

        # Move file to category folder
        destination = os.path.join(category_folder, filename)

        # Handle duplicate filenames
        if os.path.exists(destination):
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(destination):
                new_filename = f"{base}_{counter}{ext}"
                destination = os.path.join(category_folder, new_filename)
                counter += 1

        shutil.move(file_path, destination)
        print(f"✅ Moved: {filename} → {category}/")
        files_moved += 1

    print("=" * 50)
    print(f"\n📊 Organization Complete!")
    print(f"   ✅ Files moved: {files_moved}")
    print(f"   ⏭️  Files skipped: {files_skipped}")
    print("=" * 50)

def file_organizer():
    print("=" * 50)
    print("  Synent Technologies - File Organizer")
    print("        Intermediate Level Task 5")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("  1. Organize a folder")
        print("  2. View supported file categories")
        print("  3. Exit")
        print("-" * 50)

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            folder_path = input("\nEnter the full folder path to organize: ").strip()
            confirm = input(f"\n⚠️  Are you sure you want to organize this folder? (yes/no): ").strip().lower()
            if confirm == "yes":
                organize_folder(folder_path)
            else:
                print("❌ Organization cancelled.")

        elif choice == "2":
            print("\n📋 Supported File Categories:")
            print("=" * 50)
            for category, extensions in FILE_CATEGORIES.items():
                if extensions:
                    print(f"  📁 {category}: {', '.join(extensions)}")
                else:
                    print(f"  📁 {category}: All other file types")
            print("=" * 50)

        elif choice == "3":
            print("\nGoodbye! Keep your files organized! 👋")
            break

        else:
            print("❌ Invalid choice! Please select 1-3.")

if __name__ == "__main__":
    file_organizer()