# Найдите количество книг, которое можно разместить на дискете

FLOPPY_SPACE = 1.44 * 1024 * 1024
N_BOOK_PAGES = 100
N_PAGE_STRS = 50
N_STR_SYMS = 25
N_SYM_BYTES = 4

n_floppy_books = int(FLOPPY_SPACE // (N_BOOK_PAGES * N_PAGE_STRS * N_STR_SYMS * N_SYM_BYTES))

print("Количество книг, помещающихся на дискету:", n_floppy_books)
