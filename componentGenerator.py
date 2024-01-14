import re
import textwrap

def generate_file(all_ts):
    # Extract lines between start and end comments (returns all the imports which contain the categories and custom_components)
    matches = re.findall(r"\/\/ go\/keep-sorted start\n(.*?)\/\/ go\/keep-sorted end", all_ts, re.DOTALL)

    if not matches:
        print("there was an error... formatting for all.ts file might have changed.")
        return custom_components

    lines = matches[0].strip().split("\n")

    for line in lines:
        line = line.strip()
        print("\nProcessing line: " + line)

        if line.startswith("import"):
            parts = line.split("/")

            category = parts[1].strip().capitalize()
            original_component = parts[2].strip()[:-5]
            component = parts[2].strip()[:-5].removeprefix("md-")
            # [:-5] to remove " .js'; " at the end of each line
            # for some reason, import for FocusRing in all.ts is: import './focus/md-focus-ring.js';
            # this breaks the pattern, so we are taking into account this possibility. hence,
            # we use removeprefix() to remove the "md-" incase it happens again in the future.
            
            component_split = component.split("-")
            class_name = ""
            for word in component_split:
                class_name = class_name + word.capitalize()

            material_imports.append(
                f"import {{ MD{class_name} as MD{class_name}WebComponent }} from \"@material/web/{category.lower()}/{original_component}\";"
            )
            print("successfully created import for " + class_name)

            custom_components.append(textwrap.dedent(f"""
                const md{class_name} = createComponent({{
                    react: React,
                    tagName: "md-{component}"
                    elementClass: MD{class_name}WebComponent
                }});
            """))
            print("successfully created created custom component for " + class_name)

            exports.append(class_name)
            print("successfully added %s to exports" % class_name)
        else:
            pass

    return custom_components

all_ts = "./all.ts"
with open(all_ts, "r") as file:
    all_ts = file.read()

default_imports = """import React from "react";
import { createComponent } from "@lit/react";
"""

material_imports = []
custom_components = []
exports = []

generate_file(all_ts)

material_exports = "export {" + "\n    " + ",\n    ".join(exports) + ",\n}"
material_ts = default_imports + "\n" + "\n".join(material_imports) + "\n" + "\n".join(custom_components) + "\n" + material_exports

output = "material.ts"
with open(output, "w") as output_file:
    output_file.write(material_ts)

print("\nscript successful - created a file called material.ts")
print("put this in the root folder of your react project,")
print("then you can use the material-web components (for example: <mdElevatedButton>Hello World</mdElevatedButton>)")
print("IMPORTANT: make sure to install material web components by running 'npm install @material/web' or 'yarn add @material/web'")
