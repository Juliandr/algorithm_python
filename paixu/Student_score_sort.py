class Student(object):
	"""docstring for Student"""
	def __init__(self, name, age, score):
		self.name = name
		self.age = name
		self.score = score

	def __str__(self):
		return f'{self.name} {self.age} {self.score}'

	def __lt__(self, std):
		if self.score == std.score:
			if self.name == std.name:
				return self.age < std.age
			else:
				return self.name < std.name

		else:
			return self.score < std.score

students = []
n = int(input())
for _ in range(n):
	s_input = input()
	s_list = s_input.split(' ')
	current_student = Student(s_list[0], int(s_list[1]), int(s_list[2]))
	inserted = False
	for index, student in enumerate(students):
		if current_student < student:
			students.insert(index, current_student)
			inserted = True
			break
	if not inserted:
		students.append(current_student)
for student in students:
	print(student)

