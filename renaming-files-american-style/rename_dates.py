import os, shutil, re

def rename_files():
   # Create a regex pattern for American-style dates (MM-DD-YYYY)
   # \d 0-9, 2, 4- exactly two and four digits must be matched
    date_pattern = re.compile(r'(\d{2})-(\d{2})-(\d{4})')
    root_dir = 'dates/'
    # Get the current working directory
    # os.chdir('dates/')
    # current_directory = os.getcwd()
    # print(current_directory)
    # Loop through all files in the current directory
    # for filename in os.listdir(current_directory):
    for filename in os.listdir('dates2/'):
        # print(filename)
        # Check if the filename contains a date in American style
        match = date_pattern.search(filename)
        # print(match)
        if match:
            # Extract the date components
            month, day, year = match.groups()  # returns a tuple
            # print(match.groups())
            # Rename the file with European-style date (DD-MM-YYYY)
            """retrieves the part of the original filename that comes after the matched date pattern
            It uses the match.end() method, which returns the index of the end of the last match 
            (i.e., the end of the date pattern) in the filename string. By slicing the filename 
            string from that index to the end ([match.end():]), 
            you effectively retain the part of the filename that comes after the date pattern.
            """
            # new_filename = f'{filename.split("_")[0]}_{day}-{month}-{year}{filename[match.end():]}'
            new_filename = f'{filename[:match.start()]}{day}-{month}-{year}{filename[match.end():]}'
            # print(new_filename)
            
            # old_filepath = filename
            # new_filepath = new_filename
            
            old_filepath = os.path.join(root_dir, filename)
            new_filepath = os.path.join(root_dir, new_filename)
            
            # Rename the file using shutil.move()
            # print(f'Old file is {old_filepath}')
            # print(f'New file is {new_filepath}')
            shutil.move(old_filepath, new_filepath)
            print(f'Renamed: {filename} -> {new_filename}')
    
if __name__ == '__main__':
    rename_files()