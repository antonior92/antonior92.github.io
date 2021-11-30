from liquid import Template
import yaml
import os

# Created datastructure similar to the one used by liquid in my website
mydata = {}
datafolder = '_data'
for subdir, dirs, files in os.walk(datafolder):
    for file in files:
        filepath = subdir + os.sep + file
        relative_path = os.path.relpath(filepath, datafolder)
        print(subdir, dirs, files )
        name, ext = os.path.splitext(relative_path)

        if ext == ".yml":
            tags = os.path.normpath(name).split('/')
            tags.reverse()

            # Read YAML file
            with open(filepath, 'r') as stream:
                localdict = yaml.safe_load(stream)
            # Assign it to dictionary
            for t in tags[:-1]:
                localdict = {t: localdict}
            mydata[tags[-1]] = localdict

template = Template(
    "{% for paper in publications.mypapers %}"
    "Hello, {{ paper.id }}!\n"
    "{% endfor %}"
)
# TODO: Test with latex!

print(template.render(**mydata))
