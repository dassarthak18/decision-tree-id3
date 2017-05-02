from id3 import Id3Estimator
from id3.data.load_data import load_data
from id3.export import export_graphviz
from sklearn.datasets import load_breast_cancer
import resource
import time
rsrc = resource.RLIMIT_DATA
soft, hard = resource.getrlimit(rsrc)


def run():
    bunch = load_breast_cancer()
    X, y = bunch.data, bunch.target
    id3Estimator = Id3Estimator(prune=True)
    t = time.time()
    id3Estimator.fit(X, y)
    print("Model done: {}".format(time.time() - t))
    export_graphviz(id3Estimator.tree_, "test.dot", feature_names=bunch.feature_names)
    print(len(id3Estimator.tree_.classification_nodes))
    print(len(id3Estimator.tree_.classification_nodes) + len(id3Estimator.tree_.feature_nodes))
    id3Estimator.predict(X)


if __name__ == '__main__':
    run()