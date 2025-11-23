import os

# --- CONFIG ---
ROOT_DIR = "."  # repo root (where this script is)
OUTPUT_FILE = "README.md"
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".bmp")

# --- HEADER TEMPLATE ---
README_HEADER = """# 🖼️ Wallpaper Collection

ALL CREDITS GOES TO RESPECTIVE CREATORS / CONTRIBUTORS

A curated collection of wallpapers organized by categories.
Click any thumbnail below to view the full-resolution image!

---
"""

README_FOOTER = """
---
### 🛠️ Contribution
FOR CONTRIBUTION: **FORK THIS REPO, ADD YOUR WALLPAPER FOLDER, GENERATE NEW README, THEN OPEN A PR.**
"""

def generate_markdown():
    lines = [README_HEADER]

    # Only get first-level directories
    for folder in sorted(os.listdir(ROOT_DIR)):
        folder_path = os.path.join(ROOT_DIR, folder)

        # Skip files, hidden folders, this script, README, etc.
        if not os.path.isdir(folder_path) or folder.startswith(".") or folder == "__pycache__":
            continue

        # Collect image files in this folder
        images = [
            f for f in sorted(os.listdir(folder_path))
            if f.lower().endswith(IMAGE_EXTENSIONS)
        ]

        if not images:
            continue

        # Folder title
        lines.append(f"## 📁 {folder}\n")

        # Add image thumbnails
        for img in images:
            img_path = f"{folder}/{img}".replace("\\", "/")
            lines.append(f'<a href="{img_path}"><img src="{img_path}" width="200"/></a> ')

        lines.append("\n---\n")

    lines.append(README_FOOTER)
    return "\n".join(lines)


def main():
    md_content = generate_markdown()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(md_content)
    print("✅ README.md generated (non-recursive, credits + contribution info added)!")

if __name__ == "__main__":
    main()
