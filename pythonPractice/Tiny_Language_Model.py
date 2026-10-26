import torch
import torch.nn as nn
import torch.optim as optim

# 1. Tiny training dataset
text = "cat car can cat car can"

# 2. Create a character vocabulary
chars = sorted(set(text))
char_to_id = {ch: i for i, ch in enumerate(chars)}
id_to_char = {i: ch for ch, i in char_to_id.items()}

# 3. Create input-target pairs
inputs = []
targets = []

for i in range(len(text) - 1):
    inputs.append(char_to_id[text[i]])
    targets.append(char_to_id[text[i + 1]])

X = torch.tensor(inputs)
y = torch.tensor(targets)

# 4. Define a tiny neural network
model = nn.Sequential(
    nn.Embedding(len(chars), 16),
    nn.Linear(16, len(chars))
)

loss_fn = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.03)

# 5. Training loop
for epoch in range(300):
    logits = model(X)
    loss = loss_fn(logits, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 50 == 0:
        print(f"Epoch {epoch + 1}, Loss: {loss.item():.4f}")

print("\nTraining complete!")


model.eval()

print("\nPredictions:")
with torch.no_grad():
    for ch in ["c", "a", "t"]:
        x = torch.tensor([char_to_id[ch]])
        logits = model(x)
        predicted_id = logits.argmax(dim=1).item()
        print(ch, "->", id_to_char[predicted_id])
