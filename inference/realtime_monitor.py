import torch
import pandas as pd
from models.temporal_model import LSTMPredictor
from utils.device import get_device
from inference.risk_score import risk_score

device = get_device()
model = LSTMPredictor(5).to(device)
model.load_state_dict(torch.load("model.pt", map_location=device))
model.eval()

data = pd.read_csv("data/sample.csv").values
window = torch.tensor(data[:30], dtype=torch.float32).unsqueeze(0).to(device)

with torch.no_grad():
    pred = model(window)
    score = risk_score(pred, window)

print("Risk score:", score[0])