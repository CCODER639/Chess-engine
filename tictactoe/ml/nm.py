
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import pandas as pd
x = 1
# Load CSV
df = pd.read_csv("moves.csv")
def hi1(board1):
    global x
    if x == 1:
        x +=1
        inputs = []
        targets = []

        # Create training examples from consecutive boards
        for i in range(len(df) - 1):
            board = df.iloc[i][['1','2','3','4','5','6','7','8','9']].values.astype(float)
            next_board = df.iloc[i + 1][['1','2','3','4','5','6','7','8','9']].values.astype(float)

            for square in range(9):
                if board[square] != next_board[square]:
                    inputs.append(board)
                    targets.append(square)
                    break

        X = torch.tensor(inputs, dtype=torch.float32)
        y = torch.tensor(targets, dtype=torch.long)


        # Dataset
        class TicTacToeDataset(Dataset):
            def __len__(self):
                return len(X)

            def __getitem__(self, index):
                return X[index], y[index]


        dataset = TicTacToeDataset()
        loader = DataLoader(dataset, batch_size=32, shuffle=True)


        # Model
        model = nn.Sequential(
            nn.Linear(9, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 9)
        )

        loss_function = nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=0.001)


        # Train
        for epoch in range(50):
            for boards, moves in loader:
                prediction = model(boards)
                loss = loss_function(prediction, moves)

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

            print("Epoch:", epoch + 1, "Loss:", loss.item())
        torch.save(model, 'model.pth')

    model = torch.load('model.pth', weights_only=False)
    # Predict a move



    test = torch.tensor(board1, dtype=torch.float32)

    answer = model(test)
    move = torch.argmax(answer).item()

    print("Predicted square:", move + 1)
    return(move + 1)
