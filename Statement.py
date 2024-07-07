class Statement:
    def __init__(self, sentence, topic, name, responsibility_dimension, pillar, robust_eval, diverse_eval, rationale):
        self.sentence = sentence  # string
        self.topic = topic  # int
        self.name = name
        self.responsibility_dimension = responsibility_dimension  # string
        self.robust_eval = robust_eval  # int
        self.pillar = pillar
        self.diverse_eval = diverse_eval  # int
        self.rationale = rationale  # string
