import json

path = "model_training_colab.ipynb"  # ← 改成真实文件名

with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

nb.get("metadata", {}).pop("widgets", None)

for cell in nb.get("cells", []):
    cell.get("metadata", {}).pop("widgets", None)

with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=2)

print("✅ metadata.widgets removed")
