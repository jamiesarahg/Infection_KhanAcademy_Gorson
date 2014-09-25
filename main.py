#Khan Academy Infection Problem

class User:
	def __init__(self, username):
		self.username = username
		self.infected = False
		self.coaches = []
		self.students = []
		population[self] = 1
	
	def infectSelf(self):
		#infects this user 
		self.infected = True
		population[self]-=1
		for coach in self.coaches:
			population[coach]-=1
	def assignCoach(self, user):
		#assigns the input user as its coach and self as a student of the input user
		self.coaches.append(user)
		user.students.append(self)
		population[self]+=1
	def assignStudents(self,user):
		# assigns the input user as a student and self as a coach of the input user
		self.students.append(user)
		user.coaches.append(self)
		population[user]+=1
	def printStudents(self):
		# prints a list of the usernames of this user's students
		out = []
		for items in self.students:
			out.append(items.username)
		print self.username,' has these students: ',out
	def printCoaches(self):
		# prints a list of the usernames of this user's coaches
		out = []
		for items in self.coaches:
			out.append(items.username)
		print self.username,' has these coaches: ',out



def total_infection(user):
	# infects all users that are related to the input user through coaching and student relationships to any degree
	user.infectSelf()
	for coach in user.coaches:
		spread_infection(user, coach)
	for student in user.students:
		spread_infection(user, student)
	
def spread_infection(userfrom, userto):
	#recursive function of total infection
	userto.infectSelf()
	for coach in userto.coaches:
		if coach != userfrom:
			spread_infection(userto,coach)
	for student in userto.students:
		if student != userfrom:
			spread_infection(userto, student)


# def limited_infection(user, number):
# 	spread_limited_infection(user)

# def spread_limited_infection(user):
# 	for student in user.students:
# 		student.infectSelf()

if __name__ == "__main__":
	global population
	population = {}
	userA = User('userA')
	userB = User('userB')
	userC = User('userC')
	userA.assignStudents(userB)
	userB.assignStudents(userC)

	total_infection(userA)
	print population, 'population'
	print userA.infected, 'userA'
	print userB.infected, 'userB'
	print userC.infected, 'userC'
	userA.printStudents()



