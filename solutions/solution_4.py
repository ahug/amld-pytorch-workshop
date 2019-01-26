import torch.nn as nn
import torch.nn.functional as F

class MLP(nn.Module):
    def __init__(self, in_size, h1_dim, h2_dim, num_classes):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(input_size, h1_dim)
        self.fc2 = nn.Linear(h1_dim, h2_dim)
        self.fc3 = nn.Linear(h2_dim, num_classes)
    
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        return F.softmax(x)
    