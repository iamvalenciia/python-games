# BYUI W02 Prove: Developer - Solo Code Submission
# Author: Juan Valencia


def main():
    array_elements = ([1,'|',2,'|',3],['—','|','—','|','—'],[4,'|',5,'|',6],['—','|','—','|','—'],[7,'|',8,'|',9])

    row1 = array_elements[0]
    row2 = array_elements[2]
    row3 = array_elements[4]

    place1 = row1[0]
    place2 = row1[2]
    place3 = row1[4]

    place4 = row2[0]
    place5 = row2[2]
    place6 = row2[4]

    place7 = row3[0]
    place8 = row3[2]
    place9 = row3[4]

    """We need 10 movements to have a draw"""
    movements = 1

    array_printed(array_elements)
    print('-------------')
    
    end = 'welcome'
    while end == 'welcome':

        #checking the movements of player 1
        player1 = int(input("'o's turn to choose a square (1-9): "))
        print('-------------')

        if player1 == place1 and place1 != 'x':
            array_elements[0][0] = 'o'
            place1 = 'o'
        elif player1 == place2 and place2 != 'x':
            array_elements[0][2] = 'o'
            place2 = 'o'
        elif player1 == place3 and place3 != 'x':
            array_elements[0][4] = 'o'
            place3 = 'o'
        elif player1 == place4 and place4 != 'x':
            array_elements[2][0] = 'o'
            place4 = 'o'
        elif player1 == place5 and place5 != 'x':
            array_elements[2][2] = 'o'
            place5 = 'o'
        elif player1 == place6 and place6 != 'x':
            array_elements[2][4] = 'o'
            place6 = 'o'
        elif player1 == place7 and place7 != 'x':
            array_elements[4][0] = 'o'
            place7 = 'o'
        elif player1 == place8 and place8 != 'x':
            array_elements[4][2] = 'o'
            place8 = 'o'
        elif player1 == place9 and place9 != 'x':
            array_elements[4][4] = 'o'
            place9 = 'o'
        else:
            print('sorry but you missed a shift, this place is already taken')            
        array_printed(array_elements)
        print('-------------')


        """checking win Conditions to player 'o' """
        if checking_win_condition('o', place1, place2, place3, place4, place5, place6, place7, place8, place9) == 1:
            end = 'game over, player "o" win'
            break
        """checking draw"""
        movements += 1
        if movements == 10:
            end = 'Game Over!, this is a draw'
            break


        #checking the movements of player 2
        player2 = int(input("'x's turn to choose a square (1-9): "))
        print('-------------')

        if player2 == place1 and place1 != 'o':
            array_elements[0][0] = 'x'
            place1 = 'x'
        elif player2 == place2 and place2 != 'o':
            array_elements[0][2] = 'x'
            place2 = 'x'
        elif player2 == place3 and place3 != 'o':
            array_elements[0][4] = 'x'
            place3 = 'x'
        elif player2 == place4 and place4 != 'o':
            array_elements[2][0] = 'x'
            place4 = 'x'
        elif player2 == place5 and place5 != 'o':
            array_elements[2][2] = 'x'
            place5 = 'x'
        elif player2 == place6 and place6 != 'o':
            array_elements[2][4] = 'x'
            place6 = 'x'
        elif player2 == place7 and place7 != 'o':
            array_elements[4][0] = 'x'
            place7 = 'x'
        elif player2 == place8 and place8 != 'o':
            array_elements[4][2] = 'x'
            place8 = 'x'
        elif player2 == place9 and place9 != 'o':
            array_elements[4][4] = 'x'
            place9 = 'x'
        else:
            print('sorry but you missed a shift, this place is already taken')
        array_printed(array_elements)
        print('-------------')


        """checking win Conditions to player 'x' """
        if checking_win_condition('x', place1, place2, place3, place4, place5, place6, place7, place8, place9) == 1:
            end = 'game over, player "x" win'
            break

        """checking draw"""
        movements += 1
        if movements == 10:
            end = 'Game Over!, this is a draw'
            break
    print(end)


def array_printed(elements):
    for x in elements:
        for y in x:
            print(y, end='')
        print()
    return True


def checking_win_condition(a, p1, p2, p3 ,p4, p5, p6, p7, p8, p9):
    """ This function will help to know if a player won the game
        a = could be player 'o' or the player 'x' 
        p(1-9) = the places where the player could have been played '"""

    the_break_variable = 0

    if p1 == a and p2 == a and p3 == a:
        end = f"game over, player {a} win"
        the_break_variable = 1
    elif p4 == a and p5 == a and p6 == a:
        end = f"game over, player {a} win"
        the_break_variable = 1
    elif p7 == a and p8 == a and p9 == a:
        end = f"game over, player {a} win"
        the_break_variable = 1
    elif p1 == a and p4 == a and p7 == a:
        end = f"game over, player {a} win"
        the_break_variable = 1
    elif p2 == a and p5 == a and p8 == a:
        end = f"game over, player {a} win"
        the_break_variable = 1
    elif p3 == a and p6 == a and p9 == a:
        end = f"game over, player {a} win"
        the_break_variable = 1
    elif p1 == a and p5 == a and p9 == a:
        end = f"game over, player {a} win"
        the_break_variable = 1
    elif p3 == a and p5 == a and p7 == a:
        end = f"game over, player {a} win"
        the_break_variable = 1
    else:
        the_break_variable = 0
    
    return the_break_variable


if __name__ == "__main__":
    main()


