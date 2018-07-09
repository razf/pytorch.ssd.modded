import torch.optim as optim
def choose_optimizer(optim_name,ler,mom,weights_d,net):
  if optim_name == 'Adadelta':
    optimizer = optim.Adadelta(net.parameters(), lr=ler, momentum=mom,
                      weight_decay=weights_d);
  elif optim_name == 'RMSProp':
    optimizer = optim.RMSProp(net.parameters(), lr=ler,
                      weight_decay=weights_d);
  elif optim_name == 'Adam':
    optimizer = optim.Adam(net.parameters(), lr=ler,
                      weight_decay=weights_d);
  else: 
    optimizer = optim.SGD(net.parameters(), lr=ler, momentum=mom,
                      weight_decay=weights_d);
  return optimizer