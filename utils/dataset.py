import torch
from torch.utils.data import Dataset

class TimeSeriesDataset(Dataset):
    def __init__(self, data, window):
        self.data = data
        self.window = window

    def __len__(self):
        return len(self.data) - self.window

    def __getitem__(self, idx):
        x = self.data[idx:idx + self.window]
        y = self.data[idx + 1:idx + self.window + 1]
        return torch.tensor(x, dtype=torch.float32), torch.tensor(y, dtype=torch.float32)