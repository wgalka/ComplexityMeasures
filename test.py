import pickle


def test():
    from examples.corelationMatrix import corrMatrix
    return corrMatrix

# Zapisanie macierzy korelacji do pliku
# pickle.dump(test(), open(b"corrMatrix.obj", "wb"))
