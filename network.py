import torch
import torch.nn as nn
import torch.nn.functional as F



class LeNet(nn.Module):
  def __init__(self, in_channels, pools=None):
    """
    LeNet5 architecture
    
    Args:
      in_channels: no of input channels
      pools: Tuple containing two strings, 'max' for maxpools    
    
    """
    super(LeNet, self).__init__()
    self.in_channels = in_channels
    self.pool1 = 'max'
    self.pool2 = 'max'
    
    if pools is not None:
      self.pool1 = pools[0]
      self.pool2 = pools[1]

    self.conv1 = nn.Conv2d(self.in_channels, 6,  kernel_size=5)
    self.maxpool1 = nn.MaxPool2d(2)
    self.avgpool1 = nn.AvgPool2d(2)

    self.conv2 = nn.Conv2d(6, 16, kernel_size=5)
    self.maxpool2 = nn.MaxPool2d(2)
    self.avgpool2 = nn.AvgPool2d(2)

    self.linear1 = nn.Linear(400, 120)
    self.linear2 = nn.Linear(120, 84)
    self.output = nn.Linear(84, 10)

  
  def forward(self, x, activations=None):
    """
    Parameters:
      x: input tenosor 
      activations: set of 5 activation functions for each conv and linear layer.

    """
    act1 = act2 = act3 =  act4 = act5 = torch.relu

    if activations is not None:
      (act1, act2, act3, act4, act5) = activations

    x = act1(self.conv1(x))
    x = self.maxpool1(x) if self.pool1=='max' else self.avgpool1(x)
    
    x = act2(self.conv2(x))
    x = self.maxpool2(x) if self.pool2=='max' else self.avgpool2(x)

    x = x.view(x.shape[0], 16*5*5)
    x = act3(self.linear1(x))
    x = act4(self.linear2(x))
    x = act5(self.output(x))
    
    output = x

    return output