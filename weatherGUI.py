from tkinter import *
import json, requests
from datetime import datetime as dt
from PIL import ImageTk, Image
import threading
from google_weather import precepitation_info

main_root = Tk()
main_root.title("OpenWeather App")
main_frame = LabelFrame(main_root, text='')
main_frame.pack(fill=BOTH, expand=1)
search_frame = LabelFrame(main_frame)
search_frame.grid(row=0, column=0, columnspan=2, sticky='news')
weather_report_frame = LabelFrame(main_frame)
weather_report_frame.grid(row=1, column=0, columnspan=2, sticky='news')
temp_frame = LabelFrame(main_frame)
temp_frame.grid(row=2, column=0, sticky='news')
temp2_frame = LabelFrame(main_frame)
temp2_frame.grid(row=2, column=1, sticky='news')
sun_time_frame = LabelFrame(main_frame)
sun_time_frame.grid(row=3, column=0, columnspan=2, sticky='news')
rain_frame = LabelFrame(main_frame)
rain_frame.grid(row=4, column=0, columnspan=2, sticky='news')
date_time_frame = LabelFrame(main_frame)
date_time_frame.grid(row=5, column=0, columnspan=2, sticky='news')

def get_weather(CITY):
    global temp_max, temp_min, temperature, feels_like, weather_report, sunrise, sunset, date_time, cloud
    if CITY:
        search_btn.config(state=DISABLED)
        weather_report_lbl.config(text="Searching.. please wait")
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        API_KEY = "2d076255db659af3c6d3bc562c9a4d15"
        URL = BASE_URL + "q=" + CITY + "&APPID=" + API_KEY
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temperature = round((float(main['temp']) - 273.15), 2)
            feels_like = round((float(main['feels_like']) - 273.15), 2)
            temp_max = round((float(main['temp_max']) - 273.15), 3)
            temp_min = round((float(main['temp_min']) - 273.15), 3)
            weather_report = data['weather'][0]['description']
            date_time = dt.fromtimestamp(data["dt"])
            sunrise = dt.fromtimestamp((data['sys'])['sunrise']).time()
            sunset = dt.fromtimestamp((data['sys'])['sunset']).time()
            cloud = str(data['clouds']['all'])
            # search_btn.config(state=NORMAL)
            return 1
        else:
            # showing the error message
            search_btn.config(state=NORMAL)
            print("Error in the HTTP request")
            return -1
    else:
        weather_report_lbl.config(text="Enter a valid city name")

