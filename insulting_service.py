import random


class InsultingService:

    def __init__(self):
        self.insults_set = set()
        self.insults_severity = dict()

    def add_insult(self, insult, severity):
        print('Insult received: ' + insult)
        self.insults_set.add(insult)
        self.insults_severity[insult] = severity
        return 'Done'

    def get_insults(self):
        return list(self.insults_set)

    def insult_me(self):
        chosen_insult = list(self.insults_set)[random.randrange(0, len(self.insults_set))]
        print('Insult requested. Chose ' + chosen_insult)
        return chosen_insult

    def get_severity(self, insult):
        return self.insults_severity[insult]


insulting_service = InsultingService()
