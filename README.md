# LeNet5
Implementation  of LeNet5 architecture.

---
## About
LeNet5 was the first convolution neural network architecture proposed by yann le cun in 1989. This classical architecture is  inspiration of latest architectures.

## Architecture

Its architecture is simple, yet powerful. It has input size of (32,32) and going, it follows convolution, Pooling and non-linear.
Description as Below:

1. Every convolutional layer includes three parts: convolution, pooling, and nonlinear activation functions
2. Using convolution to extract spatial features (Convolution was called receptive fields originally)
3. Subsampling average pooling layer
4. tanh activation function
5. Using MLP as the last classifier
6. Sparse connection between layers to reduce the complexity of computational



## Structure
![Diagram]("/LeNet_architecture.png")
`Input(1, 32,32) => Convolution(6,28,28) => pool(6,14,14) => Convolution(16,10,10) => pool(16,5,5) => Linear(120) => Linear(84) => Output(10)`

## Results
Here is my results experimenting on mnist handwritten dataset on LeNet architecture.

#### learning rate decays and results

---


---

### References
- [LeNet5 Wiki](https://en.wikipedia.org/wiki/LeNet)
- [LeNet Paper](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf)
