import random
import string
import time


# user class containing name and highscores
class User:
    def __init__(self, name):
        self.name = name
        self.high_score_dict = {
            'easy': [0, 0, 0, 0],
            'medium': [0, 0, 0, 0],
            'hard': [0, 0, 0, 0],
            'insane': [0, 0, 0, 0]
        }


# quick match class, has game functionalities accepts user object to update highscore
class QuickMaths:
    def __init__(self, user):
        self.user = user

    def play_game(self):
        score, difficulty, duration = self.start_game()
        self.show_score(score, difficulty, duration)

    def start_game(self):
        # intialize score variable
        score = 0
        # create difficulty ls dict
        # each difficulty has a list of operators the number of each operator affects their likelihood of occurence
        difficulty_ls_dict = {
            'easy': ['+', '-'],
            'medium': ['+'] * 2 + ['-'] * 2 + ['*'],
            'hard': ['+'] * 2 + ['-'] * 2 + ['*'] * 3 + ['/'] * 3,
            'insane':
            ['+'] * 1 + ['-'] * 1 + ['*'] * 4 + ['/'] * 3 + ['**'] * 1
        }

        # creates random on/off switch
        random_bool = [True, False]

        # difficulty selection loop
        while True:
            # get difficulty from user
            difficulty = input(
                'Please Choose a difficulty level \n1.) Easy \n2.) Medium \n3.) Hard\n4.) Insane \n'
            )

            # map user selection to difficulty
            difficulty = DIFFICULTY_SELECTION_DICT.get(difficulty)

            # selection is invalid print invalid selection or break out difficulty selection loop if correct selection
            if difficulty is None:
                print('Invalid Selection')
            else:
                break

        # duration selection loop
        while True:
            # get duration from user
            duration = input(
                'Select Duration \n1.) 30secs \n2.) 45secs \n3.) 1min \n4.) 2mins \n'
            )

            # map user selection to duratiob
            duration = DURATION_DICT.get(duration)

            # selection is invalid print invalid selection or break out duration selection loop if correct selection
            if duration is None:
                print('Invalid Selection')
            else:
                break

        # if difficulty is easy or medium
        if difficulty in ['easy', 'medium']:
            # get the operarator list for selected difficulty
            difficulty_ls = difficulty_ls_dict.get(difficulty)

            # start time
            start = time.time()
            end = time.time()

            # start questioning loop, break out when time is finished
            while end - start < duration:
                # create evalaution string from randomly selected number from 1 - 5 and randomly selected operator
                # from difficulty operator list
                evaluation_string = '{} {} {} {} {}'.format(
                    random.randrange(1, 7), random.choice(difficulty_ls),
                    random.randrange(1, 7), random.choice(difficulty_ls),
                    random.randrange(1, 7))
                # show string
                print(evaluation_string)
                # evalauate string
                answer = eval(evaluation_string)
                # get user's answer
                user_answer = input('Solution: ')

                # validate user input
                try:
                    user_answer = float(user_answer)
                except ValueError:
                    user_answer = None

                # check time
                end = time.time()

                # if user answer is correct add 1 to score if not ask another question if within time limit
                if user_answer != float(answer):
                    print('Wrong answer Chief')
                else:
                    if end - start < duration:
                        print('Correct')
                        score += 1
                    else:
                        break
                    print(
                        f'Time remaining: {time.strftime("%M:%S", time.gmtime(duration - (end - start)))}'
                    )
                continue

        # if difficulty is hard
        elif difficulty == 'hard':
            # get the operarator list for selected difficulty
            difficulty_ls = difficulty_ls_dict.get(difficulty)

            # start time
            start = time.time()
            end = time.time()

            # check time limit for loop
            while end - start < duration:
                # ensure that the final answer is not a decimal, create new questions if within time limit
                answer = 0.1
                while (float(answer) -
                       int(answer)) != 0 and end - start < duration:
                    # add brackets randomly (50/ 50 chance)
                    bracket_string = '{} {} {} {} {} {} {}'
                    if random.choice(random_bool):
                        bracket_string = insert_brackets(bracket_string)
                    evaluation_string = bracket_string.format(
                        random.randrange(1, 9), random.choice(difficulty_ls),
                        random.randrange(1, 9), random.choice(difficulty_ls),
                        random.randrange(1, 9), random.choice(difficulty_ls),
                        random.randrange(1, 9))

                    answer = eval(evaluation_string)
                print(evaluation_string)
                user_answer = input('Solution: ')

                # get user answer and compare
                try:
                    user_answer = float(user_answer)
                except ValueError:
                    user_answer = None

                end = time.time()
                if user_answer != float(answer):
                    print('Wrong answer')
                else:
                    if end - start < duration:
                        print('Nice, correct')
                        score += 1
                    else:
                        break
                    print(
                        f'Time remaining: {time.strftime("%M:%S", time.gmtime(duration - (end - start)))}'
                    )
                continue
        else:
            # similar logic to hard
            difficulty_ls = difficulty_ls_dict.get(difficulty)
            start = time.time()
            end = time.time()
            while end - start < duration:
                answer = 0.1
                while (float(answer) -
                       int(answer)) != 0 and end - start < duration:
                    a = random.randrange(1, 9)
                    a_op = random.choice(difficulty_ls)
                    b = random.randrange(
                        1, 9) if a_op != '**' else random.randrange(2, 3)
                    b_op = random.choice(difficulty_ls)
                    c = random.randrange(
                        1, 9) if b_op != '**' else random.randrange(2, 3)
                    c_op = random.choice(difficulty_ls)
                    d = random.randrange(
                        1, 9) if c_op != '**' else random.randrange(2, 3)
                    d_op = random.choice(difficulty_ls)
                    e = random.randrange(
                        1, 9) if d_op != '**' else random.randrange(2, 3)
                    bracket_string = '{} {} {} {} {} {} {} {} {}'
                    if random.choice(random_bool):
                        bracket_string = insert_brackets(bracket_string)
                    evaluation_string = bracket_string.format(
                        a, a_op, b, b_op, c, c_op, d, d_op, e)
                    try:
                        answer = eval(evaluation_string)
                    except ZeroDivisionError:
                        continue
                print(evaluation_string)
                user_answer = input('Solution: ')
                try:
                    user_answer = float(user_answer)
                except ValueError:
                    user_answer = None

                end = time.time()
                if user_answer != float(answer):
                    print('Wrong answer, Chief')
                else:
                    if end - start < duration:
                        print('Nice, Correct')
                        score += 1
                    else:
                        break
                    print(
                        f'Time remaining: {time.strftime("%M:%S", time.gmtime(duration - (end - start)))}'
                    )
                continue
        return score, difficulty, duration

    def show_score(self, score, difficulty, duration):
        # get score list for difficulty for user
        score_ls = self.user.high_score_dict.get(difficulty)
        i = 0
        # get score for particular game duration
        for time_duration in DURATION_NAME_DICT:
            if time_duration == duration:
                break
            i += 1
        # check if current score is higher than current highscore for mode and duration
        # if it is update it and let user know
        if score > score_ls[i]:
            print(
                'Your score is {}. {}, you just broke your highscore for {} mode ({})'
                .format(score,
                        str(self.user.name).upper(),
                        str(difficulty).upper(),
                        DURATION_NAME_DICT.get(duration)))
            score_ls[i] = score
        else:
            print(
                'You answered {} questions correctly in {} in {} mode. Great job!'
                .format(score, DURATION_NAME_DICT.get(duration),
                        str(difficulty).upper()))


