import tensorflow as tf
import tflearn

# Data
X = [[0.04,0.04],[0.11,0.11],[0.23,0.23],[0.26,0.26],[0.3,0.3],[0.38,0.38],[0.46,0.46],[0.55,0.55],[0.62,0.62],[0.64,0.64],[0.71,0.71],[0.77,0.77],[0.82,0.82],[0.87,0.87],[0.93,0.93],[0.98,0.98],[0.04,0.11],[0.11,0.23],[0.23,0.26],[0.26,0.3],[0.3,0.38],[0.38,0.46],[0.46,0.55],[0.55,0.62],[0.62,0.64],[0.64,0.71],[0.71,0.77],[0.77,0.82],[0.82,0.87],[0.87,0.93],[0.93,0.98],[0.98,0.04],[0.04,0.23],[0.11,0.26],[0.23,0.3],[0.26,0.38],[0.3,0.46],[0.38,0.55],[0.46,0.62],[0.55,0.64],[0.62,0.71],[0.64,0.77],[0.71,0.82],[0.77,0.87],[0.82,0.93],[0.87,0.98],[0.93,0.04],[0.98,0.11],[0.04,0.26],[0.11,0.3],[0.23,0.38],[0.26,0.46],[0.3,0.55],[0.38,0.62],[0.46,0.64],[0.55,0.71],[0.62,0.77],[0.64,0.82],[0.71,0.87],[0.77,0.93],[0.82,0.98],[0.87,0.04],[0.93,0.11],[0.98,0.23],[0.04,0.3],[0.11,0.38],[0.23,0.46],[0.26,0.55],[0.3,0.62],[0.38,0.64],[0.46,0.71],[0.55,0.77],[0.62,0.82],[0.64,0.87],[0.71,0.93],[0.77,0.98],[0.82,0.04],[0.87,0.11],[0.93,0.23],[0.98,0.26],[0.04,0.38],[0.11,0.46],[0.23,0.55],[0.26,0.62],[0.3,0.64],[0.38,0.71],[0.46,0.77],[0.55,0.82],[0.62,0.87],[0.64,0.93],[0.71,0.98],[0.77,0.04],[0.82,0.11],[0.87,0.23],[0.93,0.26],[0.98,0.3],[0.04,0.46],[0.11,0.55],[0.23,0.62],[0.26,0.64],[0.3,0.71],[0.38,0.77],[0.46,0.82],[0.55,0.87],[0.62,0.93],[0.64,0.98],[0.71,0.04],[0.77,0.11],[0.82,0.23],[0.87,0.26],[0.93,0.3],[0.98,0.38],[0.04,0.55],[0.11,0.62],[0.23,0.64],[0.26,0.71],[0.3,0.77],[0.38,0.82],[0.46,0.87],[0.55,0.93],[0.62,0.98],[0.64,0.04],[0.71,0.11],[0.77,0.23],[0.82,0.26],[0.87,0.3],[0.93,0.38],[0.9,0.46],[0.04,0.62],[0.11,0.64],[0.23,0.71],[0.26,0.77],[0.3,0.82],[0.38,0.87],[0.46,0.93],[0.55,0.98],[0.62,0.04],[0.64,0.11],[0.71,0.23],[0.77,0.26],[0.82,0.3],[0.87,0.38],[0.93,0.46],[0.98,0.55],[0.04,0.64],[0.11,0.71],[0.23,0.77],[0.26,0.82],[0.3,0.7],[0.38,0.93],[0.46,0.98],[0.55,0.04],[0.62,0.11],[0.64,0.23],[0.71,0.26],[0.77,0.3],[0.82,0.38],[0.87,0.46],[0.93,0.55],[0.98,0.62],[0.04,0.71],[0.11,0.77],[0.23,0.82],[0.26,0.87],[0.3,0.93],[0.38,0.98],[0.46,0.04],[0.55,0.11],[0.62,0.23],[0.64,0.26],[0.71,0.3],[0.77,0.38],[0.82,0.46],[0.87,0.55],[0.93,0.62],[0.98,0.64],[0.04,0.77],[0.11,0.82],[0.23,0.87],[0.26,0.93],[0.3,0.98],[0.38,0.04],[0.46,0.11],[0.55,0.23],[0.62,0.26],[0.64,0.3],[0.71,0.38],[0.77,0.46],[0.82,0.55],[0.87,0.62],[0.93,0.64],[0.98,0.71],[0.04,0.82],[0.11,0.87],[0.23,0.93],[0.26,0.98],[0.3,0.04],[0.38,0.11],[0.46,0.23],[0.55,0.26],[0.62,0.3],[0.64,0.38],[0.71,0.46],[0.77,0.55],[0.82,0.62],[0.87,0.64],[0.93,0.71],[0.98,0.77],[0.04,0.87],[0.11,0.93],[0.23,0.98],[0.26,0.04],[0.3,0.11],[0.38,0.23],[0.46,0.26],[0.55,0.3],[0.62,0.38],[0.64,0.46],[0.71,0.55],[0.77,0.62],[0.82,0.64],[0.87,0.71],[0.93,0.77],[0.98,0.82],[0.04,0.93],[0.11,0.98],[0.23,0.04],[0.26,0.11],[0.3,0.23],[0.38,0.26],[0.46,0.3],[0.55,0.38],[0.62,0.46],[0.64,0.55],[0.71,0.62],[0.77,0.64],[0.82,0.71],[0.87,0.77],[0.93,0.82],[0.98,0.87],[0.04,0.98],[0.11,0.04],[0.23,0.11],[0.26,0.23],[0.3,0.26],[0.38,0.3],[0.46,0.38],[0.55,0.46],[0.62,0.55],[0.64,0.62],[0.71,0.64],[0.77,0.71],[0.82,0.77],[0.87,0.82],[0.93,0.87],[0.98,0.93]]
Y = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[1],[1],[0],[0],[0],[0],[0],[0],[0],[1],[1],[0],[0],[0],[0],[1],[1],[1],[0],[0],[0],[0],[0],[0],[1],[1],[1],[0],[0],[0],[1],[1],[1],[1],[0],[0],[0],[0],[0],[1],[1],[1],[1],[0],[0],[1],[1],[1],[1],[1],[0],[0],[0],[0],[1],[1],[1],[1],[1],[0],[1],[1],[1],[1],[1],[1],[0],[0],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[0],[0],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[0],[1],[1],[1],[1],[1],[1],[1],[0],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[0],[0],[1],[1],[1],[1],[1],[1],[0],[1],[1],[1],[1],[1],[1],[0],[0],[0],[1],[1],[1],[1],[1],[0],[0],[1],[1],[1],[1],[1],[0],[0],[0],[0],[1],[1],[1],[1],[0],[0],[0],[1],[1],[1],[1],[0],[0],[0],[0],[0],[1],[1],[1],[0],[0],[0],[0],[1],[1],[1],[0],[0],[0],[0],[0],[0],[1],[1],[0],[0],[0],[0],[0],[1],[1],[0],[0],[0],[0],[0],[0],[0],[1],[0],[0],[0],[0],[0],[0],[1],[0],[0],[0],[0],[0],[0],[0],[0]]

