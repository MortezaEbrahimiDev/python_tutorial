# imports and variables
 
from pathlib import Path
import shutil



base_dir=Path(r"C:\\Users\\ebrahimee.morteza\\Desktop")
target_dir=base_dir / "sorted"
# declare categories and extentions

FILE_CATEGORIES={
    "Images":[".jpeg",".png"],
    "Videos":[".mp4",".mkv"],
    "Docs":[".pdf",".conf",".txt",".xlsx"]
}

# create directories base on categories
def create_categories_directories():
    for category,_ in FILE_CATEGORIES.items():
        (target_dir / category).mkdir(parents=True,exist_ok=True)


# search and categorize files

def search_and_categorize_files():
    for file in base_dir.glob("*"):
        for category,extentions in FILE_CATEGORIES.items():
            if file.suffix in extentions:
                shutil.copy(file,target_dir / category)

# run the App

search_and_categorize_files()
