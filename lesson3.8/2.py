class Robot:
	def __init__(self, name=None, age=0, **kwargs) -> None:
		self.__name = name
		self.__age = age
	
	@property
	def name(self):
		# return self.__name
		return "Luke Skywalker"

	# @name.deleter
	# def asdasdasd(self):
	# 	pass

	@property
	def age(self):
		return self.__age
	
	@age.setter
	def age(self, value):
		if type(value) == int:
			print("Name can not be a integer")
			return
			# raise ValueError("Name can not be a integer")
		if "Hello" in value:
			raise ValueError("Can't set that name")
		else:
			self.__name = value



r2d2 = Robot("R2 D2", age=10)
c3po = Robot("C3PO", age=16)

print(r2d2.name)
r2d2.age = "qweqwe"
print(r2d2.name)
# print(r2d2.name())

print(r2d2.__dict__)