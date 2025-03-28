# TODO Найдите количество книг, которое можно разместить на дискете
volume_discette_mb = 1.44
volume_discette_b = volume_discette_mb * (1024 ** 2)
pages = 100
strings = 50
simbols = 25
volume_simbol_b = 4
volume_book = pages * strings * simbols * volume_simbol_b
amount_books = round(volume_discette_b / volume_book)
print("Количество книг, помещающихся на дискету:", amount_books)
