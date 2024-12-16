import os

file = open("tableofcontents.txt")
lines = file.readlines()

orig_dir = os.getcwd()

for i, line in enumerate(lines):
    if line.strip()[-1].isdigit():
        dig = int(line.strip()[-1])
        dir = line.strip()[:-2].strip()
        os.mkdir(dir)
        os.chdir(dir)
        f = open("README.md","a")
        f.write("# "+dir)
        f.write("\n")
        for j in range(dig):
            f.write("- "+ lines[i+1+j])
        f.close()
        os.chdir(orig_dir)

# # Specify the directory name
# directory = "new_directory"

# # Create the directory if it doesn't exist
# if not os.path.exists(directory):
#     os.makedirs(directory)
#     print(f"Directory '{directory}' created.")
# else:
#     print(f"Directory '{directory}' already exists.")
