import argparse
import json


parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="output file")
parser.add_argument("-i", "--input", help="input file")
args = parser.parse_args()

jfile = open(args.input)
json_data = json.load(jfile)
export = []
for i in json_data:
    ip = i.get('id', 'No ID')
    skip_id = False

    for j in i.get('data', []):
        if 'johndoe' in j.get('name', []):
            skip_id = True
            break

    if not skip_id:
        for j in i.get('data', []):
            tags = j.get('name', [])
            if 'james' in name or 'alex' in name:
                family = j.get('family', 'No Family')
                name_str = ', '.join(name)
                out = f"{id}    {family}    {name_str}"
                # print(out)
                export.append(out)
                break

write_file = open(args.output, "w")
write_file.write("\n".join(export))
