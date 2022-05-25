class MusicKind():
    def __init__(self,celsius):
        self.musicKind = self.musicKind(celsius)
        
    def musicKind(self, celsius):
        musicGenre = ''
        if (celsius >= 30):
            musicGenre += 'Party';
        elif (celsius >= 15 and celsius < 30):
            musicGenre += 'Pop';
        elif (celsius >= 10 and celsius < 15):
            musicGenre += 'Rock';
        else:
            musicGenre += 'Musica Clássica';
        
        return musicGenre
