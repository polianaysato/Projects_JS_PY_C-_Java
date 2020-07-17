import random

class Pokemon:
    def __init__(self, name, type_, level = 5):
        """
        Parameters: string name, string type_ and integer level
        Description: constructor method of the Pokemon Class. The level parameter if not passed, it'll be set with the default value of 5.
                     Both max_health and health values are based on the level parameter. The boolean knocked_out parameter is set with an initial value of False.
        Return: None
        """
        self.name = name
        self.level = level
        self.type_ = type_
        self.max_health = level * 5
        self.health = level * 5
        self.knocked_out = False

   
    def knock_out(self):
        """
        Parameters: None
        Description: method used for zeroing the pokemon's health attribute. It also sets the knocked_out boolean attribute to True.
        Return: None
        """
        self.knocked_out = True
        if self.health != 0:
            self.health = 0
            print("'{}' has been knocked out!".format(self.name))
    
    def lose_health(self, qty):
        """
        Parameters: integer quantity
        Description: This method is used by the attack() method for decreasing a pokemon's health attribute. It also verifies if the pokemon's health reached 0, when calls the knock_out method for setting knocked_out attribute to True.
        Return: health attribute value
        """
        self.health -= qty
        if self.health <= 0:
            self.health = 0
            self.knock_out()
        else:
            print("'{}' now has {} health.".format(self.name, self.health))
            return self.health
    
    def recover(self):
        """
        Parameters: None
        Description: It sets the knocked_out attribute to False and increase the pokemon's health by 1 if it's 0.
        Return: health attribute value
        """
        if self.health == 0:
            self.health += 1
            self.knocked_out = False
            print("'{}' has been energised. Its current health is {}".format(self.name), (self.health))
        return self.health
    
    def gain_health(self, qty):
        """
        Parameters: integer quantity
        Description: This method calls the recover() method to revive a pokemon if it's health attribute is set to 0. 
                     It also increases the health attribute by the amount passed by the user.
        Return: health attribute value
        """
        self.recover()
        self.health += qty
        print("'{}' has been given a boost of {} health.".format(self.name, qty))
        return self.health
    
    def attack(self, another_pokemon):
        """
        Parameters: object of Pokemon Class
        Description: This method is used by the Trainer Class' attack_other_trainer() method. It decreases another pokemon's health attribute, based on the type of each pokemon.
        Return: None
        """
        rules = [
            {'pk1':'Grass', 'pk2': 'Fire', 'damage':self.level / 2},
            {'pk1':'Grass', 'pk2': 'Water', 'damage':self.level * 2},
            {'pk1':'Fire', 'pk2':'Grass', 'damage':self.level * 2},
            {'pk1':'Fire', 'pk2':'Water', 'damage':self.level / 2},
            {'pk1':'Water', 'pk2':'Grass', 'damage':self.level /2},
            {'pk1':'Water', 'pk2':'Fire', 'damage':self.level * 2}
        ]
        damage = 0
        if self.type_ == another_pokemon.type_:
            damage = self.level
            another_pokemon.lose_health(damage)
            self._print_aux(self.name, another_pokemon, damage)
        else:
            for rule in rules:
                if self.type_ == rule['pk1'] and another_pokemon.type_ == rule['pk2']:
                    damage = rule['damage']
                    another_pokemon.lose_health(damage)
                    self._print_aux(self.name, another_pokemon, damage)
    
               
    def _print_aux(self, pokemon, another_pokemon, damage):
        """
        Parameters: 2 objects and 1 integer
        Description: Auxiliary method used to prevent repetition in the code
        Return: None
        """
        print("'{}', '{}', '{}' has attacked '{}', '{}', '{}' which has lost {} health.".format(self.name, self.type_, self.level, another_pokemon.name, another_pokemon.type_, another_pokemon.level, damage))

class Trainer:
    def __init__(self, pokemon_list, name, potions):
        """
        Parameters: a list object of Pokemon Class, string name, integer potions
        Description: constructor method of the Trainer Class. Its boolean active_pokemon attribute is set to 0 by default.
        Return: None
        """
        self.pokemon_list = pokemon_list
        self.name = name
        self.potions = potions
        self.active_pokemon = 0
    
    def heal(self):
        """
        Parameters: None
        Description: This method uses the Pokemon Class' gain_health() method. It increases the pokemon's health attribute by 20.
        Return: None
        """
        if self.potions > 0:
            self.pokemon_list[self.active_pokemon].gain_health(20)
            self.potions -= 1
            print("You're used a potion on '{}'.".format(self.pokemon_list[self.active_pokemon].name))
        else:
            print("You're out of potions.")
    
    def attack_other_trainer(self, other_trainer):
        """
        Parameters: object of Trainer Class
        Description: This method uses a Pokemon Class' method attack(). 
                     It decreases the other's trainer active pokemon's health attribute, based on the level and the type of each pokemon.
        Return: None
        """
        my_pokemon = self.pokemon_list[self.active_pokemon]
            
        other_pokemon = other_trainer.pokemon_list[other_trainer.active_pokemon]

        my_pokemon.attack(other_pokemon)

    def switch_pokemon(self, pokemon_number):
         """
        Parameters: integer pokemon_number
        Description: This method sets the active_pokemon attribute to the number passed by the user.
        Return: None
        """
        if pokemon_number < len(self.pokemon_list) and pokemon_number >= 0:
            self.active_pokemon = pokemon_number
            my_current_pokemon = self.pokemon_list[self.active_pokemon]
            print("Your active pokemon has been switched for '{}'".format(my_current_pokemon.name))
            return my_current_pokemon
        elif pokemon_number == self.active_pokemon:
            print("Your active pokemon is already '{}'".format(self.pokemon_list[pokemon_number].name))
        elif self.pokemon_list[pokemon_number].knocked_out:
            print("'{}' is knocked out, it's not possible to activate it!".format(self.pokemon_list[pokemon_number].name))
        else:
            print("You've given an invalid pokemon number!")



# Instantiating Pokemon Class' objects
Charmander = Pokemon("Charmander", "Fire")
Squirtle = Pokemon("Squirtle", "Water")
Bulbasaur = Pokemon("Bulbasaur", "Grass")


team_list = [Charmander, Squirtle, Bulbasaur]
pokemon_team1 = []
pokemon_team2 = []


# Creating Trainer's teams randomly
for x in range(0,6):
    pokemon_team1.append(team_list[random.randint(0, len(team_list)-1)])

for x in range(0,6):
    pokemon_team2.append(team_list[random.randint(0, len(team_list)-1)])


# Assigning Pokemon lists members' levels randomly
range_level = range(1, 19)
range_level = list(range_level)
random.shuffle(range_level)

for pk in range(len(pokemon_team1)):
    pokemon_team1[pk].level = range_level[pk]
    
random.shuffle(range_level)

i = 0
for pk in pokemon_team2:
    pk.level = range_level[i]
    i += 1

# Instatiating Trainer Class objects, by passing Pokemon lists
Trainer1 = Trainer(pokemon_team1, "Poli", 30)
Trainer2 = Trainer(pokemon_team2, "Ana", 18)


Trainer1.attack_other_trainer(Trainer2)
Trainer2.attack_other_trainer(Trainer1)

Trainer1.heal()
Trainer1.switch_pokemon(1)
Trainer2.switch_pokemon(2)

