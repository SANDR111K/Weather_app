import requests
from tkinter import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather API")

        # Center window on screen
        self.window_width = 330
        self.window_height = 300
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.window_width / 2)
        self.y = (self.screen_height / 2) - (self.window_height / 2)
        self.geometry(f"{self.window_width}x{self.window_height}+{int(self.x)}+{int(self.y)}")

        # GUI components
        self.title_label = Label(self, 
                                 text="Weather Application",
                                 fg="white",
                                 bg="blue4",
                                 padx=3,
                                 pady=20,
                                 font=("Arial", 27))
        self.title_label.pack()

        self.city_lbl = Label(self, text="Enter The City:", font=("Arial", 13))
        self.city_lbl.place(x=self.window_width // 2, y=100, anchor="center")

        self.city_ent = Entry(self, font=("Arial", 10))
        self.city_ent.place(x=self.window_width // 2, y=123, anchor="center")

        self.button = Button(self, 
                             text="CLICK ENTER", 
                             padx=28, 
                             fg="White", 
                             bg="blue4", 
                             font=("Arial", 9),
                             command=self.printer)
        self.button.place(x=self.window_width // 2, y=150, anchor="center")

        self.result_label = None  # **Initialize the result label**

    def data_getter(self):
        api_key = "your_api_key"
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        city_name = self.entry_getter()
        params = {'q': city_name, 'appid': api_key, 'units': 'metric'}

        try:
            response = requests.get(base_url, params=params)
            data = response.json()
            if data.get("cod") != 200:
                return None
            return data
        except requests.RequestException as e:
            print(f"Request Error: {e}")  # **Print request errors**
            return None

    def entry_getter(self):
        self.entry = self.city_ent.get().strip()
        return self.entry

    def checker(self):
        self.data = self.data_getter()

        if self.data is None:
            return "The city you entered does not exist."
        else:
            weather_info = (
                f"City: {self.data.get('name')}\n"
                f"Weather Description: {self.data['weather'][0].get('description')}\n"
                f"Temperature: {self.data['main'].get('temp')}°C\n"
                f"Feels Like: {self.data['main'].get('feels_like')}°C\n"
                f"Humidity: {self.data['main'].get('humidity')}%\n"
                f"Pressure: {self.data['main'].get('pressure')} hPa\n"
                f"Wind Speed: {self.data['wind'].get('speed')} m/s\n"
                f"Cloudiness: {self.data['clouds'].get('all')}%"
            )
            return weather_info

    def printer(self):
        if self.result_label:
            self.result_label.destroy()  # **Clear previous result**

        final_result = self.checker()
        self.result_label = Label(self, text=final_result)
        self.result_label.place(x=self.window_width // 2, y=230, anchor="center")

app = App()
app.mainloop()
