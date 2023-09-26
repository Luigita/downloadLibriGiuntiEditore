import requests




inter = 1


print(format(inter, "03d"))


while inter <= 120:
	response = requests.get("https://static.dbookeasy.giuntiscuola.it/progetti/progetto_33/book_518/pages/1665673802" + format(inter, "03d") + ".png")
	if response.status_code == 200:
		with open(r"Pages\Page " + format(inter) + ".PNG", "wb") as f:
			f.write(response.content)
			print("Pagina " + format(inter, "03d") + " scaricata")
	inter = inter + 1
