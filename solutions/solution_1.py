torch.arange(5, 16, 2)

2 * torch.eye(5) + 5 * torch.ones(5)

x = torch.arange(3).unsqueeze(1)

torch.arange(2,9,2).view(4,1).expand(4,5)

(x-1).nonzero().size(0)

x[x == 0].size(0) or (x == 0).sum()

X[Y > Y.mean()]

(X.sign() - 1).nonzero().size(0) or (1 - X.sign()).div(2).sum()  # Definitely not the best ways to do ... just for the example 

X.logsumexp(0) or X.exp().sum().log()

tensor.view(-1, 1).expand(-1, tensor.size(0)).cumprod(dim=1) or x.view(-1, 1).pow(torch.arange(0, x.size(0), dtype=torch.float))

if torch.cuda.is_available():
    x.cuda()






np.arange(5, 20, 2)

5*torch.ones(5,5) + 2*torch.eye(5)

torch.arange(4, 33, 2).view(3, 5)

torch.arange(2, 10, 2).view(4, 1).expand(4, 5)

(X**2).sum(dim=1).sqrt()

(X!=0).sum().item()

X[X > int(X.float().mean())]