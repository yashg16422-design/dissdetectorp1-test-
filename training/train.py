import torch
import pandas as pd
from torch.utils.data import DataLoader
from models.temporal_model import TemporalTransformer
from utils.dataset import TimeSeriesDataset
from utils.device import get_device

df = pd.read_csv("data/sample.csv").values
dataset = TimeSeriesDataset(df, window=30)
loader = DataLoader(dataset, batch_size=64, shuffle=True)

device = get_device()
model = TemporalTransformer(df.shape[1]).to(device)
optim = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = torch.nn.MSELoss()

for _ in range(5):
    for x, y in loader:
        x, y = x.to(device), y.to(device)
        loss = loss_fn(model(x), y)
        optim.zero_grad()
        loss.backward()
        optim.step()

torch.save(model.state_dict(), "model.pt")