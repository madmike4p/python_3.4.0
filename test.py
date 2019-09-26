import os
import glob 

PATH = os.path.abspath('.')

files = []

for r, d, f in os.walk(PATH):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))

for f in files:
    op = open(f, 'r')
    line = op.read()
    op.close()

    newLine = line.replace('_static', 'static')
    newLine = newLine.replace('_sources', 'sources')
    newLine = newLine.replace('_images', 'images')

    op = open(f, 'w')
    op.write(newLine)
    op.close()
