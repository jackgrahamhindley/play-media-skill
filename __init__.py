from mycroft import MycroftSkill, intent_file_handler


class PlayMedia(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('media.play.intent')
    def handle_media_play(self, message):
        self.speak_dialog('media.play')


def create_skill():
    return PlayMedia()

