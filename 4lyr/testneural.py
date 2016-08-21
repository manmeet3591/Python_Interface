from neuron3 import NN  
# Teach network XOR function
pat = [ [[0,0], [0]], [[0,1], [1]], [[1,0], [1]] ]
#       [[1,1], [1]]
  

    # create a network with two input, two hidden, and one output nodes
n = NN(2, 20, 1)
    # train it with some patterns
n.train(pat)
    # test it
n.test([[[1,1],[1]]])

