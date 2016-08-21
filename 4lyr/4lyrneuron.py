__author__ = 'manmeet'

# Back-Propagation Neural Networks
#
import math
import random

random.seed(0)

# calculate a random number where:  a <= rand < b
def rand(a, b):
    return (b-a)*random.random() + a

# Make a matrix (we could use NumPy to speed this up)
def makeMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill]*J)
    return m

# our sigmoid function, tanh is a little nicer than the standard 1/(1+e^-x)
def sigmoid(x):
    return math.tanh(x)

# derivative of our sigmoid function, in terms of the output (i.e. y)
def dsigmoid(y):
    return 1.0 - y**2

class NN:
    def __init__(self, ni, nh1,nh2, no):
        # number of input, hidden, and output nodes
        self.ni = ni + 1 # +1 for bias node
        self.nh1 = nh1
        self.nh2 = nh2
        self.no = no

        # activations for nodes
        self.ai = [1.0]*self.ni
        self.ah1 = [1.0]*self.nh1
        self.ah2 = [1.0]*self.nh2
        self.ao = [1.0]*self.no

        # create weights
        self.wi = makeMatrix(self.ni, self.nh1)
        self.wh1 = makeMatrix(self.nh1, self.nh2)
        self.wo = makeMatrix(self.nh2, self.no)
        # set them to random vaules
        for i in range(self.ni):
            for j in range(self.nh1):
                self.wi[i][j] = rand(-0.2, 0.2)
        for j in range(self.nh1):
            for k in range(self.nh2):
                self.wh1[j][k] = rand(-2.0, 2.0)
        for k in range(self.nh2):
            for l in range(self.wo):
                self.wo[j][k] = rand(-2.0, 2.0)


        # last change in weights for momentum
        self.ci = makeMatrix(self.ni, self.nh1)
        self.ch1 = makeMatrix(self.nh1, self.nh2)
        self.co = makeMatrix(self.nh2, self.no)

    def update(self, inputs):
        if len(inputs) != self.ni-1:
            raise ValueError('wrong number of inputs')

        # input activations
        for i in range(self.ni-1):
            #self.ai[i] = sigmoid(inputs[i])
            self.ai[i] = inputs[i]

        # hidden activations
        for j in range(self.nh1):
            sum = 0.0
            for i in range(self.ni):
                sum = sum + self.ai[i] * self.wi[i][j]
            self.ah1[j] = sigmoid(sum)

				for k in range(self.nh2):
        	sum = 0.0
					for j in range(self.nh1):
                sum = sum + self.ah1[j] * self.wh1[j][k]
          self.ah2[k] = sigmoid(sum)

       # output activations
        for l in range(self.no):
            sum = 0.0
            for k in range(self.nh2):
                sum = sum + self.ah2[k] * self.wo[k][l]
            self.ao[l] = sigmoid(sum)

        return self.ao[:]


    def backPropagate(self, targets, N, M):
        if len(targets) != self.no:
            raise ValueError('wrong number of target values')

        # calculate error terms for output
        output_deltas = [0.0] * self.no
        for l in range(self.no):
            error = targets[l]-self.ao[l]
            output_deltas[l] = dsigmoid(self.ao[l]) * error

        # calculate error terms for hidden
        hidden_deltas2 = [0.0] * self.nh2
        for k in range(self.nh2):
            error = 0.0
            for l in range(self.no):
                error = error + output_deltas[l]*self.wo[k][l]
            hidden_deltas2[k] = dsigmoid(self.ah2[k]) * error

         hidden_deltas1 = [0.0] * self.nh1
        for j in range(self.nh1):
            error = 0.0
            for k in range(self.nh2):
                error = error + hidden_deltas2[k]*self.wh2[j][k]
            hidden_deltas1[j] = dsigmoid(self.ah1[j]) * error

       # update output weights
        for k in range(self.nh2):
            for l in range(self.no):
                change = output_deltas[l]*self.ah2[k]
                self.wo[k][l] = self.wo[k][l] + N*change + M*self.co[k][l]
                self.co[k][l] = change
                #print N*change, M*self.co[j][k]

        # update hidden weights
        for j in range(self.nh1):
            for k in range(self.nh2):
                change = hidden_deltas2[k]*self.ah2[j]
                self.wh1[j][k] = self.wh1[j][k] + N*change + M*self.co[j][k]
                self.ch1[j][k] = change
                #print N*change, M*self.co[j][k]

       # update input weights
        for i in range(self.ni):
            for j in range(self.nh1):
                change = hidden_deltas1[j]*self.ai[i]
                self.wi[i][j] = self.wi[i][j] + N*change + M*self.ci[i][j]
                self.ci[i][j] = change

        # calculate error
        error = 0.0
        for k in range(len(targets)):
            error = error + 0.5*(targets[k]-self.ao[k])**2
        return error


    def test(self, patterns):
        for p in patterns:
            print(p[0], '->', self.update(p[0]))

    def weights(self):
        print('Input weights:')
        for i in range(self.ni):
            print(self.wi[i])
        print()
        print('Output weights:')
        for j in range(self.nh):
            print(self.wo[j])

    def train(self, patterns, iterations=10000, N=0.5, M=0.1):
        # N: learning rate
        # M: momentum factor
        for i in range(iterations):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.update(inputs)
                error = error + self.backPropagate(targets, N, M)
            if i % 100 == 0:
                print('error %-.5f' % error)


def demo():
    # Teach network XOR function
    pat = [
        [[0,0], [0]],
        [[0,1], [1]],
        [[1,0], [1]]
#        [[1,1], [1]]
    ]

    # create a network with two input, two hidden, and one output nodes
    n = NN(2, 10,10, 1)
    # train it with some patterns
    n.train(pat)
    # test it
#    n.test([[[1,1],[1]]])
    n.test([[[1,1]]])



if __name__ == '__main__':
    demo()
