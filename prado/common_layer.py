import torch 
import torch.nn as nn

class CommonLayers(nn.Module):
    def __init__(self, 
                 mode,
                 regularizer_scale=0.0,
                 weights_initializer='glorot',
                 quantization_enabled=True):
    
nn.init.xavier_uniform_(),