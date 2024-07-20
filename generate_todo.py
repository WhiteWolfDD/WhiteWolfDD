import json

with open('todo.json', 'r') as f:
    tasks = json.load(f)

todo_list = "\n".join([f'<li><a href="{task["link"]}"><img alt="{task["task"]}" src="https://img.shields.io/badge/{task["task"].replace(" ", "%20")}-blue"></a></li>' for task in tasks])

with open('README.md', 'r') as f:
    readme = f.read()

start_marker = "<!-- START TODO LIST -->"
end_marker = "<!-- END TODO LIST -->"

start = readme.index(start_marker) + len(start_marker)
end = readme.index(end_marker)

new_readme = readme[:start] + "\n" + todo_list + "\n" + readme[end:]

with open('README.md', 'w') as f:
    f.write(new_readme)
