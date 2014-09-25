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
		global count
		count +=1
		print count
		for coach in self.coaches:
			population[coach]-=1
	def assignCoach(self, user):
		#assigns the input user as its coach and self as a student of the input user
		self.coaches.append(user)
		user.students.append(self)
		population[user]+=1

	def assignStudents(self,user):
		# assigns the input user as a student and self as a coach of the input user
		self.students.append(user)
		user.coaches.append(self)
		population[self]+=1
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


def limited_infection(user, number):
	print count
	spread_limited_infection(user)

	while count < number:
		user2 = pick_coach(number)
		while user2 == False:
			number -= 1
			user2 = pick_coach(number)
			if number = 0:
				return False
		spread_limited_infection(user2)
def pick_coach(number):
	for coach, remaining in population.iteritems():
		if remaining == number-count:
			return coach
	return False
def spread_limited_infection(user):
	user.infectSelf()
	for student in user.students:
		student.infectSelf()
		print 'hi'

def printPopulation():
	for item in population.iteritems():
		print item[0].username, item[1]
if __name__ == "__main__":
	global population
	global count
	count = 0
	population = {}
	userA = User('userA')
	userB = User('userB')
	userC = User('userC')
	userD = User('userD')
	userE = User('userE')
	userF = User('userF')
	userG = User('userG')
	userH = User('userH')
	userI = User('userI')
	userA.assignStudents(userB)
	userB.assignStudents(userC)
	userB.assignStudents(userD)
	userE.assignStudents(userF)
	userG.assignStudents(userH)
	userG.assignStudents(userI)
	
	limited_infection(userB, 5)
	printPopulation()
	print userA.infected, 'userA'
	print userB.infected, 'userB'
	print userC.infected, 'userC'
	print userD.infected, 'userD'
	print userE.infected, 'userE'
	print userF.infected, 'userF'
	print userG.infected, 'userG'
	print userH.infected, 'userH'
	print userI.infected, 'userI'




