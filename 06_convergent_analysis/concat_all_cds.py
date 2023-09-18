import os
import argparse

def concat_seqfile(input_dir, output_file):

    input_path = os.path.abspath(input_dir)
    output_file = os.path.abspath(output_file)

    with open(output_file, 'w') as fw:
        for file in os.listdir(input_path):
            file_path = os.path.join(input_path, file)
            with open(file_path, 'r') as fin:
                fw.write(fin.read())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Put all CDSs in the input directory into the output file.')

    parser.add_argument('input_dir', type=str, help="input directory")
    parser.add_argument('output', type=str, help="path of the output file")

    args = parser.parse_args()

    concat_seqfile(args.input_dir, args.output)