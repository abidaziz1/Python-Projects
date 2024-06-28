import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

# create an object to ToastNotifier
n = ToastNotifier()

# create a function to get the data from the website
def get_data(url):
    r = requests.get(url)
    return r.text

# create a function to parse the data
htmldata = get_data("https://weather.com/en-IN/weather/today/1.25.59.85.14?par=google&temp=c/")
soup = BeautifulSoup(htmldata, 'html.parser')
current_temp = soup.find_all("span", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY") 
chances_rain = soup.find_all("div", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf") 

temp = (str(current_temp))
temp_rain = str(chances_rain)

result = "current_temp " + temp[128:-9] + "  in patna bihar" + "\n" + temp_rain[131:-14] 
n.show_toast("live Weather update",  
             result, duration = 10)