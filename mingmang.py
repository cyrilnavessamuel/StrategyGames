class mingmang:
    def __init__(self):
        self.dim = 0;
        self.board = [];

    # Initialise the 2d Array Board with the pawns of Player 1 and 2
    def newBoard(self, n):
        for i in range(0, n):
            row = [];
            for j in range(0, n):
                row.insert(j, 0);
            self.board.insert(i, row);
        for i in range(0, n):
            for j in range(0, n):
                if (i == 0 and j == 0):
                    self.board[i][j] = 1;
                elif (i == 0):
                    self.board[i][j] = 2;
                elif (j == 0):
                    self.board[i][j] = 1;
                elif (i == n - 1 and j == n - 1):
                    self.board[i][j] = 2;
                elif (i == n - 1):
                    self.board[i][j] = 1;
                elif (j == n - 1):
                    self.board[i][j] = 2;

        return self.board;

    # Display the board with the pawn positions
    def display(self, board, n):
        for i in range(0, n):
            row = [];
            for j in range(0, n):
                num = board[i][j];
                strinum = "";
                if (num == 0):
                    strinum = "."
                elif (num == 1):
                    strinum = "x";
                elif (num == 2):
                    strinum = "o";
                row.insert(j, strinum);
            print(row);

    # Define a pawn is allowed for the player
    def possiblePawn(self, board, n, player, i, j):
        if (player == board[i][j]):
            return True;
        else:
            return False;

    # Select a pawn to move
    def selectPawn(self, board, n, player):
        pospawn=True;
        while(pospawn):
         cord = [];
         row = int(input("Enter the pawn row co-ordinate"));
         column = int(input("Enter the pawn column co-ordinate"));
         cord.insert(0, row);
         cord.insert(1, column);
         if(self.possiblePawn(board,n,player,row,column)):
            pospawn=False;
            posdest = True;
            while(posdest):
             dest = self.selectDestination(board, n, row, column);
             if(self.possibleDestination(board,n,row,column,dest[0],dest[1])):
                self.move(board, n, player, row, column,dest[0],dest[1]);
                posdest=False;
        self.display(self.board, n);

    # Check if the selected destination is valid
    def possibleDestination(self, board, n, i, j, k, l):
        if (i == k and j == l):
            return False;
        elif (board[k][l] > 0):
            return False;
        elif (i == k):
            for a in range(j, l):
                if (board[i][a+1] > 0):
                    return False;
            return True;
        elif (j == l):
            for b in range(i, k):
                if (board[b+1][j] > 0):
                    return False;
            return True;
        else:
            return True;

    # Select a destination to move to
    def selectDestination(self, board, n, i, j):
        cord = [];
        row = int(input("Enter the destination row co-ordinate"));
        column = int(input("Enter the destination column co-ordinate"));
        cord.insert(0, row);
        cord.insert(1, column);
        return cord;

    # Move the piece also look for capture along four sides
    def move(self, board, n, player, i, j, k, l):
        board[i][j] = 0;
        board[k][l] = player;
        # Along columns forward
        for a in range(l+1, n ):
            if (board[k][a] == player):
                count = 0;
                compcount = 0
                for b in range(l + 1, a):
                    count += 1;
                    if (board[k][b] == self.invertplayer(player)):
                        compcount += 1;
                if (count == compcount):
                    for b in range(l + 1, a):
                        board[k][b] = player;
        # Along columns backward
        for a in range(l-1, 0):
            if (board[k][a] == player):
                count = 0;
                compcount = 0
                for b in range(l - 1, a):
                    count += 1;
                    if (board[k][b] == self.invertplayer(player)):
                        compcount += 1;
                if (count == compcount):
                    for b in range(l - 1, a):
                        board[k][b] = player;

        # Along rows forward
        for a in range(k+1, n ):
            if (board[a][l] == player):
                count = 0;
                compcount = 0
                for b in range(k + 1, a):
                    count += 1;
                    if (board[b][l] == self.invertplayer(player)):
                        compcount += 1;
                if (count == compcount):
                    for b in range(k + 1, a):
                        board[b][l] = player;

        # Along rows backward
        for a in range(k-1, 0):
            if (board[a][l] == player):
                count = 0;
                compcount = 0
                for b in range(k - 1, a):
                    count += 1;
                    if (board[b][l] == self.invertplayer(player)):
                        compcount += 1;
                if (count == compcount):
                    for b in range(k - 1, a):
                        board[b][l] = player;

    # Check if no piece move exists for player
    def lose(self,board,n,player):
        for i in range(0, n):
            for j in range(0, n):
                if(board[i][j]==player):
                    if(i+1<=n and board[i+1][j]==0):
                        return False;
                    elif(i-1<=n and board[i-1][j]==0):
                        return False;
                    elif(j+1<=n and board[i][j+1]==0):
                        return False;
                    elif(j-1<=n and board[i][j-1]==0):
                        return False;
                    else:
                        continue;
        return True;

    # Invert the player for utility
    def invertplayer(self,player):
        if (player == 1):
            return 2;
        elif (player == 2):
            return 1;
        elif (player == 0):
            return player;

    def main(self):
        player = 1;
        n = int(input("Enter the no of rows & columns of the board"));
        self.newBoard(n);
        self.display(self.board, n);
        while(not(self.lose(self.board,n,player))):
          print("Player to play is :"+str(player));
          self.selectPawn(self.board,n,player);
          player=self.invertplayer(player);
        print("Game ended Winner is player:"+str(self.invertplayer(player)))



if __name__ == '__main__':
    MingManginstance = mingmang();
    MingManginstance.main();
