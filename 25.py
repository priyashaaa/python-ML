def copy_file(src_file, dst_file):
    with open(src_file, 'r') as src:
        with open(dst_file, 'w') as dst:
            dst.write(src.read())


src_file = 'source.txt'
dst_file = 'destination.txt'
copy_file(src_file, dst_file)