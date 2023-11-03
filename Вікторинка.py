import random
from datetime import datetime
class User:
    def __init__(self, login, password, date_of_birth):
        self.login = login
        self.password = password
        if self.date_format(date_of_birth):
            self.date_of_birth = date_of_birth
        else:
            raise ValueError("Неправильний формат дати народження.")
        self.results = {}

    def date_format(self, date):
        try:
            datetime.strptime(date, '%d/%m/%Y')
            return True
        except ValueError:
            return False

class UserManager:
    def __init__(self):
        self.users = {}

    def login_existed(self, login, password):
        user = self.users.get(login)
        if user:
            user.password = password
            return user
        else:
            return None

    def registrate(self, login, password, date_of_birth):
        if login not in self.users:
            user = User(login, password, date_of_birth)
            self.users[login] = user
            return user
        return None

    def show_user_result(self, user):
        if user.login in self.users:
            return user.results.get(user.login)
        else:
            return None

    def change_data(self, user, new_password, new_date_of_birth):
        user.password = new_password
        user.date_of_birth = new_date_of_birth

class QuestionFactory:
    def create_question(self, text, correct_answer):
        return Question(text, correct_answer)

class Question:
    def __init__(self, text, correct_answer):
        self.text = text
        self.correct_answer = correct_answer

class Quiz:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions
        self.results = QuizResults(self)

class QuizResults:
    def __init__(self, quiz):
        self.quiz = quiz
        self.results = {}
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)
    def notify_s(self, user, score):
        for subscriber in self.subscribers:
            subscriber.update(user, self.quiz, score)
    def store_result(self, user, score):
        user.results[self.quiz.name] = score
        self.results[user.login] = score
        self.notify_s(user, score)

    def get_top_players(self):
        sorted_results = sorted(self.results.items(), key=lambda x: x[1], reverse=True)
        top_players = sorted_results[:20]
        return top_players

class QuizManager:
    def __init__(self):
        self.user_manager = UserManager()
        self.quizzes = {}

    def create_quiz(self, user, quiz_name, questions):
        if user or user.login == "admin":
            quiz = Quiz(quiz_name, questions)
            self.quizzes[quiz_name] = quiz
            return quiz
        return None

    def edit_quiz(self, user, quiz_name, new_name, new_questions):
        if user or user.login == "admin":
            quiz = self.quizzes.get(quiz_name)
            if quiz:
                quiz.name = new_name
                quiz.questions = new_questions
                return "Вікторина відредагована успішно."
            else:
                return "Вікторина не знайдена."
        else:
            return "Ви не маєте прав доступу."

    def get_all_questions(self):
        all_questions = []
        for quiz in self.quizzes.values():
            all_questions.extend(quiz.questions)
        return all_questions

    def mixed_quiz(self, user, quiz_name):
        all_questions = self.get_all_questions()
        if user or user.login == "admin":
            random.shuffle(all_questions)
            selected_questions = all_questions[:20]
            quiz = Quiz(quiz_name, selected_questions)
            self.quizzes[quiz_name] = quiz
            self.start_quiz(user, quiz)
        return None

    def start_quiz(self, user, quiz):
        if user:
            random.shuffle(quiz.questions)
            score = 0

            num_questions = min(20, len(quiz.questions))

            for i in range(num_questions):
                question = quiz.questions[i]
                print(f"Питання {i + 1}: {question.text}")
                user_answer = input("Ваша відповідь: ")
                if user_answer in question.correct_answer:
                    score += 1

            quiz.results.store_result(user, score)
            print(f"Ви набрали {score} балів у вікторині {quiz.name}.")


