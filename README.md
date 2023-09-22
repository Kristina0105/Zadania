<h2>Bank</h2>  
<h3>Клас Client:</h3>

###### Конструктор __init__: Приймає ім'я клієнта та параметр балансу. Встановлює ім'я та баланс клієнта.
###### Метод __str__: Повертає рядок, що містить ім'я клієнта та його баланс.

<h3>Клас Bank:</h3>

###### Конструктор __init__: Ініціалізує пустий список клієнтів банку.
###### Метод add_client: Додає нового клієнта до списку клієнтів банку з заданим ім'ям.
###### Метод find_client: Пошук клієнта за ім'ям у списку клієнтів банку. Повертає об'єкт клієнта або None, якщо клієнт не знайдений.
###### Метод save_into_file: Зберігає дані клієнтів у файл. Дані записуються у форматі "ім'я, баланс".
###### Метод download_from_file: Завантажує дані клієнтів з файлу. Відкриває файл, читає рядки та створює об'єкти клієнтів для кожного рядка.

<h3>Основний код:</h3>

###### Створюється об'єкт bank класу Bank.
###### Створюється клієнт client1 класу Client та додається до банку за допомогою методу add_client.
###### Виводиться інформація про клієнта client1 за допомогою методу __str__.
###### Пошук клієнта client1 за ім'ям виконується методом find_client, та результат виводиться на екран.
###### Збереження даних клієнтів в файл clients_data.txt виконується методом save_into_file.
###### Завантаження даних клієнтів з файлу clients_data.txt виконується методом download_from_file.

<h2>Crypto</h2>
<h3>Клас DollarValue:</h3>

###### Цей клас визначає дескриптор, який можна використовувати для отримання значення доларової вартості криптовалюти. 
###### Доларова вартість розраховується за допомогою інформації про котирування та кількість одиниць криптовалюти у портфелі. 
###### Вам потрібно отримати доступ до цього значення через інстанс об'єкта Portfel.

<h3>Клас Portfel:</h3>

###### Конструктор __init__: Приймає ім'я інвестора та ініціалізує порожній словник crypto для зберігання інформації про криптовалюту у портфелі та порожній словник quotation для зберігання котирувань криптовалют.
###### Метод add_crypto: Додає задану криптовалюту до портфелю та оновлює кількість одиниць цієї криптовалюти у портфелі. Якщо криптовалюта вже присутня у портфелі, то кількість одиниць оновлюється.
###### Метод del_crypto: Видаляє задану криптовалюту з портфелю.
###### Метод crypto_to_dollar: Обчислює доларову вартість кожної криптовалюти у портфелі на основі інформації про котирування та оновлює quotation.
###### Метод show_portfel: Виводить інформацію про інвестора та його портфель, включаючи ім'я інвестора, назву криптовалюти, кількість одиниць криптовалюти та їх доларову вартість.
###### Метод sort_portfel: Сортує портфель інвестора за доларовою вартістю криптовалют в порядку спадання.

<h3>Основний код:</h3>

###### Створюється об'єкт p класу Portfel з ім'ям інвестора "Інвестор1".
###### Встановлюються котирування для криптовалют "btc" та "etg" за допомогою атрибуту quotation.
###### Додаються кількість одиниць криптовалют "btc" та "etg" до портфеля за допомогою методу add_crypto.
###### Виводиться інформація про портфель за допомогою методу show_portfel.
###### Сортується портфель за доларовою вартістю криптовалют за допомогою методу sort_portfel та виводиться відсортований портфель.


<h2>Bankomat</h2>
<h3>Клас User:</h3>

###### Конструктор __init__: Приймає ім'я користувача, пін-код та початковий баланс ініціалізує ці атрибути об'єкта.
###### Метод check_pin_code: Порівнює введений пін-код з пін-кодом користувача та повертає True, якщо вони співпадають.
###### Метод check_balance: Повертає поточний баланс користувача.
###### Метод pay_money: Знімає гроші з балансу користувача. Якщо на балансі недостатньо коштів, повертає 0, інакше повертає суму знятих коштів.

<h3>Клас Bankomat:</h3>

###### Конструктор __init__: Приймає початковий баланс банкомату та ініціалізує атрибути об'єкта. Завантажує дані користувачів з файлу users.txt за допомогою методу load_users.
###### Метод registration: Реєструє нового користувача з ім'ям, пін-кодом і початковим балансом. Зберігає дані користувача в словник users та оновлює файл users.txt за допомогою методу save_users.
###### Метод login: Виконує процедуру входу для користувача за ім'ям і пін-кодом. Повертає об'єкт користувача, якщо ім'я і пін-код вірні, або None, якщо вони неправильні.
###### Метод operations: Виконує операції користувача, такі як перевірка балансу та зняття грошей. Цикл виконується, поки користувач не вибере опцію "Вийти".
###### Метод load_users: Завантажує дані користувачів з файлу users.txt і ініціалізує словник users.
###### Метод save_users: Зберігає дані користувачів у файл users.txt.

<h3>Основний код:</h3>

# Створюється об'єкт bankomat класу Bankomat з початковим балансом 1000.
# В головному циклі виконується вибір опцій: реєстрація нового користувача, вхід користувача та виконання операцій.
# Після виходу з циклу програма завершує роботу.
