import torch
import torch.nn as nn

class TemporalTransformer(nn.Module):
    def __init__(self, features, d_model=64, nhead=4, layers=3):
        super().__init__()
        self.input_proj = nn.Linear(features, d_model)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            batch_first=True
        )
        self.encoder = nn.TransformerEncoder(encoder_layer, layers)
        self.output_proj = nn.Linear(d_model, features)

    def forward(self, x):
        x = self.input_proj(x)
        x = self.encoder(x)
        return self.output_proj(x)