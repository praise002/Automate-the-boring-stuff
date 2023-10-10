
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.
# output folder is same as source folder

import zipfile, os, sys

def backup_to_zip(folder):
    # get the absolute path of the folder
    folder = os.path.abspath(folder)
    # print(f'r"{folder}"')
    # print(folder)
    # get the basename
    base_filename = os.path.basename(folder)
    # print(base_filename)
    
    # Initialize number
    number = 1
    
    # Check if the current base_filename and number exists
    while True:
        zip_filename = f'{base_filename}_{number}.zip'
        full_zip_path = os.path.join(folder, zip_filename)
        # print(f'Initial: {number}')
        number += 1
        # print(f'Final: {number}') 
        
        # Check if the zip file already exists
        if not os.path.exists(full_zip_path):
            break  # If the path does not exist a Unique filename found, exit the loop
        
   
    print(f'Creating {full_zip_path}...')
    
    # Create the zip file
    with zipfile.ZipFile(full_zip_path, 'w', zipfile.ZIP_DEFLATED) as backup_zip_file:
        # TEST: if we leave it like this the folder will be empty
        # backup_zip_file.write(folder)  
        # To avoid this we have to
        # Walk through the folder tree
        # for folder_name, subfolders, filenames in os.walk(folder):
        for folder_name, _, filenames in os.walk(folder):
            print(f'Adding files in {folder_name}')
            backup_zip_file.write(folder_name)

            for filename in filenames:
                # print(filename.startswith(f'{base_filename}_'))
                # print(filename.endswith('.zip'))
                # Check if a backup folder with the basename exists inside the current folder
                if not (filename.startswith(f'{base_filename}_') and filename.endswith('.zip')):
                    backup_zip_file.write(os.path.join(folder_name, filename))
    
    # Print final message
    print('Done.')
    
if __name__ == '__main__':
    # print(len(sys.argv))
    if len(sys.argv) != 2:
        print('Usage: Python backupToZip.py [folder_absolute_path e.g C:\\Users\\Praise Idowu\\Documents...]')
        sys.exit(1)
        
    folder = sys.argv[1]
    backup_to_zip(folder)
        
    