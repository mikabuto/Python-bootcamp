import requests
import sys
import os
 
HOST = "localhost"
PORT = "8888"
URL = f"http://{HOST}:{PORT}"
 
 
def upload(path: str) -> str:
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            r = requests.post(f'{URL}/post', files={'media': (os.path.basename(path), f, "multipart/form-data")})
        if r.ok:
            return "File uploaded successfully"
        else:
            return "Error: File didn't upload!"
    else:
        return "Error: File doesn't exist!"
 
 
def get_list() -> str:
    r = requests.get(f'{URL}/list')
    if r.ok:
        return r.text.replace("</br>", "\n")
    else:
        return f"Error: {r.text}"
 
 
def main():
    if len(sys.argv) == 2 and sys.argv[1] == "list":
        print(get_list())
    elif len(sys.argv) == 3 and sys.argv[1] == "upload":
        print(upload(sys.argv[2]))
    else:
        print("Error: Invalid arguments!")
 
 
if __name__ == '__main__':
    main()