# function to randomly insert brackets
def insert_brackets(bracket_string):
    bracket_string = bracket_string.split()
    bracket_insert = random.randrange(0, len(bracket_string) - 2, 2)
    bracket_string.insert(bracket_insert, '(')
    bracket_string.insert(bracket_insert + 4, ')')

    bracket_string = ' '.join(bracket_string)

    return bracket_string


# create new user or get previous user
def get_user(user_ls):
    while True:
        user_name = input('Enter name ')
        valid = validate_name(user_name)
        if valid:
            break
    current_user = None
    for user in user_ls:
        if str(user_name).strip().lower() == user.name.strip().lower():
            print(f'Welcome back {str(user.name).upper()}')
            current_user = user
            break
    if current_user is None:
        current_user = User(user_name.strip().lower())
        user_ls.append(current_user)
        print(f"Let's get started, {str(current_user.name).upper()}")
    return current_user, user_ls


# shows the highscore table
def show_high_score_table(user_ls):
    # selection loop for difficulty and duration
    # difficulty
    while True:
        difficulty_input = input(
            'Please Choose a difficulty level \n1.) Easy \n2.) Medium \n3.) Hard\n4.) Insane\n'
        )

        if difficulty_input in ['1', '2', '3', '4']:
            break
        else:
            print('Invalid Selection, Try again!')
    difficulty = DIFFICULTY_SELECTION_DICT.get(difficulty_input)

    # duration
    while True:
        duration = input(
            'Select Duration \n1.) 30secs \n2.) 45secs \n3.) 1min \n4.) 2mins \n'
        )
        if duration in DURATION_DICT:
            duration_index = int(float(duration)) - 1
            duration_name = DURATION_NAME_DICT.get(DURATION_DICT.get(duration))
            break
        else:
            print('Invalid Selection, Try again!')

    # sort user list based on their highscore for that difficulty and duration (uses bubble sort)
    sort_user_ls(user_ls, duration_index, difficulty)

    # format highscore table
    print(f'High Score Table for {duration_name}'.center(20))
    print('    ' + 'Name'.center(10) + 'Score'.center(10))
    idx = 1
    prev_value = None
    for user in user_ls:
        if user.high_score_dict.get(difficulty)[duration_index] == 0:
            continue
        if prev_value == user.high_score_dict.get(difficulty)[duration_index]:
            use_idx = prev_idx
        else:
            use_idx = idx
        print((str(use_idx) + '.').center(4) +
              str(user.name).upper().center(10) +
              str(user.high_score_dict.get(difficulty)[duration_index]).center(
                  10))
        prev_value = user.high_score_dict.get(difficulty)[duration_index]
        prev_idx = idx
        idx += 1
    print('\n')


# functions sort user_ls list in descending order based on given difficulty and duration (bubble sort)
def sort_user_ls(user_ls, index, difficulty):
    n = len(user_ls)
    change = True
    while change:
        change = False
        for i in range(n - 1):
            if user_ls[i].high_score_dict.get(difficulty)[index] < user_ls[
                    i + 1].high_score_dict.get(difficulty)[index]:
                next = user_ls[i + 1]
                current = user_ls[i]

                user_ls[i + 1] = current
                user_ls[i] = next
                change = True


def validate_name(name):
    if len(name) >= 4 and len(name) <= 10:
        for letter in name:
            if letter not in string.ascii_letters and letter not in string.digits:
                print('Name must contain only alphanumeric characters')
                return False
        return True

    else:
        print('Name must have characters must be between 4 - 10 characters')
        return False


DIFFICULTY_SELECTION_DICT = {
    '1': 'easy',
    '2': 'medium',
    '3': 'hard',
    '4': 'insane'
}

DURATION_DICT = {'1': 30, '2': 45, '3': 60, '4': 120}

DURATION_NAME_DICT = {30: '30 secs', 45: '45 secs', 60: '1 min', 120: '2 min'}
