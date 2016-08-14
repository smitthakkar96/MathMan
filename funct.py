from random import randint
import random
import math

def linear_easy():
	a = randint(4,6)
	b = 1
	c = 1
	d = randint(1,4)
	e = randint(1,4)
	f = randint(5,10)
	question = 'Solve the linear equations %sx + %sy = 0 and %sx + %sy + %s = 0' %(a,b,d,e,f)
	answer_1 = b*f
	answer_2 = 0 #e*c
	answer_3 = e*a
	answer_4 = b*d
	answer_5 = 0 #d*c
	answer_6 = f*a
	final_answer_1 = float(answer_1 - answer_2) / (answer_3 - answer_4)
	final_answer_2 = float(answer_5 - answer_6) / (answer_3 - answer_4)
	answer = "(" + "{:.2f}".format(final_answer_1) + ", " + "{:.2f}".format(final_answer_2) + ")"
	option1 = "(" + ("{:.2f}".format(final_answer_1+ 0.23))  + ", " + ("{:.2f}".format(final_answer_2+0.23))  + ")"
	option2 = "(" + ("{:.2f}".format(final_answer_1+ 0.57))  + ", " + ("{:.2f}".format(final_answer_2+0.57))  + ")"
	option3 = "(" + ("{:.2f}".format(final_answer_1+ 0.73))  + ", " + ("{:.2f}".format(final_answer_2+0.73))  + ")"
	dict = {'question' : question, 'answer' : answer, 'option1' : option1,'option2' : option2,'option3' : option3}
	return dict


def quadeasy(): 
	a = randint(1,7)
	c = randint(1,40)
	b = 2 * math.sqrt(a*c)
	while(math.sqrt(a*c).is_integer() == False):
		c = c+1
	b = int(2 * math.sqrt(a*c))
	answer = float(-1 * b )/(2*a)
	question = "Solve the Equation %sx^2 + %sx + %s = 0" %(a ,b ,c )
	return question

def quadmedium():
	a = randint(1,7)
	b = randint(1,30)
	c = randint(2,5)
	while(math.sqrt((b*b) - (4*a*c)).is_integer() == False):
		c = c+1
	question = "Solve the Equation %sx^2 + %sx + %s = 0" %(a ,b ,c )
	return question

def quadhard():
	a = randint(4,7)
	b = randint(6,30)
	c = randint(3,10)
	while(math.sqrt((b*b) - (4*a*c)).is_integer() == False):
		c = c+1
	question = "Solve the Equation %sx^2 + %sx + %s = 0" %(a ,b ,c )
	return question

