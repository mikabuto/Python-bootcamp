import yaml

with open('../materials/todo.yml') as fh:
	data = yaml.load(fh, Loader=yaml.FullLoader)


res = {"tasks": []}
for package in data['server']['install_packages']:
	res["tasks"].append({"ansible.builtin.apt": {'name': package}})

for file in data['server']['exploit_files']:
	res["tasks"].append({"ansible.builtin.copy": {"src": f"{file}", "dest": f"/path/to/{file}", "follow": "yes"}})

for file in data['server']['exploit_files']:
	args = ""
	if file == "consumer.py":
		args = "-e " + ",".join(data['bad_guys'])
	cmd = f"python3 {file} {args}"
	res["tasks"].append({"ansible.builtin.shell": {"cmd": f"{cmd}", "delegate_to": "remote_host"}})

with open("deploy.yml", 'w') as f:
	f.write(yaml.dump(res))
