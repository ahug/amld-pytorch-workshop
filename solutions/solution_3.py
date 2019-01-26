y = f(x)
y.backward()
x.data = x - lr * x.grad
x.grad.zero_()  # Try commenting that line !


optimizer.zero_grad()
y = f(x)
y.backward()
optimizer.step()
