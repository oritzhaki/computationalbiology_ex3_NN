import numpy as np
from buildnet0 import NN, Weight, sigmoid, relu


def load_data(filename):
    """
    Load test data to check model's accuracy
    """
    f = open(filename, 'r')
    lines = f.readlines()

    test = []
    for line in lines:
        string = line.strip()
        # Converting the input string into a list of integers
        test.append([int(bit) for bit in string])

    return np.array(test)


def get_weights_for_model(W1, W2, W3):
    temp1 = Weight(1, 1, activation=lambda x: relu(x))
    temp2 = Weight(1, 1, activation=lambda x: relu(x))
    temp3 = Weight(1, 1, activation=lambda x: sigmoid(x))
    temp1.update_weights(W1)
    temp2.update_weights(W2)
    temp3.update_weights(W3)
    return temp1, temp2, temp3


def initiate_best_model(filename):
    weights = np.load(filename)
    W1 = weights['arr1']
    W2 = weights['arr2']
    W3 = weights['arr3']

    weights1, weights2, weights3 = get_weights_for_model(W1, W2, W3)

    return NN(weights1, weights2, weights3)


def write_predictions_to_file(filename):
    results = open(filename, "w")
    for label in predictions:
        results.write(str(label) + "\n")

    results.close()


if __name__ == "__main__":
    # Load data from test file
    X_test = load_data("testnet0.txt")

    # Create best model according to best model received from GA
    BEST_MODEL = initiate_best_model("wnet0.npz")

    # Test data on best model
    predictions = BEST_MODEL.predict(X_test)

    # Write predictions to results file
    write_predictions_to_file("result0.txt")
