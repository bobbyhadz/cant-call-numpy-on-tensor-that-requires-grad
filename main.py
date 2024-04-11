# Python: Can't call numpy() on Tensor that requires grad


import torch

t = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)

print(t)  # 👉️ tensor([1., 2., 3.], requires_grad=True)
print(type(t))  # 👉️ <class 'torch.Tensor'>

# ✅ Call detach() before calling numpy()
t = t.detach().numpy()

print(t)  # 👉️ [1. 2. 3.]
print(type(t))  # 👉️ <class 'numpy.ndarray'>