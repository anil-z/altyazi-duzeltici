import os
import sys


def change_content(file_name):
    if file_name[-4:] != '.srt':
        print('Not a .srt file')
        sys.exit(0)

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


if __name__ == '__main__':
    all_files = [f for f in os.listdir('.') if os.path.isfile(f)]

    srt_files_argv = list(filter(filter_srt, sys.argv))
    srt_files_all = list(filter(filter_srt, all_files))

    if sys.argv[1] == '.':
        for f_name in srt_files_all:
            change_content(f_name)
    elif sys.argv[1][-4:] == '.srt':
        for f_name in srt_files_argv:
            change_content(f_name)
