from {{cookiecutter.project_name}} import artifacts_dir
import pickle


class Model:
    """
    This class should be used to load and invoke the serialized model and
    any other required model artifacts for pre/post-processing.
    """

    def __init__(self):
        """
        Load the model + required pre-processing artifacts from disk.
        Loading from disk is slow, so this is done in `__init__` rather than
        loading from disk on every call to `predict`.

        Tensorflow example:

            self.model = load_model(whisk.artifacts_dir / "model.h5")

        Pickle example:

            with open(whisk.artifacts_dir / 'tokenizer.pickle', 'rb') as file:
                self.tokenizer = pickle.load(file)
        """
        # REPLACE ME - add your loading logic
        with open(artifacts_dir / "model.pkl", 'rb') as file:
            self.model = pickle.load(file)

    def predict(self,data):
        """
        Returns model predictions.
        """
        # Add any required pre/post-processing steps here.
        return self.model.predict(data)
