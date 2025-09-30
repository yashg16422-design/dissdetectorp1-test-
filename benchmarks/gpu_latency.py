import torch
import time
from models.temporal_model import LSTMPredictor

x = torch.randn(256, 30, 5)
model = LSTMPredictor(5)

start = time.time()
model(x)
cpu_time = time.time() - start

if torch.cuda.is_available():
    model.cuda()
    x = x.cuda()
    torch.cuda.synchronize()
    start = time.time()
    model(x)
    torch.cuda.synchronize()
    gpu_time = time.time() - start
    print("CPU:", cpu_time, "GPU:", gpu_time)
else:
    print("CPU:", cpu_time)