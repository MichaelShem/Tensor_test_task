Тестовое задания для компании Тензор от Шемякина Михаила

В данном проекте используется фреймворк pytest, а так же реализован PageObject паттерн


Первый тестовый сценарий реализован в файле test_main_page.py

Второй тестовый сценарий реализован в файле test_image_page.py

**Важное замечание. Из-за разницы в версиях пакетов, иногда могут падать ошибки типа:**

from pages.product_page import ProductPageE   ImportError: attempted relative import with no known parent package

Если данная ошибка возникyеn, необходимо в файлах test_main_page.py и test_image_page.py добавить точку перед pages

___

**Запуск первого теста:** pytest -v -s --tb=line test_main_page.py

**Запуск второго теста:** pytest -v -s --tb=line test_image_page.py



