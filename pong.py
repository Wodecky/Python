#pong
#pong

from livewires import games, color
from math import sqrt

games.init(screen_width = 1366, screen_height = 768, fps = 60)

class Deska(games.Sprite):

    image = games.load_image("deska.bmp", transparent = False)
    def __init__(self):
        """ Initialize Pan object and create Text object for score. """
        super(Deska, self).__init__(x = games.mouse.x, bottom = games.screen.height, image = Deska.image)

        self.score = games.Text(value=0, size=25, color=color.black,
                                top=5, right=games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        """ Zmień pozycję na wyznaczoną przez współrzędną x myszy. """
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()

    def check_catch(self):
        """ Sprawdź, czy nie zostały złapane jakieś pizze. """
        for ball in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            ball.ball_hit(self.x)

class Ball(games.Sprite):
    """
    Pizza, która spada na ziemię.
    """
    image = games.load_image("pizza.bmp")
    speed = 4.0

    def __init__(self):
        """ Inicjalizuj obiekt klasy Pizza. """
        super(Ball, self).__init__(image = Ball.image,
                                   x = games.screen.width/2, y = games.screen.height/2,
                                   dy = Ball.speed)

    def update(self):
        """ Sprawdź, czy dolny brzeg pizzy dosięgnął dołu ekranu. """
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

        if self.top <= 0:
            self.dy *= -1

        if self.left <= 0 or self.right >= games.screen.width:
            self.dx *= -1



    def ball_hit(self, x):
        if abs(x-self.x) <= 50:
            self.dx = Ball.speed * (self.x-x)/51
            self.dy = -sqrt(Ball.speed**2 - self.dx**2)


    def end_game(self):
        """ Zakończ grę. """
        end_message = games.Message(value = "Koniec gry",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.height/2,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)

def main():
    """ Uruchom grę. """
    wall_image = games.load_image("sciana.jpg", transparent = False)
    games.screen.background = wall_image

    ball = Ball()
    games.screen.add(ball)

    the_pan = Deska()
    games.screen.add(the_pan)

    games.mouse.is_visible = False

    games.screen.event_grab = True
    games.screen.mainloop()

# wystartuj!
main()
