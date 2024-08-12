import torch

# Assuming hidden_states is a tensor of shape (seq_len, hidden_size)
hidden_states = ...

# Calculate the average
avg_hidden_state = torch.mean(hidden_states, dim=0)

# avg_hidden_state is now a fixed-size embedding
