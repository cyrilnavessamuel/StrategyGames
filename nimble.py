import random


class nimble:
    # Initialisation methods
    def __init__(self):
        self.board = [];
        self.pawn = 0;

    # Define a new board with n square of board
    # P maximum no of pawns
    def newBoard(self, n, p):
        self.pawn = p;
        for i in range(0, n):
            self.board.insert(i, 0);
        for j in range(1, p + 1):
            ran = random.randint(0, n - 1);
            if (self.board[ran] != 0):
                self.board[ran] = self.board[ran] + 1;
            else:
                self.board.insert(ran, 1);
        return self.board;

    # Display the board square with the pawns
    def displayBoard(self, board, n, ):
        output = "";
        scndoutput = "";
        for square in range(0, len(board)):
            output += str(board[square]) + " | ";
        print(output);
        dashoutput = ""
        for l in range(len(output)):
            dashoutput += "-";
        print(dashoutput);
        for square in range(0, len(board)):
            scndoutput += str(square) + " | ";
        print(scndoutput);

    # Possible Squares for a board with
    def possibleSquare(self, board, n, i):
        if (board[i] != 0):
            return True;
        else:
            return False;

    # Select a square to move
    def selectSquare(self, board, n):
        squareinstance = 0;
        possquare=True;
        while(possquare):
         squareinstance = int(input("Enter the square you want to select"))
         if (self.possibleSquare(board, n, squareinstance)):
             possquare=False;
             posdestination = True;
             while(posdestination):
              destinationsquare = self.selectDestination(board, n, squareinstance);
              if (self.possibleDestination(board, n, squareinstance, destinationsquare)):
                posdestination=False;
                self.move(board, n, squareinstance, destinationsquare);
                self.displayBoard(board, n);
                print("next move");
    # Select a possible destination and check to move the pawn to
    def possibleDestination(self, board, n, i, j):
        possiblesquare = [];
        leng = len(board);
        while (i >= 0):
            i = i - 1;
            possiblesquare.append(i);
        if (j in possiblesquare):
            return True;
        else:
            return False;

    # Select the destination of the pawn
    def selectDestination(self, board, n, i):
        square = int(input("Enter the square you want to move to"));
        return square;

    # Move the pawn to destination
    def move(self, board, n, i, j):
        board[i] = board[i] - 1;
        board[j] = board[j] + 1;

    # Check if possible move exists for a player/ no move present in board
    def lose(self, board, n):
        if (board[0] == self.pawn):
            return True;
        else:
            return False;

    def nimbleplay(self, n, p):
        playerno = 0;
        boardinstance = self.newBoard(n, p);
        self.displayBoard(boardinstance, n);
        while (not (self.lose(boardinstance, n))):
            if (playerno == 2):
                playerno -= 1;
            else:
                playerno += 1;
            print("Player" + str(playerno));
            self.selectSquare(boardinstance, n)
        print("Game Finished Winner:Player " + str(playerno));

    def main(self):
        n = int(input("Enter the no of square of the board"));
        print(n);
        p = int(input("Enter the no of pawns"));
        print(p);
        self.nimbleplay(n, p);


if __name__ == '__main__':
    nimbleinstance = nimble();
    nimbleinstance.main();
