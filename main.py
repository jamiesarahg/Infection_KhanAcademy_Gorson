#Khan Academy Infection Problem
import globals
globals.population = {}
class User:
	#Class to define each user
	def __init__(self, username):
		self.username = username
		self.infected = False
		self.coaches = []
		self.students = []
		globals.population[self] = 1

	def infectSelf(self):
		#infects this user 
		self.infected = True
		globals.population[self]-=1
		for coach in self.coaches:
			globals.population[coach]-=1

	def assignCoach(self, user):
		#assigns the input user as its coach and self as a student of the input user
		self.coaches.append(user)
		user.students.append(self)
		globals.population[user]+=1

	def assignStudents(self,user):
		# assigns the input user as a student and self as a coach of the input user
		self.students.append(user)
		user.coaches.append(self)
		globals.population[self]+=1

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



def limited_infection(user, inputNum):
	# infects the input user and all of their students and then continues to infect until  close to the input number of people infected
	count = 0
	count += globals.population[user]
	spread_limited_infection(user)
	

	while count < inputNum:
		user2 = pick_coach(inputNum, count)
		edit_inputNum = inputNum
		while user2 == False:
			edit_inputNum -= 1
			user2 = pick_coach(edit_inputNum, count)
			if edit_inputNum == 0:
				return False
		count += globals.population[user2]
		spread_limited_infection(user2)

def pick_coach(number, count):
	# picks the next coach to be infected if more people need to be infected
	for coach, remaining in globals.population.iteritems():
		if remaining == number-count:
			return coach
	return False

def spread_limited_infection(user):
	# function that infects input user and all of their students.
	user.infectSelf()
	for student in user.students:
		student.infectSelf()


def print_population():
	#prints population statistics 
	#item[0].username is the username of the discussed user
	#item[1] is how many people would be infected if chosen to spread limited infection to
	for item in globals.population.iteritems():
		print item[0].username, item[1]

def print_infection():
	numInfected = 0
	for user, remaining in globals.population.iteritems():
		print user.username, user.infected
		if user.infected == True:
			numInfected +=1
	print 'Total Infected: ', numInfected