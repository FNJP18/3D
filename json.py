import json
with open("project.json","r",encoding="utf-8") as f:
    data = json.load(f)
with open("project-formatted.json","w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)