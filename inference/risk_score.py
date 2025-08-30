import torch
import numpy as np

def risk_score(pred, target):
    return torch.mean((pred - target) ** 2, dim=(1, 2)).cpu().numpy()