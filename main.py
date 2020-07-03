from tkinter import *
from tkinter import messagebox

from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit



#top.geometry("500×500")

def weather_frame(city_n):
	
	#top.quit()
	tip=Tk()
	#tip.geometry("10000×10000")
	L1=Label(tip,text="Information")
	L1.pack()
	data = YahooWeather(APP_ID="YRSMqB52",api_key="dj0yJmk9VFRGTXdSYWlwdHJMJmQ9WVdrOVdWSlRUWEZDTlRJbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTQ0",api_secret="15747a90eda83eed3e53f99accaa6bf1c3b959b8")
	#city_n="Nagpur"
	data.get_yahoo_weather_by_city(city_n, Unit.celsius)
	temp=data.condition.temperature
	#msg2=data.condition.text
	text = Text(tip)
	text.insert(INSERT,"Temperature of ")
	text.insert(INSERT,city_n)
	text.insert(INSERT," ")
	text.insert(INSERT,temp)
	text.insert(INSERT,"°C")
	text.insert(INSERT,"\n")
	text.insert(END," ")
	text.pack()
	B1=Button(tip,text="Exit",command=exit,activebackground="Green")
	B1.place(x = 100,y = 100)
	B1.pack()
	tip.mainloop()




def close():
	top.destroy()


def main():
	
	top = Tk()
	#print(winfo(top))
	top.geometry("500x1430")
	L1 = Label(top, text = "Enter City Name")
	L1.pack( side = LEFT)
	
	E1 = Entry(top, bd = 5)
	E1.pack(side = RIGHT)
	var=E1.get()
	
	L2=Label(top, text="Weather")
	L2.pack()
	
	B1 = Button(top, text = "Okay", command =lambda:weather_frame(var) ,activebackground="Yellow")
	#B1.place(x = 50,y = 550)
	B1.pack()
	top.mainloop()
	

main()
