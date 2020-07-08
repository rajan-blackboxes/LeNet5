import torch
from torch import optim
import torch.nn as nn
import torch.nn.functional as F


def train(train_loader, model, epochs=10,  **kwargs):
  """
  Args:
    model: LeNet architecture
    epochs: No of iterations to run
    activations: 4 tuple of activation functions
    pools: 2 string of pooling e.g 'max' or 'avg'
    lr: learning rate 
    use_cuda: boolean
    print_every: False
  returns:
    parameterized model
  """

  correct, total = 0.0,0.0
  activations = kwargs.get('activations')
  pools = kwargs.get('pools')
  lr = 0.001 if kwargs.get('lr') == None else kwargs.get('lr')
  use_cuda = True if kwargs.get('use_cuda') == True else False
  early_stop = True if kwargs.get('early_stop') == True else False
  print_every = True if kwargs.get('print_every') == True else False
  model = model(1, pools).cuda() if use_cuda==True else model(1,pools)
  criterion = nn.CrossEntropyLoss()
  optimizer = optim.Adam(model.parameters(), lr)
  for i in range(1, epochs+1):
    for image, label in train_loader:
      if use_cuda:
        image, label = image.cuda(), label.cuda()
      batch = image.shape[0]
      image = F.interpolate(image.unsqueeze(1).reshape([batch,1, 28,28]), size=32)
      pred = model(image, activations)
      _, prediction = torch.max(pred, 1)
      total += label.size(0)
      correct += (prediction == label).sum().item()
      loss = criterion(pred, label)
      loss.backward()
      optimizer.step()
      optimizer.zero_grad()
    accuracy = (100 * correct / total)
    if early_stop:
      if accuracy >= 99:
        print("Accuracy reached 99 breaking....")
        break
    if print_every:
      print("epochs:{}   accuracy: {}".format(i, accuracy))
  return model, accuracy