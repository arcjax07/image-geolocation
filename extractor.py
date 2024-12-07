import os
import zipfile
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm


def extract_zip(zip_path):
    root = os.path.dirname(zip_path)
    try:
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(root)
        os.remove(zip_path)
    except Exception as e:
        print(f"Error processing {zip_path}: {e}")


def main():
    print("Collecting zip files...")
    zip_files = []
    for root, dirs, files in os.walk("data/osv5m_streetview_cropped/images"):
        for file in files:
            if file.endswith(".zip"):
                zip_files.append(os.path.join(root, file))

    max_workers = max(os.cpu_count() // 2, 1)
    print(f"Extracting {len(zip_files)} files using {max_workers} workers...")
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        list(
            tqdm(
                executor.map(extract_zip, zip_files),
                total=len(zip_files),
                desc="Extracting",
            )
        )


if __name__ == "__main__":
    main()
