import os
import argparse


def change_encoding(file_name):
    if file_name[-4:] != '.srt':
        print('Dosya uzantısı .srt değil!')
        exit(0)

    try:
        with open(file_name, 'rb') as f:
            text = f.read()
        
        text = text.decode("iso-8859-9")
        with open(file_name, 'w') as f:
            f.write(text)

        print(f'DONE {file_name}')
    except UnicodeDecodeError as e:
        print(e)
        print(f'Passing {file_name}')


def parse_args():
    parser = argparse.ArgumentParser(description='Klasördeki srt dosyalarındaki türkçe karakter sorununu düzeltir')
    parser.add_argument('directory', type=str, help='Srt dosyalarının bulunduğu klasör')
    args = parser.parse_args()

    return args.directory


def main():
    directory = parse_args()

    all_files = [f for f in os.listdir(directory) if os.path.isfile(f)]
    srt_files = list(filter(lambda x: x.split(".")[-1] == "srt", all_files))

    for f_name in srt_files:
        change_encoding(f_name)


if __name__ == '__main__':
    main()
