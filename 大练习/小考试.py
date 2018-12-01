import os
for root, dirs, files in os.walk("D:\E"):
    for dir in dirs:
        print(os.path.join(root, dir))
    for file in files:
        print(os.path.join(root, file))
