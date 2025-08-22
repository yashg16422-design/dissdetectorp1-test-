import torch
from collections import deque

class SlidingWindowInferencer:
    def __init__(self, model, window, device):
        self.model = model
        self.window = window
        self.device = device
        self.buffer = deque(maxlen=window)

    def update(self, sample):
        self.buffer.append(sample)
        if len(self.buffer) < self.window:
            return None
        x = torch.tensor(self.buffer, dtype=torch.float32).unsqueeze(0).to(self.device)
        with torch.no_grad():
            return self.model(x)