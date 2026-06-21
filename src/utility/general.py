""" General utility functions for the project """

def check_pytorch_environment():
    import torch
    print('PyTorch version :', torch.__version__)
    print('CUDA available  :', torch.cuda.is_available())
    print('CUDA version    :', torch.version.cuda)
    print('GPU             :', torch.cuda.get_device_name(0))

check_pytorch_environment()