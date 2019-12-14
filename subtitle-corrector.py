import os
import argparse


def change_content(file_name):
    if file_name[-4:] != '.srt':
        print('Not a .srt file')
        exit(0)

    try:
        with open(file_name, 'r') as f:
            text = f.read()
        text.encode('utf-8')

        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(text)

        print(f'DONE {file_name}')
    except UnicodeDecodeError:
        print(f'Passing {file_name}')


def filter_srt(file_name):
    return file_name[-4:] == '.srt'


def parse_args():
    parser = argparse.ArgumentParser(description='Change the encoding of srt files to utf-8')
    parser.add_argument('directory', type=str, help='Directory location of the srt files')
    args = parser.parse_args()

    return args.directory


if __name__ == '__main__':
    directory = parse_args()

    all_files = [f for f in os.listdir(directory) if os.path.isfile(f)]
    srt_files = list(filter(filter_srt, all_files))

    for f_name in srt_files:
        change_content(f_name)
