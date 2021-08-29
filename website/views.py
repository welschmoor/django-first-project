from django.shortcuts import render


def home(request):
	return render(request, 'home.html', {})


def about(request):
	return render(request, 'about.html', {})


def add(request):
	from random import randint
	num1 = randint(0, 10)
	num2 = randint(0, 10)
	print(num1, num2)

	if request.method == 'POST':
		# handling empty form:
		if not request.POST['answer']:
			result = "You didn't type anything!"
			color = "colorwrong"
			return render(request, 'add.html', {
			'num1':num1,
			'num2':num2,
			'result': result,
			'color': color,
			})


		answer = request.POST['answer']
		old_num1 = request.POST['old_num1']
		old_num2 = request.POST['old_num2']
		
		correct_answer = int(old_num1) + int(old_num2)
		if int(answer) == correct_answer:
			result = f"Correct! {old_num1} + {old_num2} = {correct_answer}"
			color = 'colorright'
		else:
			result =  f"Incorrect! {old_num1} + {old_num2} = {correct_answer}, not {answer}"
			color = 'colorwrong'

		return render(request,'add.html', {
			'answer':answer,
			'result':result,
			'num1':num1,
			'num2':num2,
			'color': color,
			})

	return render(request, 'add.html', {
		'num1': num1,
		'num2': num2,
	})	


def subtract(request):
	from random import randint
	num1 = randint(0,10)
	num2 = randint(0,10)
	print(request.POST)

	if request.method == "POST":
		# handling empty form:
		if not request.POST['answer']:
			result = "You didn't type anything!"
			color = "colorwrong"
			return render(request, 'subtract.html', {
			'num1':num1,
			'num2':num2,
			'result': result,
			'color': color,
			})


		answer = int(request.POST['answer'])
		old_num1 = int(request.POST['old_num1'])
		old_num2 = int(request.POST['old_num2'])

		correct_answer = old_num1 - old_num2
		print("test:", type(correct_answer), type(old_num2), type(old_num1), type(answer))
		if correct_answer == answer:
			print('correct')
			result = f"Correct! {old_num1} - {old_num2} = {correct_answer}"
			color = 'colorright'
		else:
			result =  f"Incorrect! {old_num1} - {old_num2} = {correct_answer}, not {answer}"
			color = 'colorwrong'
		
		return render(request, 'subtract.html', {
			'answer':answer,
			'num1':num1,
			'num2':num2,
			'color':color,
			'result':result,
		})
	return render(request, 'subtract.html', {
		'num1':num1,
		'num2':num2,
	})	


def multiply(request): 
	from random import randint
	num1 = int(randint(0,10))
	num2 = int(randint(0,10))

	if request.method == "POST":
		# handling empty form:
		if not request.POST['answer']:
			result = "You didn't type anything!"
			color = "colorwrong"
			return render(request, 'multiply.html', {
			'num1':num1,
			'num2':num2,
			'result': result,
			'color': color,
			})
		

		answer = int(request.POST['answer'])
		old_num1 = int(request.POST['old_num1'])
		old_num2 = int(request.POST['old_num2'])

		correct_answer = old_num1 * old_num2
		if correct_answer == answer:
			result = f"Correct! {old_num1} * {old_num2} = {correct_answer}"
			color = "colorright"
		else:
			result = f"Incorrect! {old_num1} * {old_num2} = {correct_answer}, not {answer}"
			color = "colorwrong"
		return render(request, 'multiply.html', {
			'answer':answer,
			'result':result,
			'num1':num1,
			'num2':num2,
			'color': color,
		})

	return render(request, 'multiply.html', {
		'num1':num1,
		'num2':num2,
	})


def divide(request):
	from random import randint
	num1 = int(randint(0,10))
	num2 = int(randint(1,10))

	if request.method == "POST":
		# handling empty form:
		if not request.POST['answer']:
			result = "You didn't type anything!"
			color = "colorwrong"
			return render(request, 'divide.html', {
			'num1':num1,
			'num2':num2,
			'result': result,
			'color': color,
			})



		answer = float(request.POST['answer'])
		old_num1 = int(request.POST['old_num1'])
		old_num2 = int(request.POST['old_num2'])

		correct_answer = round(float(old_num1 / old_num2), 2)
		if correct_answer == answer:
			result = f"Correct! {old_num1} / {old_num2} = {correct_answer}"
			color = "colorright"
		else:
			result = f"Incorrect! {old_num1} / {old_num2} = {correct_answer}, not {answer}"
			color = "colorwrong"
		return render(request, 'divide.html', {
			'answer':answer,
			'result':result,
			'num1':num1,
			'num2':num2,
			'color': color,
		})

	return render(request, 'divide.html', {
		'num1':num1,
		'num2':num2,
	})