def fetch():
    if get_weather(city.get())==1:
        weather_report_lbl.config(text=f'{weather_report}, cloud: {cloud}%')
        current_temp.config(text=f"{temperature}°C")
        feels_like_lbl.config(text=f"Feels like : {feels_like}°C")
        max_temp.config(text=f"Max temp: {temp_max}°C", fg='red')
        min_temp.config(text=f"Min temp: {temp_min}°C", fg='blue')
        sun_rise_lbl.config(text=f"Sunrise: {sunrise}")
        sun_set_lbl.config(text=f"Sunset: {sunset}")
        date_and_time.config(text=f"Last updated at: {date_time}")
        main_root.title(f"Showing result for: {city.get().upper()} || OpenWeather App")
        rain_frame.config(text="Getting precipitation info from google..")
        time_data, precipitation = precepitation_info(city.get())
        rain_frame.config(text=f'Forecast for {city.get().upper()}')
        prec0.pack(fill=BOTH, expand=1)
        time0.pack(fill=BOTH, expand=1)
        prec1.pack(fill=BOTH, expand=1)
        time1.pack(fill=BOTH, expand=1)
        prec2.pack(fill=BOTH, expand=1)
        time2.pack(fill=BOTH, expand=1)
        prec3.pack(fill=BOTH, expand=1)
        time3.pack(fill=BOTH, expand=1)
        prec4.pack(fill=BOTH, expand=1)
        time4.pack(fill=BOTH, expand=1)
        prec5.pack(fill=BOTH, expand=1)
        time5.pack(fill=BOTH, expand=1)
        prec6.pack(fill=BOTH, expand=1)
        time6.pack(fill=BOTH, expand=1)
        prec7.pack(fill=BOTH, expand=1)
        time7.pack(fill=BOTH, expand=1)
        prec8.pack(fill=BOTH, expand=1)
        time8.pack(fill=BOTH, expand=1)
        prec9.pack(fill=BOTH, expand=1)
        time9.pack(fill=BOTH, expand=1)

        prec0.config(text=precipitation[0])
        prec1.config(text=precipitation[1])
        prec2.config(text=precipitation[2])
        prec3.config(text=precipitation[3])
        prec4.config(text=precipitation[4])
        prec5.config(text=precipitation[5])
        prec6.config(text=precipitation[6])
        prec7.config(text=precipitation[7])
        prec8.config(text=precipitation[8])
        prec9.config(text=precipitation[9])
        time0.config(text=time_data[0])
        time1.config(text=time_data[1])
        time2.config(text=time_data[2])
        time3.config(text=time_data[3])
        time4.config(text=time_data[4])
        time5.config(text=time_data[5])
        time6.config(text=time_data[6])
        time7.config(text=time_data[7])
        time8.config(text=time_data[8])
        time9.config(text=time_data[9])
        search_btn.config(state=NORMAL)

    else:
        search_btn.config(state=NORMAL)
        weather_report_lbl.config(text="Enter a valid city name")

def main_thread(e):
    t1 = threading.Thread(target=fetch)
    t1.daemon = True
    t1.start()


# search_frame
city = Entry(search_frame, font=("Helvetica", 10, 'bold'), justify=CENTER, bd=5)
city.insert(0, 'keyyur')
city.grid(row=0, column=0, sticky='news', padx=30, pady=20)
search_btn = Button(search_frame, text="Search", relief=GROOVE, font=("Helvetica", 10, 'bold'), bd=5, command=lambda :main_thread(1))
search_btn.grid(row=0, column=1, sticky='news', pady=20, ipadx=30)
canvas = Canvas(search_frame, width=212, height=80)
canvas.grid(row=0, column=2)
img = ImageTk.PhotoImage(Image.open("assets/openweather_cpy.jpg"))
canvas.create_image(105, 40, image=img)

# weather_report_frame
weather_report_lbl = Label(weather_report_frame, text='--------', font=('Helvetica', 20, 'bold'))
weather_report_lbl.pack(fill=BOTH, expand=1)

# temp_frame
current_temp = Label(temp_frame, text="--°C", font=('Helvetica', 30, 'bold'))
feels_like_lbl = Label(temp_frame, text="Feels like : --°C", font=('Helvetica', 10))
current_temp.pack(fill=BOTH, expand=1)
feels_like_lbl.pack(fill=BOTH, expand=1)

# temp2_frame
max_temp = Label(temp2_frame, text="Max temp: --°C", font=('Helvetica', 12, 'bold'))
min_temp = Label(temp2_frame, text="Min temp: --°C", font=('Helvetica', 12, 'bold'))
max_temp.pack(fill=BOTH, expand=1)
min_temp.pack(fill=BOTH, expand=1)

# sun_time_frame
sun_rise_lbl = Label(sun_time_frame, text="Sunrise: --", font=('Calibri', 12, 'bold'), anchor=CENTER)
sun_set_lbl = Label(sun_time_frame, text="Sunset: --", font=('Calibri', 12, 'bold'), anchor=CENTER)
sunrise_canvas = Canvas(sun_time_frame, width=176, height=93)
sunset_canvas = Canvas(sun_time_frame, width=141, height=157)
sunrise_img = ImageTk.PhotoImage(Image.open("assets/sunrise.png"))
sunrise_canvas.create_image(100, 90, image=sunrise_img)
sunset_img = ImageTk.PhotoImage(Image.open("assets/sunset.png"))
sunset_canvas.create_image(80, 100, image=sunset_img)
sunrise_canvas.grid(row=0, column=0, sticky='news', padx=30, ipady=10)
sun_rise_lbl.grid(row=1, column=0, sticky='news', pady=20)
sunset_canvas.grid(row=0, column=1, sticky='news', padx=80, ipady=10)
sun_set_lbl.grid(row=1, column=1, sticky='news', pady=20)

