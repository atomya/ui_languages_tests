# ui_languages_tests
Проект содержит в себе набор автотестов для проверки корректной локализации при переключении языков на coinmarketcap.com.
Покрытие неполное, использовался DDT подход, тесты легко расширяемы, для увеличения тестового покрытия достаточно добавить данные в параметры.
Тесты доступны для запуска на Chrome и Firefox
### Requirements
```
pytest==5.1.1
PyYAML==5.3.1
selenium==3.14.0
```
### Start:
```
git clone https://github.com/atomya/ui_languages_tests.git
cd ui_languages_tests
pip install -r requirements.txt 
```
### Run the tests:
```
Command to run tests for review:
pytest -s -v test_lang.py
```
