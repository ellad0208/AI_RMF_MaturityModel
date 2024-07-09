"""Defines the topic class."""
class Topic:
    def __init__(self, rationale, evaluation, sentence, stage, statements, name):
        self.rationale = rationale  # string
        self.evaluation = evaluation  # int (1-5)
        self.sentence = sentence  # string
        self.stage = stage  # int
        self.statements = statements  # list of Statement objects
        self.name = name
        self.pillars_list = []
        self.dimensions_list = []