# Rain frame
frame0 = LabelFrame(rain_frame)
frame1 = LabelFrame(rain_frame)
frame2 = LabelFrame(rain_frame)
frame3 = LabelFrame(rain_frame)
frame4 = LabelFrame(rain_frame)
frame5 = LabelFrame(rain_frame)
frame6 = LabelFrame(rain_frame)
frame7 = LabelFrame(rain_frame)
frame8 = LabelFrame(rain_frame)
frame9 = LabelFrame(rain_frame)

frame0.grid(row=0, column=0, sticky='news')
frame1.grid(row=0, column=1, sticky='news')
frame2.grid(row=0, column=2, sticky='news')
frame3.grid(row=0, column=3, sticky='news')
frame4.grid(row=0, column=4, sticky='news')
frame5.grid(row=0, column=5, sticky='news')
frame6.grid(row=0, column=6, sticky='news')
frame7.grid(row=0, column=7, sticky='news')
frame8.grid(row=0, column=8, sticky='news')
frame9.grid(row=0, column=9, sticky='news')

prec0 = Label(frame0, text='--%')
time0 = Label(frame0, text='-:--')
prec1 = Label(frame1, text='--%')
time1 = Label(frame1, text='-:--')
prec2 = Label(frame2, text='--%')
time2 = Label(frame2, text='-:--')
prec3 = Label(frame3, text='--%')
time3 = Label(frame3, text='-:-- ')
prec4 = Label(frame4, text='--%')
time4 = Label(frame4, text='-:-- ')
prec5 = Label(frame5, text='--%')
time5 = Label(frame5, text='-:-- ')
prec6 = Label(frame6, text='--%')
time6 = Label(frame6, text='-:-- ')
prec7 = Label(frame7, text='--%')
time7 = Label(frame7, text='-:-- ')
prec8 = Label(frame8, text='--%')
time8 = Label(frame8, text='-:-- ')
prec9 = Label(frame9, text='--%')
time9 = Label(frame9, text='-:-- ')

# prec0.pack(fill=BOTH, expand=1)
# time0.pack(fill=BOTH, expand=1)
# prec1.pack(fill=BOTH, expand=1)
# time1.pack(fill=BOTH, expand=1)
# prec2.pack(fill=BOTH, expand=1)
# time2.pack(fill=BOTH, expand=1)
# prec3.pack(fill=BOTH, expand=1)
# time3.pack(fill=BOTH, expand=1)
# prec4.pack(fill=BOTH, expand=1)
# time4.pack(fill=BOTH, expand=1)
# prec5.pack(fill=BOTH, expand=1)
# time5.pack(fill=BOTH, expand=1)
# prec6.pack(fill=BOTH, expand=1)
# time6.pack(fill=BOTH, expand=1)
# prec7.pack(fill=BOTH, expand=1)
# time7.pack(fill=BOTH, expand=1)
# prec8.pack(fill=BOTH, expand=1)
# time8.pack(fill=BOTH, expand=1)
# prec9.pack(fill=BOTH, expand=1)
# time9.pack(fill=BOTH, expand=1)

#date_time_frame
date_and_time = Label(date_time_frame, text="Last updated at: ", font=('Helvetica', 8), anchor=E)
date_and_time.pack(fill=BOTH, expand=1)

# Bind Enter key to the submit function
main_root.bind("<Return>", main_thread)


main_root.mainloop()
