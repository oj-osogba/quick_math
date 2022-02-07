from quick_math_helper import QuickMaths, get_user, show_high_score_table


# quick match function
def quick_maths():
    # create list to store user objects
    user_ls = []
    # create user
    current_user, user_ls = get_user(user_ls)
    # enter game loop
    while True:
        # start game session
        quick_maths_session = QuickMaths(current_user)
        # play game
        quick_maths_session.play_game()
        # finish game

        # ask user question if they want to continue (as themselves or new user) or show highscore or end
        while True:
            try_again = input(
                '1.) Try again as current user\n2.) Try again as new user\n3.) Show Highscore Table\n4.) End Game\n'
            )
            if try_again == '1':
                try_again = True
                break
            elif try_again == '2':
                # create the new user object
                current_user, user_ls = get_user(user_ls)
                try_again = True
                break
            elif try_again == '3':
                # show highscore table
                show_high_score_table(user_ls)
            elif try_again == '4':
                try_again = False
                break
            else:
                print('Invalid Selection')
                continue
        if try_again:
            continue
        else:
            break


quick_maths()
