
# TRAINING WITH RANDOM WEIGHTS



import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))   # to make the values between 0 and 1 

training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])


training_outputs = np.array([[0,1,1,0]]).T   #transposing the output to math the matrix

#initialising our weight , assigning random values 

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3,1)) - 1

print('Random starting snaptic weights: ')

print(synaptic_weights)

for iteration in range(1):

    input_layer = training_inputs 


    outputs = sigmoid(np.dot(input_layer,synaptic_weights))

print('Outputs after training :')
print(outputs)




