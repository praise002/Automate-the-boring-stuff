# To rename filenames with European-style dates to American-style dates

import os, shutil, re, sys

def rename_files(root_dir):
   # Create a regex pattern for American-style dates (MM-DD-YYYY)
   # \d 0-9, 2, 4- exactly two and four digits must be matched
    date_pattern = re.compile(r'(\d{2})-(\d{2})-(\d{4})')
    
    # Loop through all files in the current directory
    for filename in os.listdir(root_dir):
        # print(filename)
        # Check if the filename contains a date in American style
        match = date_pattern.search(filename)
        # print(match)
        if match:
            # Extract the date components
            month, day, year = match.groups()  # returns a tuple
            # print(match.groups())
            # Rename the file with European-style date (DD-MM-YYYY)
            new_filename = f'{day}-{month}-{year}{filename[match.end():]}'
            # print(new_filename)
            
            old_filepath = os.path.join(root_dir, filename)
            new_filepath = os.path.join(root_dir, new_filename)
            
            # Rename the file using shutil.move()
            shutil.move(old_filepath, new_filepath)
            print(f'Renamed: {filename} -> {new_filename}')
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python main.py [root_dir]')
        exit(1)
    
    try:
        root_dir = sys.argv[1]  
        rename_files(root_dir)
    except FileNotFoundError as e:
        print(e)
    