# Graph definition
with tf.Graph().as_default():
    # Building a network with 2 optimizers
    g = tflearn.input_data(shape=[None, 2])
    # XOR operator definition
    #g = tflearn.fully_connected(g, 64 ,activation='sigmoid')
    g = tflearn.fully_connected(g, 32 ,activation='tanh')
    g = tflearn.fully_connected(g, 1, activation='tanh')
    g = tflearn.regression(g, optimizer='adam', 
                            loss='binary_crossentropy'
                            ,learning_rate=0.01)

    # Training
    m = tflearn.DNN(g)
    m.fit(X, Y, n_epoch=1000)

    # Testing
    print("Testing XOR operator")
    print("0.02 xor 0.02:", m.predict([[0.02, 0.02]]))
    print("0.03 xor 0.03:", m.predict([[0.03, 0.03]]))
    print("0.05 xor 0.05:", m.predict([[0.05, 0.05]]))
    print("0.06 xor 0.06:", m.predict([[0.06, 0.06]]))
    print("0.08 xor 0.08:", m.predict([[0.08, 0.08]]))
    print("0.1 xor 0.1:"  , m.predict([[0.1, 0.1]]))
    print("0.11 xor 0.11:", m.predict([[0.11, 0.11]]))
    print("0.13 xor 0.13:", m.predict([[0.13, 0.13]]))
    print("0.16 xor 0.16:", m.predict([[0.16, 0.16]]))
    print("0.17 xor 0.17:", m.predict([[0.17, 0.17]]))
    print("0.21 xor 0.21:", m.predict([[0.21, 0.21]]))
    print("0.24 xor 0.24:", m.predict([[0.24, 0.24]]))
    print("0.25 xor 0.25:", m.predict([[0.25, 0.25]]))
    print("0.27 xor 0.27:", m.predict([[0.27, 0.27]]))
    print("0.29 xor 0.29:", m.predict([[0.29, 0.29]]))
    print("0.31 xor 0.31:", m.predict([[0.31, 0.31]]))
    print("0.33 xor 0.33:", m.predict([[0.33, 0.33]]))
    print("0.35 xor 0.35:", m.predict([[0.35, 0.35]]))
    print("0.37 xor 0.37:", m.predict([[0.37, 0.37]]))
    print("0.39 xor 0.39:", m.predict([[0.39, 0.21]]))
    print("0.4 xor 0.4:"  , m.predict([[0.4, 0.4]]))
    print("0.42 xor 0.42:", m.predict([[0.42, 0.42]]))
    print("0.43 xor 0.43:", m.predict([[0.43, 0.43]]))
    print("0.45 xor 0.45:", m.predict([[0.45, 0.45]]))
    print("0.48 xor 0.48:", m.predict([[0.48, 0.48]]))
    print("0.51 xor 0.51:", m.predict([[0.51, 0.51]]))
    print("0.53 xor 0.53:", m.predict([[0.53, 0.53]]))
    print("0.54 xor 0.54:", m.predict([[0.54, 0.54]]))
    print("0.57 xor 0.57:", m.predict([[0.57, 0.57]]))
    print("0.58 xor 0.58:", m.predict([[0.58, 0.58]]))
    print("0.61 xor 0.61:", m.predict([[0.61, 0.61]]))
    print("0.63 xor 0.63:", m.predict([[0.63, 0.63]]))
    print("0.65 xor 0.65:", m.predict([[0.65, 0.65]]))
    print("0.66 xor 0.66:", m.predict([[0.66, 0.66]]))
    print("0.68 xor 0.68:", m.predict([[0.68, 0.68]]))
    print("0.7 xor 0.7:", m.predict([[0.7, 0.7]]))
    print("0.72 xor 0.72:", m.predict([[0.72, 0.72]]))
    print("0.74 xor 0.74:", m.predict([[0.74, 0.74]]))
    print("0.76 xor 0.76:", m.predict([[0.76, 0.76]]))
    print("0.78 xor 0.78:", m.predict([[0.78, 0.78]])) 
    print("0.81 xor 0.81:", m.predict([[0.81, 0.81]]))
    print("0.83 xor 0.83:", m.predict([[0.83, 0.83]]))
    print("0.84 xor 0.84:", m.predict([[0.84, 0.84]]))
    print("0.86 xor 0.86:", m.predict([[0.86, 0.86]]))                                           
    print("0.88 xor 0.88:", m.predict([[0.88, 0.88]]))
    print("0.92 xor 0.92:", m.predict([[0.92, 0.92]]))
    print("0.94 xor 0.94:", m.predict([[0.94, 0.94]]))
    print("0.96 xor 0.96:", m.predict([[0.96, 0.96]]))
    print("0.97 xor 0.97:", m.predict([[0.97, 0.97]]))
    print("0.99 xor 0.99:", m.predict([[0.99, 0.99]]))
    print("0.02 xor 0.03:", m.predict([[0.02, 0.03]]))
    print("0.03 xor 0.05:", m.predict([[0.03, 0.05]]))
    print("0.05 xor 0.06:", m.predict([[0.05, 0.06]]))
    print("0.06 xor 0.08:", m.predict([[0.06, 0.08]]))
    print("0.08 xor 0.1:", m.predict([[0.08, 0.1]]))
    print("0.1 xor 0.11:", m.predict([[0.1, 0.11]]))
    print("0.11 xor 0.13:", m.predict([[0.11, 0.13]]))
    print("0.13 xor 0.16:", m.predict([[0.13, 0.16]]))
    print("0.16 xor 0.17:", m.predict([[0.16, 0.17]]))
    print("0.17 xor 0.21:", m.predict([[0.17, 0.21]]))
    print("0.21 xor 0.24:", m.predict([[0.21, 0.24]]))
    print("0.24 xor 0.25:", m.predict([[0.24, 0.25]]))
    print("0.25 xor 0.27:", m.predict([[0.25, 0.27]]))
    print("0.27 xor 0.29:", m.predict([[0.27, 0.28]]))
    print("0.29 xor 0.31:", m.predict([[0.29, 0.31]]))
    print("0.31 xor 0.33:", m.predict([[0.31, 0.33]]))
    print("0.33 xor 0.35:", m.predict([[0.33, 0.35]]))
    print("0.35 xor 0.37:", m.predict([[0.35, 0.37]]))
    print("0.37 xor 0.39:", m.predict([[0.37, 0.39]]))
    print("0.39 xor 0.4:", m.predict([[0.39, 0.4]]))
    print("0.4 xor 0.42:", m.predict([[0.4, 0.42]]))
    print("0.42 xor 0.43:", m.predict([[0.42, 0.43]]))
    print("0.43 xor 0.45:", m.predict([[0.43, 0.45]]))
    print("0.45 xor 0.48:", m.predict([[0.45, 0.48]]))
    print("0.48 xor 0.51:", m.predict([[0.48, 0.51]]))
    print("0.51 xor 0.45:", m.predict([[0.51, 0.45]]))
    print("0.53 xor 0.48:", m.predict([[0.53, 0.48]]))
    print("0.54 xor 0.43:", m.predict([[0.54, 0.43]]))
    print("0.57 xor 0.42:", m.predict([[0.57, 0.42]]))
    print("0.58 xor 0.4:", m.predict([[0.58, 0.4]]))
    print("0.61 xor 0.39:", m.predict([[0.61, 0.39]]))
    print("0.63 xor 0.37:", m.predict([[0.63, 0.37]]))
    print("0.65 xor 0.35:", m.predict([[0.65, 0.35]]))
    print("0.66 xor 0.33:", m.predict([[0.66, 0.33]]))
    print("0.68 xor 0.31:", m.predict([[0.68, 0.31]]))
    print("0.7 xor 0.29:", m.predict([[0.7, 0.29]]))
    print("0.72 xor 0.27:", m.predict([[0.72, 0.27]]))
    print("0.74 xor 0.25:", m.predict([[0.74, 0.25]]))
    print("0.76 xor 0.24:", m.predict([[0.76, 0.24]]))
    print("0.78 xor 0.21:", m.predict([[0.78, 0.21]])) 
    print("0.81 xor 0.17:", m.predict([[0.81, 0.17]]))
    print("0.83 xor 0.16:", m.predict([[0.83, 0.16]]))
    print("0.84 xor 0.13:", m.predict([[0.84, 0.13]]))
    print("0.86 xor 0.11:", m.predict([[0.86, 0.11]]))
    print("0.88 xor 0.1:", m.predict([[0.88, 0.1]]))
    print("0.92 xor 0.08:", m.predict([[0.92, 0.08]]))
    print("0.94 xor 0.06:", m.predict([[0.94, 0.06]]))
    print("0.96 xor 0.05:", m.predict([[0.96, 0.05]]))
    print("0.97 xor 0.03:", m.predict([[0.97, 0.03]]))
    print("0.99 xor 0.02:", m.predict([[0.99, 0.02]]))

    print("Finish!")