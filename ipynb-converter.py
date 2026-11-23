import json

with open (r"path_file", "r", encoding="utf-8") as file:
    notebook = json.load(file) 

for cell in notebook["cells"]:
    tipe = cell["cell_type"]
    isi = "".join(cell["source"])

    print("=== TIPE:", tipe, "===")
    print(isi)
    print()
