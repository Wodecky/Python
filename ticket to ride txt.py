# ticket to ride txt

# text version of board game.

import random
import collections


class Game(object):
    P_COLOURS = ["black", "blue", "green", "red", "yellow"]
    C_COLOURS = ["black", "blue", "green", "orange", "pink", "red", "white", "yellow"]

    POINTS_TABLE = {1: 1,
                    2: 2,
                    3: 4,
                    4: 7,
                    6: 15,
                    8: 21}

    E_ROUTES = [(("Amsterdam", "Bruxelles"), "black", 0, 1),        (("Amsterdam", "Essen"), "yellow", 0, 3),
                (("Amsterdam", "Frankfurt"), "white", 0, 2),        (("Amsterdam", "London"), "grey", 2, 0),
                (("Angora", "Constantinople"), "grey", 3, 2),       (("Angora", "Erzurum"), "black", 0, 3),
                (("Angora", "Smyrna"), "orange", 3, 3),             (("Athina", "Brindisi"), "grey", 1, 3),
                (("Athina", "Sarajevo"), "green", 0, 4),            (("Athina", "Sofia"), "pink", 0, 3),
                (("Athina", "Smyrna"), "grey", 1, 1),               (("Barcelona", "Madrid"), "yellow", 0, 2),
                (("Barcelona", "Marseille"), "grey", 0, 4),         (("Barcelona", "Pamplona"), "grey", 0, 2),
                (("Berlin", "Danzig"), "grey", 0, 4),               (("Berlin", "Essen"), "blue", 0, 2),
                (("Berlin", "Frankfurt"), "black", 0, 3),           (("Berlin", "Frankfurt"), "red", 0, 3),
                (("Berlin", "Warszawa"), "pink", 0, 4),             (("Berlin", "Warszawa"), "yellow", 0, 4),
                (("Berlin", "Wien"), "green", 0, 3),                (("Brest", "Dieppe"), "orange", 0, 2),
                (("Brest", "Pamplona"), "pink", 0, 4),              (("Brest", "Paris"), "black", 0, 3),
                (("Brindisi", "Palermo"), "grey", 1, 2),            (("Brindisi", "Roma"), "white", 0, 2),
                (("Bruxelles", "Dieppe"), "green", 0, 2),           (("Bruxelles", "Frankfurt"), "blue", 0, 2),
                (("Bruxelles", "Paris"), "yellow", 0, 2),           (("Bruxelles", "Paris"), "red", 0, 2),
                (("Bucuresti", "Budapest"), "grey", 3, 4),          (("Bucuresti", "Constantinople"), "yellow", 0, 3),
                (("Bucuresti", "Kyiv"), "grey", 0, 4),              (("Bucuresti", "Sevastopol"), "white", 0, 4),
                (("Bucuresti", "Sofia"), "grey", 3, 2),             (("Budapest", "Kyiv"), "grey", 3, 6),
                (("Budapest", "Sarajevo"), "pink", 0, 3),           (("Budapest", "Wien"), "red", 0, 1),
                (("Budapest", "Wien"), "white", 0, 1),              (("Budapest", "Zagrab"), "orange", 0, 2),
                (("Cadiz", "Lisboa"), "blue", 0, 2),                (("Cadiz", "Madrid"), "orange", 0, 3),
                (("Constantinople", "Sevastopol"), "Grey", 2, 2),   (("Constantinople", "Sofia"), "Blue", 0, 3),
                (("Constantinople", "Smyrna"), "Grey", 3, 2),       (("Danzig", "Riga"), "black", 0, 3),
                (("Danzig", "Warszawa"), "grey", 0, 2),             (("Dieppe", "London"), "grey", 1, 1),
                (("Dieppe", "London"), "grey", 1, 1),               (("Dieppe", "Paris"), "pink", 0, 1),
                (("Edinburgh", "London"), "orange", 0, 4),          (("Edinburgh", "London"), "black", 0, 4),
                (("Erzurum", "Sevastopol"), "grey", 2, 2),          (("Erzurum", "Sochi"), "red", 3, 3),
                (("Essen", "Frankfurt"), "green", 0, 2),            (("Essen", "Kobenhavn"), "grey", 1, 2),
                (("Essen", "Kobenhavn"), "grey", 1, 2),             (("Frankfurt", "Munchen"), "pink", 0, 2),
                (("Frankfurt", "Paris"), "white", 0, 3),            (("Frankfurt", "Paris"), "orange", 0, 3),
                (("Kharkov", "Kyiv"), "grey", 0, 4),                (("Kharkov", "Moskva"), "grey", 0, 4),
                (("Kharkov", "Rostov"), "green", 0, 2),             (("Kobenhavn", "Stockholm"), "yellow", 0, 3),
                (("Kobenhavn", "Stockholm"), "white", 0, 3),        (("Kyiv", "Smolensk"), "red", 0, 3),
                (("Kyiv", "Warszawa"), "grey", 0, 4),               (("Kyiv", "Wilno"), "grey", 0, 2),
                (("Lisboa", "Madrid"), "pink", 0, 3),               (("Madrid", "Pamplona"), "black", 3, 3),
                (("Madrid", "Pamplona"), "white", 3, 3),            (("Marseille", "Pamplona"), "red", 0, 4),
                (("Marseille", "Paris"), "grey", 0, 4),             (("Marseille", "Roma"), "grey", 3, 4),
                (("Marseille", "Zurich"), "pink", 3, 2),            (("Moskva", "Petrograd"), "white", 0, 4),
                (("Moskva", "Smolensk"), "orange", 0, 2),           (("Munchen", "Venezia"), "blue", 3, 2),
                (("Munchen", "Wien"), "orange", 0, 3),              (("Munchen", "Zurich"), "yellow", 3, 2),
                (("Palermo", "Roma"), "grey", 1, 3),                (("Palermo", "Smyrna"), "grey", 2, 4),
                (("Pamplona", "Paris"), "blue", 0, 4),              (("Pamplona", "Paris"), "green", 0, 4),
                (("Paris", "Zurich"), "grey", 3, 3),                (("Petrograd", "Riga"), "grey", 0, 4),
                (("Petrograd", "Stockholm"), "grey", 3, 8),         (("Petrograd", "Wilno"), "blue", 0, 4),
                (("Riga", "Wilno"), "green", 0, 4),                 (("Roma", "Venezia"), "black", 0, 2),
                (("Rostov", "Sevastopol"), "grey", 0, 4),           (("Rostov", "Sochi"), "grey", 0, 2),
                (("Sarajevo", "Sofia"), "grey", 3, 2),              (("Sarajevo", "Zagrab"), "red", 0, 3),
                (("Sevastopol", "Sochi"), "grey", 1, 1),            (("Smolensk", "Wilno"), "yellow", 0, 3),
                (("Venezia", "Zagrab"), "grey", 0, 2),              (("Venezia", "Zurich"), "green", 3, 2),
                (("Warszawa", "Wien"), "blue", 0, 4),               (("Warszawa", "Wilno"), "red", 0, 3),
                (("Wien", "Zagrab"), "grey", 0, 2)]

    E_STATIONS = sorted(set([x[0][0] for x in E_ROUTES] + [x[0][1] for x in E_ROUTES]))

    E_TICKETS_SHORT = [["Athina", "Angora", 5, False],              ["Budapest", "Sofia", 5, False],
                       ["Frankfurt", "Kobenhavn", 5, False],        ["Rostov", "Erzurum", 5, False],
                       ["Sofia", 'Smyrna', 5, False],               ['Kyiv', 'Petrograd', 6, False],
                       ['Warszawa', 'Smolensk', 6, False],          ['Zagrab', 'Brindisi', 6, False],
                       ['Zurich', 'Brindisi', 6, False],            ['Zurich', 'Budapest', 6, False],
                       ['Amsterdam', 'Pamplona', 7, False],         ['Brest', 'Marseille', 7, False],
                       ['Edinburgh', 'Paris', 7, False],            ['London', 'Berlin', 7, False],
                       ['Paris', 'Zagrab', 7, False],               ['Barcelona', 'Bruxelles', 8, False],
                       ['Barcelona', 'Munchen', 8, False],          ['Berlin', 'Bucuresti', 8, False],
                       ['Brest', 'Venezia', 8, False],              ['Kyiv', 'Sochi', 8, False],
                       ['Madrid', 'Dieppe', 8, False],              ['Madrid', 'Zurich', 8, False],
                       ['Marseille', 'Essen', 8, False],            ['Palermo', 'Constantinople', 8, False],
                       ['Paris', 'Wien', 8, False],                 ['Roma', 'Smyrna', 8, False],
                       ['Sarajevo', 'Sevastopol', 8, False],        ['Smolensk', 'Rostov', 8, False],
                       ['Berlin', 'Roma', 9, False],                ['Bruxelles', 'Danzig', 9, False],
                       ['Angora', 'Kharkov', 10, False],            ['Essen', 'Kyiv', 10, False],
                       ['London', 'Wien', 10, False],               ['Riga', 'Bucuresti', 10, False],
                       ['Venezia', 'Constantinople', 10, False],    ['Athina', 'Wilno', 11, False],
                       ['Stockholm', 'Wien', 11, False],            ['Amsterdam', 'Wilno', 12, False],
                       ['Berlin', 'Moskva', 12, False],             ['Frankfurt', 'Smolensk', 13, False]]

    E_TICKETS_LONG = [['Brest', 'Petrograd', 20, False],
                      ['Cadiz', 'Stockholm', 21, False],
                      ['Edinburgh', 'Athina', 21, False],
                      ['Kobenhavn', 'Erzurum', 21, False],
                      ['Lisboa', 'Danzig', 20, False],
                      ['Palermo', 'Moskva', 20, False]]

    def __init__(self):
        self.players = []
        self.deck = Deck()
        self.deck.populate()
        self.end = 0
        self.longest = 0
        self.routes = Game.E_ROUTES
        self.stations = Game.E_STATIONS

    def generate_players(self, number):
        available_colours = self.P_COLOURS
        question = "What colour do you choose?"
        for player in range(number):
            answer = ask_question("\n"+str(player+1), question, *available_colours)
            player = Player(answer)
            self.players.append(player)
            available_colours.remove(answer)

    def turn(self):
        for player in self.players:
            if self.end > len(self.players):
                break
            if self.end > 1:
                self.end += 1
                print("This is your last turn")
            player.choose_action(self.deck, self.routes, self.stations)
            if player.last_turn and self.end == 0:
                self.end += 1

    def final_count(self):
        for player in self.players:
            player.longest1()
            if player.lomgest > self.longest:
                self.longest = player.lomgest

        for player in self.players:
            player.points = player.final_count(self.longest)

    def results(self):
        self.players.sort(key=lambda x: x.points, reverse=True)
        print("Results")
        for player in self.players:
            print('{}: {} {}pts'.format(self.players.index(player) + 1, player.colour, player.points))


