#!/Users/anilzeybek/opt/miniconda3/bin/python3

import os
import argparse
import chardet

lookup_table = {
    'â€¢': '•',
    'â€œ': '“',
    'â€': '”',
    'â€˜': '‘',
    'â€™': '’',
    'Ý¾': 'İ',
    'Ý': 'İ',
    'Ä°': 'İ',
    'Ã': 'İ',
    'â€¹': 'İ',
    '&Yacute;': 'İ',
    'ý': 'ı',
    'Ä±': 'ı',
    'Â±': 'ı',
    'Ã½': 'ı',
    'Ã›': 'ı',
    'â€º': 'ı',
    '&yacute;': 'ı',
    'Þ': 'Ş',
    'Åž': 'Ş',
    'Ã…Å¸': 'Ş',
    'Ã¥Ã¿': 'Ş',
    '&THORN;': 'Ş',
    'þ': 'ş',
    'Å?': 'ş',
    'ÅŸ': 'ş',
    '&thorn;': 'ş',
    'Ð': 'Ğ',
    'Äž': 'Ğ',
    'ð': 'ğ',
    'Ä?': 'ğ',
    'ÄŸ': 'ğ',
    '&eth;': 'ğ',
    'Ã°': 'ğ',
    'Ã‡': 'Ç',
    'Ã?': 'Ç',
    '&Ccedil;': 'Ç',
    'Ã§': 'ç',
    '&ccedil;': 'ç',
    'Ã–': 'Ö',
    '&Ouml;': 'Ö',
    'Ã¶': 'ö',
    '&ouml;': 'ö',
    'Ãœ': 'Ü',
    '&Uuml;': 'Ü',
    'ÃƒÂ¼': 'ü',
    'Ã£Â¼': 'ü',
    'Ã¼': 'ü',
    '&uuml;': 'ü',
}


def change_encoding(file_name):
    with open(file_name, 'rb') as f:
        text = f.read()

    encoding = chardet.detect(text)['encoding']
    text = text.decode(encoding)
    
    for key, value in lookup_table.items():
        text = text.replace(key, value)

    with open(file_name, 'w') as f:
        f.write(text)

    print(f'Bitti: {file_name}')


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
