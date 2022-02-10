from socket import timeout
from aiohttp import request
import requests

r = requests.get(
    "https://mercer00.github.io/SimplyRecipes/assets/recipes/recipe-4.jpeg", timeout=10)

with open("./Requests/img.jpeg", "wb") as f:
    f.write(r.content)
