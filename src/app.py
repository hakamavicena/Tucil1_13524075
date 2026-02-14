import logic, utils

def main():
    start = True
    while(start):
        file = input("Apa nama file:")
        board = utils.file_to_board(file)
        boardValid, boardValidMsg = utils.validate_board(board)
        if not boardValid : print(boardValidMsg)
        n= len(board)
        boardDict = utils.convert_dict(board, n)
        answer, duration = logic.play(boardDict,n)
        if answer == None:
            print('Tidak ada jawabannya, berikan board lain ya :)')
        print(answer)
        utils.interface(boardDict, answer, n)
        print(f'Permainan berlangsung selama {duration*1000} ms dengan brute force algorithm')
        nextGame = input('Mau melanjutkan permainan (y/n): ')
        if(nextGame == 'n'):
            start= False
        elif(nextGame == 'y'):
            start= True
        else:
            print('Input jawaban yang sesuai pls')
            start = False        



     
if __name__ == "__main__":
    main()
    