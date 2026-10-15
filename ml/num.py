import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import numpy as np


# -------------------------
# 1. Dataset
# -------------------------

class NumberDataset(Dataset):

    def __init__(self):
        pass

    def __len__(self):
        return 1000

    def __getitem__(self, index):

        # Work out which number and which image
        n = index // 100
        file = index % 100

        # Open image
        image = Image.open(f"numbers/{n}-{file}.png").convert("L")

        # Make sure it is 28 x 28
        image = image.resize((28, 28))

        # Convert image to NumPy array
        array = np.array(image)

        # Turn 28 x 28 into 784 values
        array = array.flatten()

        # Convert to PyTorch tensor
        tensor = torch.tensor(array, dtype=torch.float32)

        return tensor, n


# -------------------------
# 2. Dataset and DataLoader
# -------------------------

dataset = NumberDataset()

loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True
)


# Check Dataset
image, number = dataset[0]

print(image.shape)
print(number)

for images, numbers in loader:
    print(images.shape)
    print(numbers.shape)
    break


# -------------------------
# 3. Create the model
# -------------------------

model = nn.Sequential(
    nn.Linear(784, 120),
    nn.ReLU(),

    nn.Linear(120, 60),
    nn.ReLU(),

    nn.Linear(60, 10)
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

    for images, numbers in loader:

        # Make prediction
        prediction = model(images)

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

image = Image.open("ml/traningdNum/1.png").convert("L")

# IMPORTANT: make test image 28 x 28
image = image.resize((28, 28))

array = np.array(image)

array = array.flatten()

test = torch.tensor(array, dtype=torch.float32)

# Give image to model
answer = model(test)

print("Model output:")
print(answer)

# Find the output with the highest value
prediction = torch.argmax(answer)

print("Predicted number:", prediction.item())