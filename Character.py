import time
class player_class:
	
	def __init__(self, name, health, damage, gold):
		self.name = name
		self.health = health
		self.start_health = health
		self.damage = damage
		self.gold = gold
		self.is_alive = True
		self.inventory = {"HP Potion" : 2}


	def __repr__(self):
		retw = "Player: " + self.name + "\nHealth: "
		retw += str(self.health)
		retw += "\nGold: "
		retw += str(self.gold)
		return retw
	
	
	def use_hp_potion(self):
		if self.inventory["HP Potion"] > 0:
			self.inventory["HP Potion"] -= 1
			self.heal(5)
		else:
			print("no more potions")		

	def get_item(self, itemname, itemamount):
		if itemname in self.inventory.keys():
			self.inventory[itemname] += itemamount
			print("inventory amount updated!")
		else:
			self.inventory.update({itemname : itemamount})
			print("new item added!")


	def change_gold(self, goldamount):
		if self.gold + goldamount <= 0:
			self.gold = 0
		self.gold -= goldamount

	def heal(self, heal_amount):
		if self.health + heal_amount >= self.start_health:
			self.health = self.start_health
		else:
			self.health += heal_amount

	def open_inventory(self):
		while True:
			try:
				counted = 1
				for i, v in self.inventory.items():
					print(f"[{counted}]"+ i + f"-- amount: [{v}]")
					counted += 1
					#print(v)

				print("Type [exit] to exit Inventory!")
				plr_input = input("What is your choice\n> ")
				if int(plr_input) == 1:
					#print("SHOULD USE HP???")
					self.use_hp_potion()
			except ValueError:
				if str(plr_input).lower().strip() == "exit":
					break
				continue

			else:
				
				break

			
			

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

