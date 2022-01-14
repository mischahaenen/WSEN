import sys
'''
x - Create - will create a file, returns an error if the file exist
r - Read. The stream beginning of file.
r+- Read/Write. The stream beginning of file.
w - Delete content for Read. The stream beginning of file.
w+- Delete content for Read/Write. The stream beginning of file.
a - Read. The stream end of file.
a+- Read/Write. The stream end of file.
'''
# Zugriffsversuch
try:
    d = open("schreiben.txt","w+")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)
# Write
d.write("Die erste Zeile\n")
for i in range(2,11,2):
    d.write(str(i) + " ")
    d.write("\n")
# Writelines
x = ["abc\n", str(12/7.5)+"\n", "xyz\n"]
d.writelines(x)
# Readline
zeile1 = d.readline()
print(zeile1, end="")
# Readlines
allezeilen = d.readlines()
summe = 0
for zeile in allezeilen:
    print(zeile, end="")
    summe += float(zeile)
d.close()
# Tabelle schreiben
d = open("obst.txt","w")
# Tabelle mit verschiedenen Objekten
artname = {23:"Apfel", 8:"Banane", 42:"Pfirsich"}
anzahl = {23:1, 8:3, 42:5}
epreis = {23:2.95, 8:1.45, 42:3.05}
d.write(f"{'Nr':>4}{'Name':>12}{'Anz':>4}{'EP':>13}{'GP':>13}\n")
for x in 23, 8, 42:
    d.write(f"{x:04d}{artname[x]:>12}{anzahl[x]:4d}{epreis[x]:8.2f}"
    f" Euro{anzahl[x] * epreis[x]:8.2f} Euro\n")

""" 
Python Pickle is used to serialize and deserialize a python object structure.
Any object on python can be pickled so that it can be saved on disk.
"""
import pickle
class Fruits: pass
banana = Fruits()
banana.color = 'yellow'
banana.value = 30

filehandler = open("Fruits.bin","wb")
pickle.dump(banana, filehandler)
filehandler.close()

file = open("Fruits.bin",'rb')
object_file = pickle.load(file)
file.close()

print(object_file.color, object_file.value, sep=', ')

import glob, os
files = glob.glob('*.txt')
print(files)

def get_tree_size(path):
    """Return total size of files in given path and subdirs."""
    total = 0
    for entry in os.scandir(path):
        if entry.is_dir(follow_symlinks=False):
            total += get_tree_size(entry.path)
        else:
            total += entry.stat(follow_symlinks=False).st_size
    return total
print(get_tree_size('/Users/mischahaenen/dev/projects/school/WSEN'))