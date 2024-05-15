import pytest
from main import BooksCollector


@pytest.fixture(scope='function')
def collector():
    collector = BooksCollector()
    return collector


@pytest.fixture(scope='function')
def books_genre(collector):
    collector.books_genre = {'Пришельцы': 'Фантастика', 'Мгла': 'Ужасы', 'Шерлок Холмс': 'Детективы',
                             'Буратино': 'Мультфильмы', 'Ревизор': 'Комедии', 'Лунный камень': 'Детективы',
                             'Десять негритят': 'Детективы'}
    return collector.books_genre


@pytest.fixture(scope='function')
def favorites(collector):
    collector.favorites = ['Пришельцы', 'Мгла', 'Шерлок Холмс']
    return collector.favorites
