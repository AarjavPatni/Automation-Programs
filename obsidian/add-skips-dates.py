import os
import pendulum

# Set the directory where your markdown files are located
root_directory = r'C:\Users\Aarjav\Documents\Second Brain\Goals'

# Create a list to store the filenames of the markdown files that meet our criteria
matching_files = []

# Recursive function to search for markdown files in all subdirectories


def find_markdown_files(directory):
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isdir(path):
            find_markdown_files(path)
        elif filename.endswith('.md') and filename != r'Trackr.md':
            # Read the contents of the file
            with open(path, 'r', encoding='utf-8') as file:
                contents = file.read()
            # Check if the file contains '# Streak' but not 'day-one: today'
            if '# Streak' in contents and 'day-one: today' not in contents:
                # Add the filename to the list of matching files
                matching_files.append(path)


# Call the function to find markdown files in all subdirectories
find_markdown_files(root_directory)
selected_files = []

# Print the filenames of the matching files
print("Matching files:")
for i, filename in enumerate(matching_files):
    filename_without_extension = filename.split('\\')[-1].replace('.md', '')
    choice = input(f'{filename_without_extension} ')
    if choice.lower() in ('y', ''):
        print(
            "\x1b[1A" + f"\x1b[{len(choice) + len(filename_without_extension)}C" + " ✅")
    else:
        print(
            "\x1b[1A" + f"\x1b[{len(choice) + len(filename_without_extension)}C" + " ❌")
    selected_files.append(filename) if choice.lower() in ('y', '') else None

yesterday = pendulum.yesterday().to_date_string()

# Loop through the selected files
for filename in selected_files:
    # Read the contents of the file
    with open(filename, 'r') as file:
        contents = file.read()
    lines_list = contents.split('\n')
    # Find the second '---' and add a line above it with today's date in the format YYYY-MM-DD with '- ' prepended
    target_string = lines_list.index('---', 1)
    contents = '\n'.join(
        lines_list[:target_string] + [f'- {yesterday}'] + ['---'] + lines_list[target_string + 1:])
    # Write the modified contents back to the file
    with open(filename, 'w') as file:
        file.write(contents)
