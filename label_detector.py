import tqdm
from rekognition import detect_labels
import csv
import os


def get_basename(file_path):
    base_name, _ = os.path.splitext(file_path)
    return base_name


def run(bucket: str, folder: str, filenames: list):

    out_dir = os.path.join(os.getcwd(), 'labels')
    os.path.exists(out_dir) or os.makedirs(out_dir)

    for filename in tqdm.tqdm(filenames):
        file_path = f"{folder}/{filename}"
        labels = detect_labels(file_path, bucket)

        basename = get_basename(filename)
        f = open(f"{out_dir}/{basename}.csv", "w")
        data = [["Label", "Confidence"]]
        for label in labels:
            data.append([label['Name'], label['Confidence']])

        writer = csv.writer(f)
        writer.writerows(data)
        f.close()

    print("Labeling complete.")
