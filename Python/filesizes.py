import os
files = {name: os.path.getsize(name) for name in os.listdir() if os.path.isfile(name)}

sorted_files = sorted(files.items(), key=lambda x: x[1], reverse=True)

for name, size in sorted_files:
    print(f"{name} : {size} bytes")