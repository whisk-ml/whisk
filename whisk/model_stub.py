class ModelStub:
    # DELETE ME - Remove this class when you load a real model. This only
    # exists so the ModelWrapper works when creating an initial project.
    """
    A placeholder for a real ML Model. Returns the number of features in each row.

    Example:

        ModelStub().predict([[1,2],[3,4]]) => [2,2]
    """
    def predict(self,X):
        return list(map(lambda instance: len(instance), X))
