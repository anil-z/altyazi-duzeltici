import sys


def check_argv():
    if len(sys.argv) < 2:
        print('At least 1 .srt file in arguments')
        sys.exit(0)


def change_content(file_name):
    if file_name[-4:] != '.srt':
        print('Not a .srt file')
        sys.exit(0)

    with open(file_name, 'r') as f:
        text = f.read()
    text.encode('utf-8')

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(text)


if __name__ == '__main__':
    check_argv()
    change_content(file_name=sys.argv[1])
    print('DONE!')