class Card(object):
    def __init__(self, colour):
        self.colour = colour

    def __str__(self):
        return self.colour


class Deck(object):
    def __init__(self):
        self.cards = []
        self.face_up = []
        self.used = []
        self.short = Game.E_TICKETS_SHORT
        random.shuffle(self.short)
        self.long = Game.E_TICKETS_LONG
        random.shuffle(self.long)

    def face_up_control(self):
        trains = 0
        while len(self.face_up) < 5:
            self.face_up.append(self.cards.pop(0))
            self.repopulate()
            if self.cards is None and self.used is None:
                break
        for card in self.face_up:
            if card.colour == "train":
                trains += 1
        if trains >= 3:
            for i in range(5):
                self.used.append(self.face_up.pop())
            self.face_up_control()

    def give_each(self, players):
        """Gives each player 4 cards and four tickets"""
        for player in players:
            for i in range(4):
                player.cards.append(self.cards.pop(0))
            player.tickets.append(self.long.pop(0))
            for i in range(3):
                player.tickets.append(self.short.pop())

            while len(player.tickets) > 2:
                question = "Which ticket would you like to discard?"
                ticket = ask_question(player.colour, question, *player.tickets + ["none"], form="{} to {} ({})")

                if ticket[2] in [20, 21]:
                    player.tickets.remove(ticket)
                elif ticket == "none":
                    break
                else:
                    self.short.append(player.tickets.pop(player.tickets.index(ticket)))

    def populate(self):
        for colour in Game.C_COLOURS:
            for i in range(12):
                self.cards.append(Card(colour))
        for i in range(14):
            self.cards.append(Card(colour="train"))
        random.shuffle(self.cards)

    def repopulate(self):
        if not self.cards:
            if not self.used:
                print("Deck and discards stacks are empty")
            else:
                self.cards = self.used
                random.shuffle(self.cards)
                self.used = []
                print("Discards have been reshuffled into deck")


