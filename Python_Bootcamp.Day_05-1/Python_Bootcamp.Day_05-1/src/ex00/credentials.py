from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
import json

data = {"Cyberman": "John Lumic",
			"Dalek": "Davros",
			"Judoon": "Shadow Proclamation Convention 15 Enforcer",
			"Human": "Leonardo da Vinci",
			"Ood": "Klineman Halpen",
			"Silence": "Tasha Lem",
			"Slitheen": "Coca-Cola salesman",
			"Sontaran": "General Staal",
			"Time Lord": "Rassilon",
			"Weeping Angel": "The Division Representative",
			"Zygon": "Broton"}

def app(environ, start_response):
	# Parse query string to get species parameter
	params = parse_qs(environ["QUERY_STRING"])
	species = params.get("species", None)
	
	if species is not None and len(species):
		payload = "{\"credentials\": \"Unknown\"}"
		if (species[0]):
			found_species = data.get(species[0], 0)
			payload_data = json.dumps({species[0]: found_species}) if found_species else json.dumps({"credentials": "Unknown"})
			payload = (payload_data + '\n').encode("utf-8")
			status = "200 OK"
			headers = [("Content-Type", "application/json")]
			start_response(status, headers)
			return [payload]
		else:
			status = "400 Bad Request"
			headers = [("Content-Type", "text/plain")]
			start_response(status, headers)
			return ["Missing request parameter: species"]

if __name__ == "__main__":
	httpd = make_server("", 8888, app)
	print("Serving on port 8888...")
	httpd.serve_forever()
