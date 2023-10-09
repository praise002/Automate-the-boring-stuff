import os, shutil, sys
         
            
def rename_files_with_prefix(root_dir, prefix):
    for filename in os.listdir(root_dir):
        # print(filename)
        file_path = os.path.join(root_dir, filename)
        if os.path.isfile(file_path):
            print(filename)
            # print(f'spam_{filename}')
            old_filename = os.path.join(root_dir, filename)
            # new_filename = os.path.join(root_dir, f'spam_{filename}')
            new_filename = os.path.join(root_dir, f'{prefix}_{filename}')
            # shutil.move(old_filename, new_filename)
            os.rename(old_filename, new_filename)
            
def remove_prefix_from_files(root_dir):
    for filename in os.listdir(root_dir):
        file_path = os.path.join(root_dir, filename)
        old_filename = os.path.join(root_dir, filename)
        if os.path.isfile(file_path):
            if '_' not in filename:
                print(f'{filename} cannot be renamed because it doesn\'t have a prefix.')
            else:
                splitted_filename = filename.split('_')
                # print(splitted_filename)
                # print(splitted_filename[1:])
                # print(len(splitted_filename[1:]))
                if len(splitted_filename) == 3:
                    splitted_filename_list = splitted_filename[1:]
                    # old_filename = os.path.join(root_dir, filename)
                    # print(old_filename)
                    new_name = f'{splitted_filename_list[0]}_{splitted_filename_list[1]}'
                    # print(new_name)
                    new_filename = os.path.join(root_dir, new_name)
                    # print(new_filename)
                    os.rename(old_filename, new_filename)
                else:
                    # old_filename = os.path.join(root_dir, filename)
                    print(old_filename)
                
                    

if __name__ == '__main__':
    # if len(sys.argv) != 3:
    #     print('Usage: Python main.py [root_dir] [prefix]')
    #     sys.exit(1)
        
    root_dir = sys.argv[1]
    # prefix = sys.argv[2]
    
    # rename_files_with_prefix(root_dir, prefix)
    remove_prefix_from_files(root_dir)
    
# TODO: Make the code neater
    