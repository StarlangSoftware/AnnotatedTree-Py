from AnnotatedTree.Layer.MultiWordLayer import MultiWordLayer


class TurkishSemanticLayer(MultiWordLayer):

    def __init__(self, layerValue: str):
        """
        Constructor for the Turkish semantic layer. Sets semantic information for each word in
        the node.
        :param layerValue: Layer value for the Turkish semantic information. Consists of semantic (Turkish synset id)
                       information for every word.
        """
        self.layer_name = "semantics"
        self.setLayerValue(layerValue)

    def setLayerValue(self, layerValue: str):
        """
        Sets the value for the Turkish semantic layer in a node. Value may consist of multiple sense information
        separated via '$' character. Each sense value is a string representing the synset id of the sense.
        :param layerValue: New layer info
        """
        self.items = []
        self.layer_value = layerValue
        if layerValue is not None:
            split_meanings = layerValue.split("\\$")
            self.items.extend(split_meanings)
