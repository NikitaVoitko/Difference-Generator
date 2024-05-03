import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', metavar='first_file', type=str,
                        help='Path to the first configuration file')
    parser.add_argument('second_file', metavar='second_file', type=str,
                        help='Path to the second configuration file')
    parser.add_argument('-f', '--format', help='set format of output')
    # args = parser.parse_args()


if __name__ == '__main__':
    main()
