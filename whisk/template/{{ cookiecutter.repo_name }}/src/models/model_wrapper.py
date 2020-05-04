class DummyModel:
    # DELETE ME - Remove this class when you load a real model. This only
    # exists so the ModelWrapper works when creating an initial project.
    """
    A placeholder for a real ML Model. Returns the number of features in each row.

    Example:

        DummyModel().predict([[1,2],[3,4]]) => [2,2]
    """
    def predict(self,X):
        return list(map(lambda instance: len(instance), X))

class ModelWrapper:
    """
    This class should be used to load and invoke the serialized model and any other required
    model artifacts for pre/post-processing.
    """

    def __init__(self):
        """
        Load the model + required pre-processing artifacts from disk. Loading from disk is slow,
        so this is done in `__init__` rather than loading from disk on every call to `predict`.

        Use paths relative to the project root directory.

        Tensorflow example:

            self.model = load_model("models/model.h5")

        Pickle example:

            with open('models/tokenizer.pickle', 'rb') as handle:
                self.tokenizer = pickle.load(handle)
        """
        # REPLACE ME - add your loading logic
        self.model = DummyModel()

    def predict(self,data):
        """
        Returns model predictions.
        """
        # Add any required pre/post-processing steps here.
        return self.model.predict(data)
