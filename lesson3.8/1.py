class Robot:
	__counter = 0

	def __init__(self, name=None, age=0, **kwargs) -> None:
		self.name = name
		self.age = age
		# for key, value in kwargs.items():
		# 	self.__setattr__(key, value)

		Robot.__counter += 1
		print('Robot was created')
	
	def __str__(self):
		return self.attr_name

	def __del__(self):
		Robot.__counter -= 1
		print("Robot was deleted")
	
	def __setattr__(self, name: str, value):
		name = "".join(['attr_', name])
		self.__dict__[name] = value

	def __getattr__(self, name):
		print(f"Sorry, {self} has no {name}")

	def __getattribute__(self, name):
		return super().__getattribute__(name)

	def __len__(self):
		return self.attr_age
	
	def get_robots_count():
		return Robot.__counter

r2d2 = Robot(name="R2 D2", age=10)
c3po = Robot(name="C3PO", age=20)

# r2d2.var = 10
# setattr(r2d2, 'var', 10)
# r2d2.var

# Robot._Robot__counter += 100
# Robot.__counter += 100

# del(r2d2)

print(Robot.get_robots_count())
print(len(c3po))
print(r2d2.attr_age)
print(r2d2.age)