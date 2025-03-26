import requests

response = requests.get("https://api.chucknorris.io/jokes/random")

if response.status_code == 200:
    data = response.json()
    joke = data["value"]

    with open("joke.txt", "w", encoding="utf-8") as file:
        file.write(joke)

    print("הבדיחה נשמרה לקובץ 🎉")
else:
    print("שגיאה בשליפת הבדיחה")
