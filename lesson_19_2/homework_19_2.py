import requests
from pathlib import Path

url = 'http://127.0.0.1:8080'
file_path = Path("omg.png")

with open(file_path, 'rb') as f:
    post_file = {'image': f}
    response_post = requests.post(f"{url}/upload", files=post_file)

data = response_post.json()
image_url = data.get('image_url')

print("-" * 40, "POST")
print(response_post.status_code)
print(response_post.json())


print("-"*40, "GET")
file_name = Path(image_url).name  # omg.png
get_url = f"{url}/image/{file_name}"

headers = {"Content-Type": "text"}
response_get = requests.get(get_url, headers=headers)
if response_get.status_code == 200:
    print("JSON відповідь:", response_get.json())
    print(response_get.status_code)
else:
    print("Помилка GET:", response_get.status_code, response_get.text)



del_url = f"{url}/delete/{file_name}"
response_del = requests.delete(del_url)
print("-" * 40, "DELETE")
print(response_del.status_code)
print(response_del.json())




