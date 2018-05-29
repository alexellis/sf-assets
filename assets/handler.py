import csv, os
import json
from urllib import parse

def handle(req):
    """handle a request to the function, set map_label querystring
    to filter based upon a "Map Label" within the CSV file - if undefined
    then a wildcard will match
    Args:
        req (str): request body
    """

    filter = False
    map_label = ""
    if len(os.getenv("Http_Query", "")) > 0:
        filter = True
        qs = parse.parse_qs(os.getenv("Http_Query"))
        map_label_values = qs["map_label"]
        if len(map_label_values) > 0:
            map_label = map_label_values[0]

    file_name = "function/data/Assets_Maintained_by_the_Recreation_and_Parks_Department.csv"

    rows = []
    with open(file_name) as f:
        reader = csv.DictReader(f, delimiter=',', quotechar='\"')
        for row in reader:
            geom = row["Geom"]
            geom = geom[1:len(geom)-2]
            parts = geom.split(",")            
            row["lat"] = parts[0].strip()
            row["lng"] = parts[1].strip()

            if filter == False or row["Map Label"] == map_label:
                rows.append(row)

    return json.dumps(rows)