class QuizSystemFacade:
    def __init__(self):
        self.user_manager = UserManager()
        self.quiz_manager = QuizManager()
        self.user = None

    def display_menu(self):
        while True:
            if not self.user:
                print("1. Зареєструватися")
                print("2. Війти у систему")

                choice = input("Виберіть варіант: ")

                if choice == '1':
                    login = input("Введіть логін: ")
                    password = input("Введіть пароль: ")
                    date_of_birth = input("Введіть вашу дату народження: ")
                    user = self.user_manager.registrate(login, password, date_of_birth)
                    if user:
                        print(f"Зареєстовано як - {user.login}")
                        self.user = user
                    else:
                        print("Login failed.")
                elif choice == '2':
                    login = input("Введіть логін: ")
                    password = input("Введіть пароль: ")
                    user = self.user_manager.login_existed(login, password)
                    if user:
                        print(f"Користувач {user.login} війшов у систем")
                        self.user = user
                    else:
                        print("Login failed.")
                else:
                    print("Invalid choice. Please select a valid option.")

            elif self.user.login == "admin":
                print("1. Створити вікторину")
                print("2. Редагувати вікторину (Admin)")
                print("3. Exit")

                option = input("Виберіть варіант: ")

                if option == '1':
                    quiz_name = input("Enter quiz name: ")
                    num_of_questions = int(input("Enter the number of questions: "))
                    questions = []
                    for i in range(num_of_questions):
                        question_text = input(f"Enter Question {i + 1}: ")
                        answers = input("Enter correct answers separated by commas: ").split(',')
                        new_question = Question(question_text, answers)
                        questions.append(new_question)
                    new_quiz = self.quiz_manager.create_quiz(user.login, quiz_name, questions)
                    if new_quiz:
                        print(f"Quiz {new_quiz.name} created.")
                    else:
                        print("Failed to create the quiz.")
                elif option == '2':
                    quiz_name = input("Enter quiz name to edit: ")
                    new_name = input("Enter new name: ")
                    num_of_questions = int(input("Enter the number of questions: "))
                    questions = []
                    for i in range(num_of_questions):
                        question_text = input(f"Enter Question {i + 1}: ")
                        answers = input("Enter correct answers separated by commas: ").split(',')
                        new_question = Question(question_text, answers)
                        questions.append(new_question)
                    result = self.quiz_manager.edit_quiz(user.login, quiz_name, new_name, questions)
                    print(result)
                elif option == '3':
                    self.user = None
                else:
                    print("Invalid choice. Please select a valid option.")

            else:
                print("Menu:")
                print("1. Почати вікторину")
                print("2. Подивитись свій результат")
                print("3. Подивитись Top 20 з певної вікторини")
                print("4. Змінити налаштування. Можна змінювати пароль та дату народження.")
                print("5. Exit")

                choice1 = input("Виберіть варіант: ")

                if choice1 == '1':
                    if user:
                        quiz_type = input("Тематична вікторина - 1, змішані питання - 2: ")
                        if quiz_type == '1':
                            quiz_name = input("Enter quiz name to start: ").lower()
                            quiz = self.quiz_manager.quizzes.get(quiz_name)
                            if quiz:
                                self.quiz_manager.start_quiz(user, quiz)
                            else:
                                print("Quiz not found.")
                        elif quiz_type == '2':
                            self.quiz_manager.mixed_quiz(user, "Mixed")
                        else:
                            print("Invalid choice. Please select a valid option.")
                elif choice1 == '2':
                    if user:
                        result = self.user_manager.show_user_result(user)
                        print(f"User results: {result}")
                elif choice1 == '3':
                    quiz_name = input("Enter quiz name to view Top 20 Players: ").lower()
                    quiz = self.quiz_manager.quizzes.get(quiz_name)
                    if quiz:
                        top_players = quiz.results.get_top_players()  # Отримати топ-20 гравців для цієї вікторини
                        if top_players:
                            print(f"Top 20 Players for '{quiz_name}':")
                            for rank, (user_login, score) in enumerate(top_players, start=1):
                                print(f"Rank {rank}: User: {user_login}, Score: {score}")
                        else:
                            print(f"No top players for '{quiz_name}' yet.")
                    else:
                        print("Quiz not found.")
                elif choice1 == '4':
                    if user:
                        password = input("Enter new password: ")
                        date_of_birth = input("Enter new date of birth: ")
                        self.user_manager.change_data(user, password, date_of_birth)
                        print("User data changed.")
                elif choice1 == '5':
                    print("Exit")
                    self.user = None
                else:
                    print("Invalid choice. Please select a valid option.")



quiz_system = QuizSystemFacade()

admin_user = quiz_system.user_manager.registrate("admin", "admin_password", "01/02/1998")
user1 = quiz_system.user_manager.registrate("Михайло", "1", "05/02/1998")
user2 = quiz_system.user_manager.registrate("Крістіна", "2", "30/09/1999")
if admin_user:
    print("Admin user registered.")
else:
    print("Failed to register admin user.")

