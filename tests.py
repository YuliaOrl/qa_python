import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    def test_add_new_book_no_genre(self, collector):
        name = 'Евгений Онегин'
        collector.add_new_book(name)
        assert collector.books_genre[name] == ''

    @pytest.mark.parametrize('name', ['1', '2k', 'В названии этой книги всего 39 символов',
                                      'В названии этой книги всего 40 символов!'])
    def test_add_new_book_pozitiv_limit_values(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.books_genre

    @pytest.mark.parametrize('name', ['', 'В названии этой большой книги 41 символ!!'])
    def test_add_new_book_negativ_limit_values(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    books = [['Пришельцы', 'Фантастика'], ['Мгла', 'Ужасы'], ['Шерлок Холмс', 'Детективы'], ['Буратино', 'Мультфильмы'],
             ['Ревизор', 'Комедии']]

    @pytest.mark.parametrize('name, genre', books)
    def test_set_book_genre_correct_genre_set(self, collector, name, genre):
        collector.books_genre = {name: ''}
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    @pytest.mark.parametrize('name, genre', [['Мгла', 'Ужастики'], ['Мгла2', 'Ужасы']])
    def test_set_book_genre_incorrect_genre_and_name_not_set(self, collector, name, genre):
        collector.books_genre = {'Мгла': ''}
        collector.set_book_genre(name, genre)
        assert collector.books_genre == {'Мгла': ''}

    test_data = [['Пришельцы', 'Фантастика'], ['Мгла', 'Ужасы'], ['Шерлок Холмс', 'Детективы'],
                 ['Буратино', 'Мультфильмы'], ['Ревизор', 'Комедии']]

    @pytest.mark.parametrize('name, genre', test_data)
    def test_get_book_genre_rights(self, collector, books_genre, name, genre):
        assert collector.get_book_genre(name) == genre

    def test_get_books_with_specific_genre_rights(self, collector, books_genre):
        genre = 'Детективы'
        for book in collector.get_books_with_specific_genre(genre):
            assert collector.get_book_genre(book) == genre

    def test_get_books_with_specific_genre_negativ(self, collector, books_genre):
        assert collector.get_books_with_specific_genre('Романы') == []

    def test_get_books_genre_rights(self, collector):
        collection = {'Пришельцы': 'Фантастика', 'Мгла': 'Ужасы', 'Шерлок Холмс': 'Детективы'}
        collector.books_genre = collection
        assert collector.get_books_genre() == collection

    def test_get_books_for_children_rights(self, collector, books_genre):
        for book in collector.get_books_for_children():
            assert collector.get_book_genre(book) not in collector.genre_age_rating

    def test_add_book_in_favorites_rights(self, collector, books_genre):
        book = 'Пришельцы'
        collector.add_book_in_favorites(book)
        assert book in collector.favorites

    def test_add_book_in_favorites_once(self, collector, books_genre):
        collector.add_book_in_favorites('Пришельцы')
        collector.add_book_in_favorites('Пришельцы')
        assert len(collector.favorites) == 1

    def test_add_book_in_favorites_nonexistent_book(self, collector, books_genre):
        nonexistent_book = 'Отсутствующая в словаре книга'
        collector.add_book_in_favorites(nonexistent_book)
        assert nonexistent_book not in collector.favorites

    def test_delete_book_from_favorites_rights(self, collector, favorites):
        book = 'Пришельцы'
        collector.delete_book_from_favorites(book)
        assert book not in collector.favorites

    def test_delete_book_from_favorites_nonexistent_book(self, collector, favorites):
        expected_result = ['Пришельцы', 'Мгла', 'Шерлок Холмс']
        collector.delete_book_from_favorites('Несуществующая в избранном книга')
        assert collector.favorites == expected_result

    def test_get_list_of_favorites_books_rights(self, collector, favorites):
        expected_result = ['Пришельцы', 'Мгла', 'Шерлок Холмс']
        assert collector.get_list_of_favorites_books() == expected_result
