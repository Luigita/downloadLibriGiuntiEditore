import requests

page = 1
total_pages = 120

print("Page " + format(page, "03d") + " done")

while page <= total_pages:
	response = requests.get("https://static.dbookeasy.giuntiscuola.it/progetti/progetto_33/book_518/pages/1665673802" + format(page, "03d") + ".png")
	if response.status_code == 200:
		with open(r"Pages\Page " + format(page) + ".PNG", "wb") as f:
			f.write(response.content)
			print("Pagina " + format(page, "03d") + " scaricata")
	page = page + 1
