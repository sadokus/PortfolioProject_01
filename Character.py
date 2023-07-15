import time
class player_class:
	
	def __init__(self, name, health, damage, gold):
		self.name = name
		self.health = health
		self.start_health = health
		self.damage = damage
		self.gold = gold
		self.is_alive = True


	def __repr__(self):
		retw = "Player: " + self.name + "\nHealth: "
		retw += str(self.health)
		retw += "\nGold: "
		retw += str(self.gold)
		return retw

	def take_damage(self, damage, attacker):
		if self.is_alive == False:
			return
		
		print("BATTLE INFO: " + self.name + " has taken damage " + str(damage) + " from [" + str(attacker.name) + "]")
		if self.health - damage > 0:
			self.health -= damage
		elif self.health - damage <= 0:
			print( "\n"+ self.name + " died to " + str(attacker) + "!")
			self.is_alive = False
		print(f'Player HP: {self.start_health} / {self.health}\n')

class enemy_class:
	
	def __init__(self, name = "Bandit", health = 10, damage = 1, gold_amount = 2):
		self.name = name
		self.damage = damage
		self.start_health = health
		self.health = health
		self.gold_amount = gold_amount
		self.is_alive = True

	def take_damage(self, damage, attacker):
		if self.health - damage > 0:
			self.health -= damage
			print("BATTLE INFO: " + self.name + " has taken damage!")
		elif self.health - damage <= 0:
			#self.health = 0
			self.health -= damage
			print(attacker.name + " defeated " + self.name + "!\nReward: " + str(self.gold_amount) + " gold!")
			attacker.gold += self.gold_amount
			time.sleep(1)
			self.is_alive = False
		#print(f'Enemy HP: {self.start_health} / {self.health}')

	def __repr__(self):
		return "Enemy: " + self.name + "--- HP: " + str(self.start_health) + "/" + str(self.health)

