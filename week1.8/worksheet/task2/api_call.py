
import httpx

base_url = "https://dummyjson.com/"

# content = "posts/5"

content = "products/search?q=apple"

url = 'https://dummyjson.com/recipes/meal-type/snack'  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

content = response.json()   # JSON data

content = [content.get("difficulty") for content in content.get("recipes", [])]

print(content)
