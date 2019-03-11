""" Illustrate how gradient decent works

Formulas:
https://medium.com/meta-design-ideas/linear-regression-by-using-gradient-descent-algorithm-your-first-step-towards-machine-learning-a9b9c0ec41b1

NumPy implementation (make things simpler):
https://towardsdatascience.com/linear-regression-using-gradient-descent-in-10-lines-of-code-642f995339c0

Expand things to multi-variate and SGD:
https://towardsdatascience.com/gradient-descent-in-python-a0d07285742f

Conclusions: Note that mini-batch with size=1 has many more updates and converges much faster compared to the full SGD
"""

import random

# First, generate data
A = 2
B = 5
N = 1000  # number of examples
E = 0.0000000001  # error
LR = 0.0001  # default learning rate
EPOCH = 200
X_RANGE_LOW = 0
X_RANGE_HIGH = 100

# formula: Y=AX+B
X, Y = [], []
for _ in range(N):
    x_base = random.randrange(X_RANGE_LOW, X_RANGE_HIGH)
    X.append(x_base + random.uniform(0, E))
    Y.append(A * x_base + B + random.uniform(0, E))
print(list(zip(X, Y)))


# compute total loss over X and Y given a and b values
def loss(a, b):
    s = 0.0
    for x_i, y_i in zip(X, Y):
        s += (y_i - (x_i * a + b)) ** 2
    return s / N


# This works for both GD and SGD
# Given the formula Y=AX+B and values of X and Y, we want to fit A and B. this is a single epoch.
def descent_epoch(x, y, a_init, b_init):
    n = float(len(x))
    a_curr, b_curr = a_init, b_init
    # compute gradient
    g_a, g_b = 0.0, 0.0
    h_a, h_b = 0.0, 0.0     # gradient to check using a different approach
    lv = 0.0
    for x_i, y_i in zip(x, y):
        # this is the feedforward + backprop approach.
        # feed forward is mainly to calculate the values to help compute gradient during back prop

        # feed forward
        t1 = a_curr * x_i
        t2 = t1 + b_curr
        t3 = t2 - y_i
        t4 = t3 ** 2.0
        t5 = (1.0/(2*n)) * t4   # we use 1/2n here to cancel out x**2 derivative
        # finally do the sum to produce the final loss score.
        # the loss score is not needed to produce back prop though, because back prop always starts with 1.0
        lv += t5
        # print(f'Loss: {lv}')

        # back prop
        u1 = 1.0
        u2 = (1.0/(2*n)) * u1
        u3 = 2 * t3 * u2     # this is the derivative of x**2 => 2 * x
        u4_x = 1.0 * u3       # "-" node derivative is just the original
        # u4_y = -1 * u3     # this branch of gradient is no need to compute, because we won't update y.
        g_b += 1.0 * u4_x     # "+" node just pass through the gradient to "b" node
        u5 = u4_x
        g_a += x_i * u5
        # u5_x = a_curr * u5   # this is not needed because we don't update x.

        # here is the final results from taking derivates directly
        # 1/n is unnecessary because we'll scale by learning_rate anyways. but this helps make learning rate independent from the size of mini batch for multiple runs
        h_a += (1.0/n) * x_i * (a_curr * x_i + b_curr - y_i)
        h_b += (1.0/n) * (a_curr * x_i + b_curr - y_i)
        assert abs(g_a - h_a) < 0.0001 and abs(g_b - h_b) < 0.0001, (g_a, h_a, g_b, h_b)

    # decent with learning rate
    a_curr -= g_a * LR
    b_curr -= g_b * LR

    return a_curr, b_curr


# This is full gradient descent
def full():
    a, b = random.random(), random.random()
    for epoch in range(EPOCH):
        lv = loss(a, b)
        print(f'{epoch}:\t{a}\t{b}\t{lv}')
        # pass all data to compute gradient
        a, b = descent_epoch(X, Y, a, b)
    # print(a, b)


# This is mini-batch with batch size 1
def batch(bs=1):
    a, b = random.random(), random.random()
    assert N % bs == 0
    bn = N // bs    # number of batches
    for epoch in range(EPOCH):
        lv = loss(a, b)
        print(f'{epoch}:\t{a}\t{b}\t{lv}')
        # pass batches to compute gradient
        # note that each batch we do an update, which means updates happen much more often
        for batch in range(bn):
            x = X[batch*bs: (batch+1)*bs]
            y = Y[batch*bs: (batch+1)*bs]
            a, b = descent_epoch(x, y, a, b)

# full()
batch(bs=1)

