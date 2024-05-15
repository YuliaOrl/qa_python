# qa_python

1. test_add_new_book_add_two_books - проверяет работу метода add_new_book и добавление двух книг в словарь.

2. test_add_new_book_no_genre - проверяет работу метода add_new_book, а именно: у новой добавленной книги нет жанра в
   словаре.

3. test_add_new_book_pozitiv_limit_values - проверяет граничные значения для метода add_new_book, а именно: 1, 2, 39, 40
   возможных символов в названии книги.

4. test_add_new_book_negativ_limit_values - проверяет граничные значения для метода add_new_book, а именно: при 0 и 41
   символе в названии книги, книга не добавляется в словарь.

5. test_set_book_genre_correct_g - позитивная проверка метода set_book_genre. Проверяется выполнение условий метода с
   корректными тестовыми данными (устанавливается жанр, если книга есть в books_genre и её жанр входит в список genre).

6. test_set_book_genre_incorrect_genre_and_name_not_set - негативная проверка метода set_book_genre, а именно: если в
   методе передаётся несуществующая в словаре книга или некорректный жанр, то жанр книги не устанавливается.

7. test_get_book_genre_rights - проверка метода get_book_genre, а именно: результат получения корректного жанра методом
   get_book_genre соответствует ожидаемому результату.

8. test_get_books_with_specific_genre_rights - позитивная проверка метода get_books_with_specific_genre, а именно: в
   получаемом по жанру списке присутствуют книги только с нужным жанром.

9. test_get_books_with_specific_genre_negativ - негативная проверка метода get_books_with_specific_genre с
   несуществующим жанром.

10. test_get_books_genre_rights - позитивная проверка метода get_books_genre, а именно: результат получения словаря
    методом get_books_genre соответствует ожидаемому результату.

11. test_get_books_for_children_rights - позитивная проверка метода get_books_for_children, а именно: в списке книг для
    детей отсутствуют книги с возрастным рейтингом.

12. test_add_book_in_favorites_rights - позитивная проверка метода add_book_in_favorites, а именно: добавленная книга
    присутствует в избранном.

13. test_add_book_in_favorites_once - позитивная проверка метода add_book_in_favorites, а именно: книгу можно добавить
    один раз.

14. test_add_book_in_favorites_nonexistent_book - негативная проверка метода add_book_in_favorites, а именно: книга,
    отсутствующая в словаре, не добавляется в избранное.

15. test_delete_book_from_favorites_rights - позитивная проверка метода delete_book_from_favorites: книга удаляется из
    избранного, если она есть в списке избранное.

16. test_delete_book_from_favorites_nonexistent_book - негативная проверка метода delete_book_from_favorites: книга,
    отсутствующая в избранном, не удаляется из списка избранного и не меняет его содержание.

17. test_get_list_of_favorites_books_rights - позитивная проверка метода get_list_of_favorites_books, а именно:
    список избранных книг, полученных методом get_list_of_favorites_books, соответствует ожидаемому результату. 