class Mediaplayer:

    def open_file(self, file):
        self.filename = file

    def play(self):
        print(f"Воспроизведение {self.filename}")


media1 = Mediaplayer()
media2 = Mediaplayer()

media1.open_file('filemedia1')
media2.open_file('filemedia2')

media1.play()
media2.play()
