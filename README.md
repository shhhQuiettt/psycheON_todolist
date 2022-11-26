
# Todo list







a) Zawiera model z następującymi parametrami: id (int, identyfikator), title (str, tytuł
zadania), done (bool, czy zadanie zostało zrobione), author_ip (str, adres ip osoby
tworzącej), created_date (datetime, data utworzenia), done_date (datetime, data
zakończenia zadania).

b) Posiada widok dostępny pod adresem ‘/todolist’ z metodą GET, który w postaci JSONA
zwraca listę wcześniej zapisanych w bazie sqlite zaplanowanych zadań.

c) Posiada widok ‘/todolist’ z metodą POST, który przyjmuje na wejściu JSON z
parametrami: title, done, done_date. Widok ma dodać zadanie o tytule w podanym polu
title (jedyny wymagany parametr). Oznaczyć jako zrobione lub niezrobione zależnie od
wartości pola done, dodatkowo ustawić adres IP requesta jako author_ip. W przypadku
niepodania pola done, należy ustawić zadanie jako niewykonane. Dodatkowo w
przypadku podania done: true oraz done_date, należy ustawić obie wartości w bazie,
natomiast w przypadku podania done: true oraz niepodania done_date, należy użyć
bieżącego czasu jako done_date. Ostatnim warunkiem, to zwrócenie kodu HTTP 400 w
przypadku podania done: false oraz done_date innego niż null.

d) Posiada widok ‘/todolist/<id_zadania>’ z metodą GET, który w przypadku podania
identyfikatora zadania, które nie istnieje, zwraca HTTP 404, natomiast w przypadku
istniejącego zadania, powinien być zwrócony kompletny obiekt zadania.

e) Posiada widok ‘/todolist/<id_zadania>’ z metodą DELETE, który w przypadku podania
identyfikatora zadania, które nie istnieje, zwraca HTTP 404, lecz w przypadku
istniejącego zadania, to zadanie zostanie usunięte z bazy danych.

f) Posiada testy, które sprawdzą poprawność działania programu. 

#
Tests, that explicitly test task point, are marked by 
```
# Explicit <point> test
```

## Setting up

To run project first time build docker image from the `todolist` directory and run a container

```bash
docker-compose up --build
```

Next program startup can be executed without the `--build` flag

## Testing 
To run tests, run the following command, when the cotainer is already up

```bash
  docker-compose exec app python manage.py test
```

