outputString = ""


print("input a file name")
fileName = input();


file = open(fileName,'r');
for line in file:
	data = line.split();
	lastName= data[0];
	firstName = data[1];
	year = data[2];
	
	outputString +=data[0]+'\n'+data[1]+'\n'+data[2]+'\n\n'
	
	

file.close()
file = open(fileName,'w');

file.write(outputString);
	
	