import requests

input_file = 'urls.txt' #change this
def urls_alive(input_file, out_file):
    print("[*] In processing...\n[*] Please wait.")
    alive_urls =[]
    with open(input_file, 'r') as urls:
        for url in urls:
            url = url.strip('\n')
            try:
                res = requests.get(url)

                if res.status_code == 200:
                    alive_urls.append(url)
            except requests.exceptions.ConnectionError:
                pass
            except requests.exceptions.MissingSchema:
                pass

    with open(out_file, 'w') as output_file:
        output_file.write('\n'.join(alive_urls))

    print("[>>] DONE!")
    print(f"[>>] Saved URLs in {out_file}.")

out_file = 'alive_urls.txt' #change this if you want.
urls_alive(input_file, out_file)