class Player(object):
    def __init__(self, colour):
        self.colour = colour
        self.cards = []
        self.cars = 45
        self.last_turn = False
        self.routes = []
        self.points = 0
        self.stations = []
        self.tickets = []
        self.longest = 0

    def __str__(self):
        if self.cards is None:
            return "Hand is empty"
        else:
            rep = ""
            lista = {}
            for card in self.cards:
                if card.colour not in lista:
                    lista[card.colour] = 1
                else:
                    lista[card.colour] += 1

            for key in lista:
                rep += "\n" + key + ": " + str(lista[key])
            return rep

    def available_routes(self, cards, trains, routes):
        """finds routes available for player"""
        available = []
        for route in routes:
            # finds available routes
            if route[2] in [0, 3] and route[3] <= self.cars:
                if route[1] == "grey":
                    if route[3] <= max(cards.values()) + trains:
                        available.append(route)
                elif route[1] in cards:
                    if route[3] <= cards[route[1]] + trains:
                        available.append(route)
            elif route[2] <= trains and route[2] + route[3] < self.cars:
                if route[2] + route[3] <= trains + max(cards.values()):
                    available.append(route)
        return available

    def build_station(self, deck, routes, stations):
        """builds station"""
        question = "Where would you like to build a station?"
        city = ask_question(self.colour, question, *stations + ["Go to previous menu"])

        if city in stations:
            question = "Which route would you like to claim?"
            lines = []
            for route in Game.E_ROUTES:
                if city in route[0]:
                    lines.append(route)
            choice = ask_question(self.colour, question, *lines + ["Go to main decision menu"], form="{} to {}")

            if choice in lines:
                question = "Cards of what colour would you like to use?({})".format(len(self.stations)+1)
                cards, trains = self.num_of_each()
                colours = [x for x in cards.keys() if cards[x] + trains > len(self.stations)]
                colour = ask_question(self.colour, question, *colours + ["Go to main decision menu"], form='{} ({})')

                if colour in colours:
                    self.routes.append(((choice[0][0], choice[0][1]), "Fake"))
                    self.stations.append(stations.pop(stations.index(city)))
                    self.give_cards(colour, len(self.stations), 0, deck)
                else:
                    self.choose_action(deck, routes, stations)

            else:
                self.choose_action(deck, routes, stations)

        else:
            self.choose_action(deck, routes, stations)

    def check_tickets(self):
        for ticket in self.tickets:
            if not ticket[3]:
                self.connected(ticket)

    def choose_action(self, deck, routes, stations):
        """lets player to choose action and runs proper method"""
        question = "What would you like to do"
        actions = []
        cards, trains = self.num_of_each()
        available = self.available_routes(cards, trains, routes)
        # check if player can draw a card
        if deck.face_up:
            actions.append("Draw a card/cards")
        if available:
            actions.append("Claim a route")
        # check if player can build station
        if deck.short:
            actions.append("Draw a destination ticket")
        if len(self.stations) < 3 and max(cards.values()) + trains >= len(self.stations) + 1:
            actions.append("Build railway station")
        print("\n{},\nCards in your hand:".format(self.colour.capitalize()), self)
        print("Cards face up: {}, {}, {}, {}, {}".format(*[card.colour for card in deck.face_up]))
        action = ask_question(self.colour, question, *actions)

        if action == "Draw a card/cards":
            self.draw_card(deck, routes, stations)

        elif action == "Claim a route":
            self.claim(available, deck, routes, stations)

        elif action == "Draw a destination ticket":
            self.draw_ticket(deck)

        elif action == "Build railway station":
            self.build_station(deck, routes, stations)
        else:
            error()

    def connected(self, ticket, start="", used=None):
        """checks if claimed routes connect cities on ticket"""
        if not ticket[3]:
            if not used:
                used = []
            if not start:
                start = ticket[0]
            used.append(ticket[1])
            for route in self.routes:
                if route not in used and start in route[0]:
                    if ticket[1] in route[0]:
                        ticket[3] = True
                        break
                    else:
                        used.append(route)
                        for city in route[0]:
                            self.connected(ticket, city, used)

    def claim(self, available, deck, routes, stations):

        cards, trains = self.num_of_each()
        question = "Below is list of available ordinary lines, ferries and tunnels that you may be able to claim." \
                   " Please choose one:"

        choice = ask_question(self.colour, question, *available + ["Go to previous menu"], form="{} to {}")

        colour_used = ""
        if choice in available:
            # if route is grey asks what colour of cards should be used to claim it
            if choice[1] == "grey":
                question = "What colour_used would you like to use?"
                colours = [x for x in cards.keys() if cards[x] + trains >= choice[3]]
                colour_used = ask_question(self.colour, question, *colours)
            else:
                colour_used = choice[3]

        else:
            # go to previous menu
            self.choose_action(deck, routes, stations)

        if choice[2] == 3:
            # if tunnel pick 3 cards from deck to check length
            x = 0

            for i in range(3):
                if deck.cards:
                    if deck.cards[0].colour in ["train", colour_used]:
                        x += 1
                    deck.used.append(deck.cards.pop(0))
            deck.repopulate()
            print(x)

            if choice[3] + x <= trains + cards[colour_used]:
                question = "Tunnel will take {} additional cards. Are you still willing to claim it?".format(str(x))
                yes_or_no = ["Yes", "No"]
                yes_no = ask_question(self.colour, question, *yes_or_no)
                if yes_no == "Yes":
                    self.successful_claim(choice, colour_used, choice[3] + x, 0, deck, routes)
            else:
                print("Failed to claim tunnel.")

        else:
            self.successful_claim(choice, colour_used, choice[3], choice[2], deck, routes)

    def draw_card(self, deck, routes, stations):
        x = 0
        question = "Which card would you like to draw?"
        while x < 2:
            available = []

            if x == 0:
                for card in deck.face_up:
                    available.append(card)
            elif x == 1:
                for card in deck.face_up:
                    if card.colour != "train":
                        available.append(card)

            if deck.cards:
                available.append("back up card")

            if x == 0:
                available.append("go to previous menu")

            if not available:
                print("There are no more cards.")
                break

            print(available)

            choice = ask_question(self.colour, question, *available)

            if type(choice) is Card:
                self.cards.append(deck.face_up.pop(deck.face_up.index(choice)))
                deck.face_up_control()

                if self.cards[-1].colour == "train":
                    x += 2
                else:
                    x += 1
            elif choice == "back up card":
                print("This card is {}".format(deck.cards[0].colour))
                self.cards.append(deck.cards.pop(0))
                deck.repopulate()
                x += 1
            elif choice == "go to previous menu":
                self.choose_action(deck, routes, stations)
            else:
                error()

    def draw_ticket(self, deck):
        """draws 3 tickets player keeps at least 1"""
        tickets = []
        for i in range(3):
            if deck.short:
                tickets.append(deck.short.pop(0))

        while len(tickets) > 1:
            question = "Which ticket would you like to discard?"
            ticket = ask_question(self.colour, question, *tickets + ["none"], form="{} to {} ({})")

            if ticket in tickets:
                tickets.remove(ticket)
            elif ticket == "none":
                break

        self.tickets.extend(tickets)

    def final_count(self, longest):
        points = self.points + 12 - 4 * len(self.stations)
        for ticket in self.tickets:
            if ticket[3]:
                points += ticket[2]
            else:
                points -= ticket[2]
        if self.longest == longest:
            points += 10
        return points

    def get_points(self, length):
        self.points += Game.POINTS_TABLE[length]
        print("Gained {} point/s. Now you have {}".format(*[Game.POINTS_TABLE[length], self.points]))

    def give_cards(self, colour, amount, trains, deck):
        x = 0
        t = 0
        for card in self.cards:
            if card.colour == colour:
                deck.used.append(self.cards.pop(self.cards.index(card)))
                x += 1
                if x == amount:
                    break

        if trains > 0:
            for card in self.cards:
                if card.colour == "train":
                    deck.used.append(self.cards.pop(self.cards.index(card)))
                    t += 1
                    if amount + trains == x + t:
                        break

        deck.repopulate()

    def longest1(self):
        """searches for stations that may be beginning of the longest route"""
        cities = {}
        for route in self.routes:
            for city in route[0]:
                if city not in cities:
                    cities[city] = 1
                else:
                    cities[city] += 1
        for city in cities:
            a = self.longest2(city)
            if a > self.longest:
                self.longest = a

    def longest2(self, city, used=None):
        c = 0
        a = 0

        if not used:
            used = []
        for route in self.routes:
            if route not in used and city in route[0] and route[1] != "Fake":
                used.append(route)

                for station in route[0]:
                    if station != city:
                        a = self.longest2(city = station, used = used)

                if route[2] == 3:
                    b = route[3]
                else:
                    b = route[2] + route[3]

                if a + b > c:
                    c = a + b
                    print(city, route, a, b, c, used)

        return c

    def num_of_each(self):
        """returns dictionary where keys are colours in hand and values are their numbers and number of trains"""
        cards = {}
        trains = 0
        for card in self.cards:
            if card.colour == "train":
                trains += 1
            elif card.colour not in cards:
                cards[card.colour] = 1
            else:
                cards[card.colour] += 1
        return cards, trains

    def successful_claim(self, route, colour, cars, trains, deck, routes):
        self.routes.append(routes.pop(routes.index(route)))
        print("Tunnel successfully claimed!")
        self.give_cards(colour, cars, trains, deck)
        self.get_points(route[3]+trains)
        self.cars -= trains + route[3]
        if self.cars <= 2:
            self.last_turn = True


