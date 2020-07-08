import requests
from pathlib import Path
import gzip
import pickle
import torch
from torch.utils.data import DataLoader, TensorDataset
import torch.nn.functional as F
from itertools import combinations_with_replacement
import math

def load_dataset(url,batch_size, save_location='/content'):
  data = Path(save_location+ '/data/mnist')
  data.mkdir(parents=True, exist_ok=True)
  file_location = data / 'mnist.pkl.gz'
  if file_location.exists() is False:
    content= requests.get(url).content
    file_location.open('wb').write(content)
  else:
    print("File already exists "+file_location.as_posix())
  ((x_train, y_train), (x_test, y_test), _) =  pickle.load(gzip.open(file_location.as_posix(), 'rb'), encoding="latin-1")
  x_train, y_train, x_test, y_test = map(torch.tensor, (x_train,y_train,x_test,y_test))
  train_loader = DataLoader(TensorDataset(x_train, y_train), batch_size, shuffle=True)
  test_loader = DataLoader(TensorDataset(x_test, y_test), batch_size, shuffle=True)
  return train_loader, test_loader




def check_accuracy(test_loader, model, use_cuda=False):
  correct_test, total_test = 0,0
  with torch.no_grad():
    for data in test_loader:
      image, label = data
      if use_cuda:
        image, label=image.cuda(), label.cuda()
      _, predicted_test = torch.max(model(F.interpolate(image.unsqueeze(1).reshape([image.shape[0],1, 28,28]), 32)), 1)
      total_test += label.size(0)
      correct_test += (predicted_test == label).sum().item()

  accuracy_test = (100 * correct_test / total_test)
  print("Accuracy on test: {}".format(accuracy_test))
  return accuracy_test

def lr_decay(start, end):
  rate = []
  for i in range(start, end):
    rate.append(1 / (1 + 1 * i)* 0.2)
  return rate

def combination(list_of_item, max_no):
  total = []
  for item in combinations_with_replacement(list_of_item, max_no):
    total.append(item)
  return total
