import requests, json, cairosvg, os

API_URL = "https://api.scryfall.com"
OUT_DIR = "out/"

if not os.path.exists(OUT_DIR):
    os.mkdir(OUT_DIR)

res = requests.get(API_URL + "/sets/")
sets = json.loads(res.text)["data"]
set_codes = []
set_icons = []
for s in sets:
    if s["set_type"] == "expansion":
        set_codes.append(s["code"])
        set_icons.append(s["icon_svg_uri"])

i = 0
for i in range(0, len(set_icons)):
    cairosvg.svg2png(url=set_icons[i], write_to=OUT_DIR + set_codes[i] + ".png")
    print("Downloaded " + set_codes[i] + ".png")

print("\nDone!")
print(str(i) + " files downloaded to " + OUT_DIR)