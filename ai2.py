import csv

data=[]
with open('DataTugas2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        data.append(row)

penghasilan_a=0.5;
penghasilan_b=0.75;

penghasilan_c=0.5;
penghasilan_d=0.75;
penghasilan_e=1;
penghasilan_f=1.5;

penghasilan_g=1;
penghasilan_h=1.5;


def penghasilan_low(x):
	if(x<=0.5): return 1;
	elif(x<=0.75):
		return (penghasilan_b-x)/(penghasilan_b - penghasilan_a);
	else: return 0;

def penghasilan_mid(x):
	if(x<=0.5): return 0;
	elif(x<=0.75):
		return (x-penghasilan_c)/(penghasilan_d - penghasilan_c);
	elif(x<=1):
		return 1;
	elif(x<=1.5):
		return (penghasilan_e-x)/(penghasilan_e - penghasilan_f);
	else: return 0;

def penghasilan_high(x):
	if(x<=1): return 0;
	elif(x<=1.5):
		return (x-penghasilan_g)/(penghasilan_h - penghasilan_g);
	else: return 1;

hutang_a=25;
hutang_b=50;

hutang_c=25;
hutang_d=50;
hutang_e=75;
hutang_f=100;

hutang_g=75;
hutang_h=100;

def hutang_low(x):
	if(x<=25): return 1;
	elif(x<=50):
		return (hutang_b-x)/(hutang_b - hutang_a);
	else: return 0;

def hutang_mid(x):
	if(x<=25): return 0;
	elif(x<=50):
		return (x-hutang_c)/(hutang_d - hutang_c);
	elif(x<=75):
		return 1;
	elif(x<=100):
		return (hutang_e-x)/(hutang_e - hutang_f);
	else: return 0;

def hutang_high(x):
	if(x<=75): return 0;
	elif(x<=100):
		return (x-hutang_g)/(hutang_h - hutang_g);
	else: return 1;


def fuzzipendapatan(data):
	data.append(penghasilan_high(float(data[1]))) //3
	data.append(penghasilan_mid(float(data[1]))) //4
	data.append(penghasilan_low(float(data[1]))) //5
	return data;
def fuzzihutang(data):
	data.append(hutang_high(float(data[2])))//6
	data.append(hutang_mid(float(data[2]))) //7
	data.append(hutang_low(float(data[2]))) //8
	return data;

def Accepted(data):
	return max(min(data[6],data[4]),min(data[6],data[5]),min(data[7],data[5]));
def considered(data):
	return max(min(data[6],data[3]),min(data[7],data[3]),min(data[7],data[4]),min(data[8],data[5]));
def rejected(data):
	return max(min(data[8],data[3]),min(data[8],data[4]));

def inference(data):
	data.append(Accepted(data));
	data.append(considered(data));
	data.append(rejected(data));
	return data;

def maxb(r,c,a,i):
	return max(r[i],c[i],a[i]);

def defuzzi(data):
	r=[1,1,1,1,0.75,0.25,0,0,0,0];
	c=[0,0,0,0,0.25,0.75,0.75,0.25,0,0];
	a=[0,0,0,0,0,0,0.25,0.75,1,1];
	b=[];

	if (data[11]<=0.25):
		r=[data[11],data[11],data[11],data[11],data[11],data[11],0,0,0,0];
	elif(data[11]<=0.75):
		r=[data[11],data[11],data[11],data[11],data[11],0.25,0,0,0,0];
	else:
		r=[data[11],data[11],data[11],data[11],0.75,0.25,0,0,0,0];

	if(data[10]<=0.25):
		c=[0,0,0,0,data[10],data[10],data[10],data[10],0,0];
	elif(data[10]<=0.75):
		c=[0,0,0,0,0.25,data[10],data[10],0.25,0,0];
	else:
		c=[0,0,0,0,0.25,0.75,0.75,0.25,0,0];

	if(data[9]<=0.25):
		a=[0,0,0,0,0,0,data[9],data[9],data[9],data[9]];
	elif(data[9]<=0.75):
		a=[0,0,0,0,0,0,0.25,data[9],data[9],data[9]];
	else:
		a=[0,0,0,0,0,0,0.25,0.75,data[9],data[9]];

	for i in range(10):
		b.append(maxb(r,c,a,i))

	z=0;
	y=0;
	for i in range(10):
		z+=((i*10)+5)*b[i];
		y+=b[i];

	data.append(z/y);
	return data;

for i in range(1,101):
	data[i]=fuzzipendapatan(data[i])
	data[i]=fuzzihutang(data[i])
	data[i]=inference(data[i])
	data[i]=defuzzi(data[i])

def take(elem):
	return elem[12]
data.pop(0)
data.sort(key=take,reverse=True)
for i in range(80):
	data.pop(20)

#for row in data:
	#print(row[0],row[12])

with open('TebakanTugas2.csv','w',newline ='\n') as hasil:
	write = csv.writer(hasil,dialect='excel')
	for row in data : 
		write.writerow([row[0]])
		print([row[0]])
hasil.close()
#print(Accepted(data[1]));
#print(considered(data[1]));`