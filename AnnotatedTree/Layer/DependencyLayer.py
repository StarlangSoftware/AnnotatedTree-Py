from AnnotatedTree.Layer.SingleWordLayer import SingleWordLayer


class DependencyLayer(SingleWordLayer):

    def __init__(self, layerValue: str):
        """
        Constructor for the dependency layer. Dependency layer stores the dependency information of a node.
        :param layerValue: Value of the dependency layer.
        """
        self.layer_name = "dependency"
        self.setLayerValue(layerValue)
