import os
import re
from pathlib import Path

def fill_gaps(prefix, directory):
    # Compile regex pattern
    sequence_regex = re.compile(rf'^({prefix})(\d+)(\.\w+)?$', re.IGNORECASE)

    # Extract numbers from files
    files = os.listdir(directory)
    numbers = [int(sequence_regex.search(f).group(2)) for f in files if sequence_regex.search(f)]

    # Check if numbers list is not empty
    if not numbers:
        print(f"No files found with prefix '{prefix}' in directory '{directory}'.")
        return

    # Find gaps
    gaps = [i for i in range(min(numbers), max(numbers)+1) if i not in numbers]

    # Print gaps
    print("Gaps:")
    print(gaps)

    # Rename files to fill gaps
    files = [f for f in os.listdir(directory) if sequence_regex.search(f)]
    files.sort(key=lambda x: int(re.search(r'\d+', x).group()))

    for i, file in enumerate(files):
        num = min(numbers) + i
        filename, extension = sequence_regex.search(file).group(1), sequence_regex.search(file).group(3) or ''
        new_file = f"{filename}{num:03}{extension}"
        os.rename(Path(directory) / file, Path(directory) / new_file)


# Example usage
fill_gaps('spam', f'C:\\Users\\maak\\spam')