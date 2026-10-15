import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import numpy as np
import pandas as pd

# -------------------------
# 1. Dataset
# -------------------------

class NumberDataset(Dataset):

    def __init__(self):
        pass

    def __len__(self):
        return 1000

    def __getitem__(self, index):

        # Open csv
        df = pd.read_csv('moves.csv')

        # Extract our 3 input columns and convert to a PyTorch tensor
        X_data = torch.tensor(df[['1','2','3','4','5','6','7','8','9']].values, dtype=torch.float32)

        # Extract our output target column (Decision) as integer labels
        w_data = torch.tensor(df['winner'].values)


        


        return X_data, w_data


# -------------------------
# 2. Dataset and DataLoader
# -------------------------

dataset = NumberDataset()

loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True
)



# -------------------------
# 3. Create the model
# -------------------------

model = nn.Sequential(
    nn.Linear(9, 64),
    nn.ReLU(),

    nn.Linear(64, 32),
    nn.ReLU(),

    nn.Linear(32, 9)
)


# -------------------------
# 4. Loss function
# -------------------------

loss_function = nn.CrossEntropyLoss()


# -------------------------
# 5. Optimizer
# -------------------------

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)


# -------------------------
# 6. Training
# -------------------------

for epoch in range(50):

    total_loss = 0

    for board, numbers in loader:

        # Make prediction
        prediction = model(board.float())

        # Calculate loss
        loss = loss_function(prediction, numbers)

        # Clear old gradients
        optimizer.zero_grad()

        # Calculate gradients
        loss.backward()

        # Update weights
        optimizer.step()

        total_loss += loss.item()

    print("Epoch:", epoch + 1, "Loss:", total_loss)


# -------------------------
# 7. Test the model
# -------------------------


array = [0,0,1,0,1,1,2,2,0]

test = torch.tensor(array)

# Give image to model
answer = model(test.float())

print("Model output:")
print(answer)

# Find the output with the highest value
prediction = torch.argmax(answer).item()

print("Predicted number:", prediction.item())