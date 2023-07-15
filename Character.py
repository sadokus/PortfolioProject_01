class player_class:
	
	def __init__(self, name, health, damage, gold):
		self.name = name
		self.health = health
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
		print(self.name + " has taken damage " + str(damage))
		if self.health - damage > 0:
			self.health -= damage
		elif self.health - damage <= 0:
			print(self.name + " died to " + str(attacker) + "!")
			self.is_alive = False

class enemy_class:
	
	def __init__(self, name = "Bandit", health = 10, damage = 1, gold_amount = 2):
		self.name = name
		self.damage = damage
		self.health = health
		self.gold_amount = gold_amount

	def take_damage(self, damage, attacker):
		if self.health - damage > 0:
			print(self.name + " has taken damage!")
		elif self.health - damage <= 0:
			print(attacker + " defeated " + self.name + "!\nReward: " + str(self.gold_amount) + " gold!")

	def __repr__(self):
		return "Enemy: " + self.name + "\nGold Amount: " + str(self.gold_amount)

