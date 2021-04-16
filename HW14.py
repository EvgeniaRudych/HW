# Create a script that should find the lines by provided pattern in the provided path directory with recursion.
# it means if the directory has other directories,
# the script should get all the info from them as well and threads

import glob
import time
from concurrent.futures import ThreadPoolExecutor


def find_by_pattern(filename, pattern):
    line_container = set()
    with open(filename) as f:
        for line in f:
            if pattern in line:
                line_container.add(line)
    return line_container


def find_all_by_pattern(directory_path, pattern):
    files = glob.glob(f'{directory_path}/**/*.py', recursive=True)
    container = set()
    with ThreadPoolExecutor() as pool:
        result = pool.map(find_by_pattern, files, pattern)
        for res in result:
            container.update(res)
    return container


if __name__ == "__main__":
    start = time.time()
    search_by_pattern = find_all_by_pattern('.', pattern='print')
    end = time.time() - start
    print(f'Search time in {end} seconds')

    for line in search_by_pattern:
        print(line)