quiz1_name = "Гаррі Поттер"
quiz1_questions = [
    Question("Який тип тварини є домашнім улюбленцем Гегріда, Бакбіком?", ["Гіпогриф"]),
    Question("Сльози якої тварини є єдиним відомим протиотрутою для отрути василіска?", ["Фінікс"]),
    Question("Напишіть усіх 4 кентаврів, названих у книгах про Гаррі Поттера", ["Ронан, Бейн, Магоріан, Фіренце"]),
    Question("Яким заклинанням Гаррі вбив лорда Волдеморта?", ["Експеліармус"]),
    Question("Напишіть усі 3 Непростимі прокляття", ["Імперій, Круциат, Авада Кедавра"]),
    Question("Заклинання Феліфорс перетворює кота на що?", ["Котел"]),
    Question("Як Гаррі вдається дихати під водою під час другого завдання Тричаклунського турніру?", ["Він їсть жаберник"]),
    Question("Чарівник, який не вміє займатися магією, відомий як:", ["Скиб"]),
    Question("Який елемент асоціюється з Хаффлпаффом?", ["Земля"]),
    Question("Символічною твариною якого будинку є змія?", ["Слизарін"]),
    Question("Який дорогоцінний камінь символізує студентів у домі Рейвенкло?", ["Сапфір"]),
    Question("Який дорогоцінний камінь символізує студентів у домі Хаффлпафф?", ["Ромб"]),
    Question("Який темний чарівник був із Гріфіндору?", ["Петро Петтігрю"]),
    Question("Як звали домашнього ельфа родини Чорних?", ["Кричер"]),
    Question("Що таке тестрал?", ["Невидимий крилатий кінь"]),
    Question("Як звали тварину, яка виконувала роль стукача на ранніх іграх у квідич?", ["Золотий Сніджет"]),
    Question("Викопаний, що зробить мандрагора?", ["Орать"]),
    Question("Хто нокаутує троля в жіночій ванній в Гаррі Поттері та Філософському камені?", ["Рон"]),
    Question("Що повинен сказати користувач Мародерської карти після її використання, щоб скинути її?", ["Пустощі вдалося"]),
    Question("Закінчіть напис на надгробку Доббі: «Тут лежить Добі ...", ["Вільний ельф"]),
]

quiz2_name = "На кмітливість"
quiz2_questions = [
    Question("Яку воду можна принести в ситі?", ["Заморожену."]),
    Question("Кінь перевозить 10 кг вугілля, а поні — 10 кг вати. У кого вантаж важчий?", ["Вантаж однаковий"]),
    Question("Що посеред землі стоїть?", ["М"]),
    Question("Яке колесо не крутиться в автомобілі, коли він їде?", ["Запасне"]),
    Question("На небі одна, у баби дві, а у дівки немає.", ["Б"]),
    Question("Коли ми, дивлячись на цифру «два» кажемо «десять».", ["Коли стрілка годинника показує десять хвилин."]),
    Question("Складіть віршик з шести літер.", ["Віршик"]),
    Question("Їде чоловік у потязі, сниться йому, що сидить він на підлозі, а дошки у безодню летять. Глядь—лише одна дошка залишилась. Що треба зробити чоловіку, аби не впасти?", ["Прокинутись"]),
    Question("Від чого у качки ноги червоні?", ["Від колін"]),
    Question("В якому морі води немає?", ["У тому, що на карті в атласі."]),
    Question("Сорок п’ят і сорок п’ят — скільки буде?", ["85"]),
    Question("Що дістане зубами потилицю?", ["Гребінець"]),
    Question("Який острів каже, що він одяг?", ["Ямайка"]),
    Question("Ішли дві матері і дві дочки. Знайшли три яблука і поділились. Кожній дісталось по одному. Як так вийшло?", ["Внучка, мама та бабуся"]),
    Question("Яке ім’я хлопчика вперед і назад читається однаково?", ["Пилип"]),
    Question("Коли людина в кімнаті може бути без голови?", ["Коли виглядає у вікнот"]),
    Question("Коли дурень розумний?", ["Коли мовчить"]),
    Question("Що спочатку треба зробити, лягаючи спати?", ["Сісти"]),
    Question("У млині було вісім мішків, на кожному мішку сиділо по дві миші, прийшов мельник з котом, скільки тепер стало ніг?", ["Дві ноги мельника"]),
    Question("Хто показує кожному його обличчя, бо не має власного?", ["Дзеркало"]),
]

quiz1 = quiz_system.quiz_manager.create_quiz(admin_user, quiz1_name, quiz1_questions)
quiz2 = quiz_system.quiz_manager.create_quiz(admin_user, quiz2_name, quiz2_questions)

quiz_system.display_menu()

