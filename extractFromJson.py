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
    ip = i.get('ip', 'No IP')
    skip_ip = False

    for j in i.get('data', []):
        if 'honeypot' in j.get('tags', []):
            skip_ip = True
            break

    if not skip_ip:
        for j in i.get('data', []):
            tags = j.get('tags', [])
            if 'iot' in tags or 'ics' in tags:
                product = j.get('product', 'No Product')
                tags_str = ', '.join(tags)
                out = f"{ip}    {product}    {tags_str}"
                # print(out)
                export.append(out)
                break

write_file = open(args.output, "w")
write_file.write("\n".join(export))
