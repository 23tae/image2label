from variables import get_variables
from label_detector import run


def main():
    bucket, folder, filenames = get_variables()
    run(bucket, folder, filenames)


if __name__ == '__main__':
    main()
