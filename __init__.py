from mycroft import MycroftSkill, intent_file_handler


class FerienRechner(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('rechner.ferien.intent')
    def handle_rechner_ferien(self, message):
         = ''

        self.speak_dialog('rechner.ferien', data={
            '': 
        })


def create_skill():
    return FerienRechner()

