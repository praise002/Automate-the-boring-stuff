import os, sys

# You can also use the file_path instead of stating old_filename again as it is the same as file_path
# But I find it more readable by stating it
# For more flexibility the user can add as many prefix as possible
# You could make the program disallow user from adding prefix when it gets to a max number
# In removing it follows (LIFO) - Last In First Out

"""
    Here's an example to illustrate how the program works:
    
    rename_files_with_prefix
    Original Filename: filename.txt
    After Processing: prefix1_filename.txt
    This is useful if you want to add prefix in a specific order
    
    remove_prefix_from_files
    Original Filename: prefix3_prefix2_prefix1_filename.txt
    After Processing: prefix2_prefix3_filename.txt
    The program is useful in scenarios where you have filenames that follow this specific 
    naming convention and you want to remove the most recently added prefix from the filename. 
    This can be helpful in organizing files or cleaning up filenames that have accumulated prefixes over time.

    However, if you need to remove prefixes in a different order or have more complex renaming requirements, 
    you may need to modify the code accordingly to suit your specific use case. The provided code is a starting 
    point and can be customized to meet your unique requirements for renaming files based on their naming conventions and prefixes.
"""       
            
def rename_files_with_prefix(root_dir, prefix):
    for filename in os.listdir(root_dir):
        file_path = os.path.join(root_dir, filename)
        if os.path.isfile(file_path):
            old_filename = os.path.join(root_dir, filename)
            new_filename = os.path.join(root_dir, f'{prefix}_{filename}')
            os.rename(old_filename, new_filename)
            print(f'Renamed: {old_filename} to {new_filename}')
            
def remove_prefix_from_files(root_dir):
    for filename in os.listdir(root_dir):
        file_path = os.path.join(root_dir, filename)
        old_filename = os.path.join(root_dir, filename)
        if os.path.isfile(file_path):
            if '_' not in filename:
                print(f'{filename} cannot be renamed because it doesn\'t have a prefix.')
            else:
                splitted_filename = filename.split('_')
                print(splitted_filename)
                print(splitted_filename[1:])
                # print(len(splitted_filename[1:]))
                if len(splitted_filename) > 1:
                    new_name = '_'.join(splitted_filename[1:])
                    print(new_name)
                    new_filename = os.path.join(root_dir, new_name)
                    os.rename(old_filename, new_filename)
                    print(f'Renamed: {filename} to {new_name}')
                                       

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: Python main.py [root_dir] [prefix]')
        print('The [prefix] is optional. \nIf you did not specify a prefix the program will assume you want to remove a prefix.')
        print('Prefix are removed based on the order that they are added.')
        sys.exit(1)
        
    root_dir = sys.argv[1]
    
    # It assumes the user wants to add prefix to a filename
    if len(sys.argv) == 3:
        prefix = sys.argv[2]
        rename_files_with_prefix(root_dir, prefix)
    else:
        remove_prefix_from_files(root_dir)
    