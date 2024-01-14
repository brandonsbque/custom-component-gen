import re

def convert_to_dict(all_ts):
    custom_components = {}

    # Extract lines between start and end comments (returns all the imports which contain the categories and custom_components)
    matches = re.findall(r'\/\/ go\/keep-sorted start\n(.*?)\/\/ go\/keep-sorted end', all_ts, re.DOTALL)

    if not matches:
        print("there was an error... formatting for all.ts file might have changed.")
        return custom_components

    lines = matches[0].strip().split('\n')

    for line in lines:
        line = line.strip()
        print("\nProcessing line: " + line)

        if line.startswith('import'):
            parts = line.split("/")
            print(parts)

            category = parts[1].strip().capitalize()
            component = parts[2].strip()[:-5] # remove " .js'; " at the end of each line
            if category not in custom_components:
                custom_components[category] = []
                print("added %s to as a category in custom_components!" % category)

                custom_components[category].append("md-" + component)
                print("added md-%s to category: %s" % (component, category))
            else:
                custom_components[category].append("md-" + component)
                print("added md-%s to category: %s" % (component, category))
        else:
            pass

    return custom_components

all_ts = "./all.ts"
with open(all_ts, "r") as file:
    all_ts = file.read()

custom_components = convert_to_dict(all_ts)

print("\ndictionary for components complete!\nnow generating material.ts file...")

