from AnnotatedTree.Layer.MultiWordLayer import MultiWordLayer


class ShallowParseLayer(MultiWordLayer):

    def __init__(self, layerValue: str):
        """
        Constructor for the shallow parse layer. Sets shallow parse information for each word in
        the node.
        :param layerValue: Layer value for the shallow parse information. Consists of shallow parse information
                       for every word.
        """
        self.layer_name = "shallowParse"
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        """
        Sets the value for the shallow parse layer in a node. Value may consist of multiple shallow parse information
        separated via space character. Each shallow parse value is a string.
        :param layerValue: New layer info
        """
        self.items = []
        self.layer_value = layerValue
        if layerValue is not None:
            split_parse = layerValue.split(" ")
            self.items.extend(split_parse)
