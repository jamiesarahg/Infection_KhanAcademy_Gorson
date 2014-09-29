README

limited_infection has two inputs, the user to start the infection and the total number of users to be infected
total_infection has one input, the user to start the infection

To run limited_infection or total_infection:

-Open python in the command line.
-Import one of the population environments as people
-Import main
-Run either function as main.FUNCTION(people.USER, #) where function is either limited_infection or total_infection and user is a user in the population environment. # is only needed for limited_infection and represents the number of people to be infected.
-Run main.print_infection() to see how many people and who were infected

Population environments are test groups of different numbers of people with different relationship arrangements. The available ones are:
groupA
groupB
groupC



Future changes:
I would have loved to spend more time on the pick_coach algorithm. I was considering options of counting the number of already infected students to help make the algorithm better. 

I was also hoping to be able to make limited_infection fail if it isn't possible to infect the exact number of people given. My current function does fail when it is not able to perfectly infect the input number but there are a few problems. If it selects a coach in the wrong order and it did happen to be possible doing it another way, my algorithm might not notice. Also, the way it is set up, as the algorithm is working it infects people, so even though it fails, it infected people in the process. In order to fix this, I would have to redesign my code so that the function would output the usernames to infect and then infect those instead of using the population as is. This would also invovle changing the algorithm, because the current state of population is used to determine the state of the infection. If it wasn't dynamically updating, the code wouldn't work.

