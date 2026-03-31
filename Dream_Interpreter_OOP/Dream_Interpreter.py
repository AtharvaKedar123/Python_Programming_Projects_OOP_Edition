import random


class Symbol:
    def __init__(self, name):
        self.name = name
        self.meanings = []

    def add_meaning(self, meaning, emotion_weight):
        self.meanings.append((meaning, emotion_weight))

    def interpret(self, emotion):
        if not self.meanings:
            return "Unknown meaning"

        weighted = []
        for meaning, weight in self.meanings:
            score = weight * emotion
            weighted.append((meaning, score))

        weighted.sort(key=lambda x: x[1], reverse=True)
        return weighted[0][0]


class Dream:
    def __init__(self, text, emotion):
        self.text = text.lower()
        self.emotion = emotion
        self.symbols = []

    def extract_symbols(self, symbol_registry):
        words = self.text.split()
        for word in words:
            if word in symbol_registry:
                self.symbols.append(symbol_registry[word])


class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule_func):
        self.rules.append(rule_func)

    def apply_rules(self, interpretations):
        for rule in self.rules:
            interpretations = rule(interpretations)
        return interpretations


class Interpreter:
    def __init__(self, symbol_registry, rule_engine):
        self.symbol_registry = symbol_registry
        self.rule_engine = rule_engine

    def interpret(self, dream):
        dream.extract_symbols(self.symbol_registry)

        interpretations = []
        for symbol in dream.symbols:
            meaning = symbol.interpret(dream.emotion)
            interpretations.append((symbol.name, meaning))

        interpretations = self.rule_engine.apply_rules(interpretations)
        return interpretations


def fear_rule(interpretations):
    modified = []
    for symbol, meaning in interpretations:
        if "fear" in meaning:
            modified.append((symbol, meaning + " (intensified)"))
        else:
            modified.append((symbol, meaning))
    return modified


def conflict_rule(interpretations):
    names = [s for s, _ in interpretations]
    if "water" in names and "fire" in names:
        interpretations.append(("conflict", "inner conflict detected"))
    return interpretations


if __name__ == "__main__":
    symbol_registry = {}

    snake = Symbol("snake")
    snake.add_meaning("hidden fear", 0.9)
    snake.add_meaning("transformation", 0.5)

    water = Symbol("water")
    water.add_meaning("calmness", 0.3)
    water.add_meaning("emotional depth", 0.8)

    fire = Symbol("fire")
    fire.add_meaning("anger", 0.7)
    fire.add_meaning("passion", 0.6)

    symbol_registry["snake"] = snake
    symbol_registry["water"] = water
    symbol_registry["fire"] = fire

    rule_engine = RuleEngine()
    rule_engine.add_rule(fear_rule)
    rule_engine.add_rule(conflict_rule)

    interpreter = Interpreter(symbol_registry, rule_engine)

    dream_text = "I saw a snake and fire in water"
    emotion_level = random.uniform(0.5, 1.5)

    dream = Dream(dream_text, emotion_level)

    result = interpreter.interpret(dream)

    print("\nDream Interpretation:")
    for symbol, meaning in result:
        print(f"{symbol} -> {meaning}")