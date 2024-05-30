import requests    # http requests for scryfall's api
import json        # for a nice, exploitable format
import cairosvg    # svg to png conversion
import os          # file/folder manipulation

API_URL = "https://api.scryfall.com"
OUT_DIR = "out/"

# if the output folder doesn't exist yet, create it
if not os.path.exists(OUT_DIR):
    os.mkdir(OUT_DIR)

# the http request's response
res = requests.get(API_URL + "/sets/")
# all sets data
sets = json.loads(res.text)["data"]

# these two are pretty self explanatory
set_codes = []
set_icons = []

# for each set...
for s in sets:
    # ... if it's an expansion...
    if s["set_type"] == "expansion":
        # append the data as new entries
        set_codes.append(s["code"])
        set_icons.append(s["icon_svg_uri"])     # stored as a link to an svg file

# for each icon...
i = 0
for i in range(0, len(set_icons)):
    # convert it to a png and output it in the OUT_DIR
    cairosvg.svg2png(url=set_icons[i], write_to=OUT_DIR + set_codes[i] + ".png")
    print("Downloaded " + set_codes[i] + ".png")

print("\nDone!")
print(str(i) + " files downloaded to " + OUT_DIR)
