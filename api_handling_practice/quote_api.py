import requests


def fetch_url(url):
    response = requests.get(url)
    data = response.json()
    if data["success"]:
        data =  data["data"]
        return data


def main():

    url = "https://api.freeapi.app/api/v1/public/quotes?page=1&limit=10&query=human"
    data = fetch_url(url)

    for md in data["data"]:
        author = md["author"]
        quote = md["content"]
        print("")
        print("*"*100)
        print(f"\n\"{quote}\"\n\n\tby: {author}\n")
        print("*"*100)       
        print("")

if __name__ == "__main__":
    main()