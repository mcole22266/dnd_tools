import os

# Loop through current directory
for path, subdirs, files in os.walk('.'):
    # Loop through files
    for filename in files:
        # Names start with an ID followed by a dash followed by
        # what we care about. Grab the latter
        firstHyphenIndex = filename.find('-')
        newName = filename[firstHyphenIndex+1:]

        # Files are snake_cased. Change that
        newName = newName.replace('_', ' ')

        # Print change to screen
        print('The following files will be updated from THIS -> THAT')
        print(f'    {filename} -> {newName}')

        # Get confirmation
        input('> Press Enter to execute the change ')
        os.rename(filename, newName)
