from win10toast import ToastNotifier
import datetime
import requests

byCityCode = "http://api.openweathermap.org/data/2.5/forecast?id="
# City code for Chciago
cityCode = "4887398" 
# Enter your open weather map API key
apiKey = None

weatherUrl = byCityCode+cityCode+"&appid="+apiKey

today = datetime.datetime.today().strftime('%Y-%m-%d')
tomorrowWeather = set()

response = requests.get(weatherUrl)
data = response.json() 

for weatherGroup in data["list"]:
    # get the date(yyyy-mm-dd) of the forecast
    date = weatherGroup["dt_txt"].split(" ", 1)[0]
    # get tomorrow's forecast
    if(date == today):
        for weatherData in weatherGroup["weather"]:
            tomorrowWeather.add(weatherData["main"])

title = ""
message = ""
if set(["Snow", "Rain"]).issubset(tomorrowWeather):
    title = "Snow + Rain"
    message = "It is going to snow AND rain!!\nDrive carefully and bring an umbrella!"
elif "Snow" in tomorrowWeather:
    title = "Snow"
    message = "It is going to snow!!\nDrive carefully!"
elif "Rain" in tomorrowWeather:
    title = "Rain"
    message = "It is going to rain!!\nDont't forget to bring an umbrella!"

if title != "" and message != "":
    toaster = ToastNotifier()
    toaster.show_toast(title=title,msg=message, duration=10)


