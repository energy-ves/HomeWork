# TODO Найдите количество книг, которое можно разместить на дискете
disk_size_in_mb = 1.44
count_of_pages = 100
count_of_lines = 50
count_of_chars = 25
b_one_char = 4
disk_size_in_b = 1024 * 1024 * disk_size_in_mb
total_b_in_book = count_of_pages * count_of_lines * count_of_chars * b_one_char
count_of_book = disk_size_in_b // total_b_in_book
count_of_book = int(count_of_book)
print("Количество книг, помещающихся на дискету:", count_of_book)