def ask_question(reciever, question, *answers, form=None):
    answer = ""
    while answer not in [str(x) for x in range(1, len(answers)+1)]:
        print(reciever.capitalize()+"!")
        print(question)
        if form:
            new_answers = []
            for x in answers:
                if type(x) in [list, tuple]:
                    x = flatten(x)
                    new_answers.append(form.format(*x))
                elif type(x) is str:
                    new_answers.append(x)

            answer = input("\n".join("{} - {}".format(*k) for k in enumerate(new_answers, start=1)))
        if not form:
            answer = input("\n".join("{} - {}".format(*k) for k in enumerate(answers, start=1)))
    return answers[int(answer)-1]


def error():
    print("Something wrong")


def flatten(x):
    for y in x:
        if isinstance(y, collections.Iterable) and not isinstance(y, (bytes, str)):
            yield from flatten(y)
        else:
            yield y


def number_of_players():
    """Asks about number of players"""
    players = 0
    while players not in [str(x) for x in range(2, 6)]:
        players = input("How many players?(2-5)")
    return int(players)


def main():
    game = Game()
    game.generate_players(number_of_players())
    game.deck.give_each(game.players)
    game.deck.face_up_control()
    while True:
        if game.end > len(game.players):
            break
        game.turn()
    game.final_count()
    game.results()

    print("Game over XD")

main()

input("watwat")
