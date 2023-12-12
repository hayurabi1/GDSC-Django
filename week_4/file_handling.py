import os
import shutil
import time

def is_recently_modified(file_path):
    # Get the modification and creation time of the file
    stat = os.stat(file_path)
    modification_time = stat.st_mtime
    creation_time = stat.st_ctime

    # Get the current time
    current_time = time.time()

    # Calculate the time difference in seconds
    time_diff_modification = current_time - modification_time
    time_diff_creation = current_time - creation_time

    # Check if the file has been modified or created in the last 24 hours
    if time_diff_modification <= 24 * 60 * 60 or time_diff_creation <= 24 * 60 * 60:
        return True
    else:
        return False

def update_files(file_list):
    # Create a folder named "last_24hours" if it doesn't exist
    if not os.path.exists("last_24hours"):
        os.makedirs("last_24hours")

    # Move the identified and updated files to the "last_24hours" folder
    for file_path in file_list:
        # Generate a timestamp
        timestamp = str(int(time.time()))

        # Read the file content
        with open(file_path, 'r') as file:
            content = file.read()

        # Append the timestamp to the content
        updated_content = content + "\nUpdated at: " + timestamp

        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.write(updated_content)

        # Move the file to the "last_24hours" folder
        destination = os.path.join("last_24hours", os.path.basename(file_path))
        shutil.move(file_path, destination)

# Get the list of all files in the current directory
current_directory = os.getcwd()
file_list = [os.path.join(current_directory, file) for file in os.listdir(current_directory) if os.path.isfile(file)]

# Filter the files that have been created or modified in the last 24 hours
recently_modified_files = [file for file in file_list if is_recently_modified(file)]

# Update and move the identified files
update_files(recently_modified_files)