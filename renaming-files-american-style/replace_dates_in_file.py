import re, os

# Function to replace American-style dates with European-style dates
def replace_dates_in_file(file_path):
    # Loop through the files
    for filename in os.listdir(file_path):
        # print(filename)
        # Read the content of the file
        file_path2 = os.path.join(file_path, filename)
        
        with open(file_path2, 'r') as file:
            file_content = file.read()
            # print(file_content)
    
        
        # Create a regex pattern for American-style dates (MM-DD-YYYY)
        date_pattern = re.compile(r'(\d{2})-(\d{2})-(\d{4})')
        match = date_pattern.search(file_content)
        # print(match)
        iters = date_pattern.finditer(file_content)
        for iter in iters:
            print(iter)
    # Replace American-style dates with European-style dates (DD-MM-YYYY)
    def replace_date(match):
        month, day, year = match.groups()
        return f'{day}-{month}-{year}'
    
    updated_content = date_pattern.sub(replace_date, file_content)
    # print(updated_content)
        
if __name__ == '__main__':
    file_path = 'data2/'
    replace_dates_in_file(file_path)
    
# TODO: Learn regex and fix it