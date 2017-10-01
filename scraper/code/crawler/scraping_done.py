import requests

if __name__ == "__main__":

    token_url = "http://web/token/"

    payload = {"username":"internal", "password":"newco"}

    r = requests.post(token_url, json=payload)

    if r.status_code == 200:
        token = r.json()['token']

        """
        scraping_done_url = "http://web/scraping/done/"
        headers = {"Content-Type":"application/json", "Authorization": token}
        r = requests.put(scraping_done_url, headers=headers)

        if r.status_code != 200:
            print("Cannot update scraping info")
        else:
            print("Scraping info updated")
        """
