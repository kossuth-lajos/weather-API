import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        
        # Set window icon (ensure the file is in the same directory)
        self.setWindowIcon(QIcon("weather-icon.png"))
        
        # Fix window size for a compact, modern look
        self.setFixedSize(400, 550)

        # Set placeholder text for the input field
        self.city_input.setPlaceholderText("e.g., London, New York, Budapest")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        # Content margins and spacing for a clean UI layout
        vbox.setContentsMargins(30, 40, 30, 40)
        vbox.setSpacing(15)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city-label")
        self.city_input.setObjectName("city-input")
        self.get_weather_button.setObjectName("get-weather-button")
        self.temperature_label.setObjectName("temperature-label")
        self.emoji_label.setObjectName("emoji-label")
        self.description_label.setObjectName("description-label")

        # PREMIUM UPGRADED DARK THEME STYLING
        self.setStyleSheet("""
            /* Main window background */
            QWidget {
                background-color: #121824;
            }
            
            /* Global font and text color */
            QLabel {
                font-family: "Segoe UI", Calibri, sans-serif;
                color: #ffffff;
            }
            
            /* Title label styling */
            QLabel#city-label {
                font-size: 26px;
                font-weight: 300;
                color: #a0aec0;
                margin-bottom: 5px;
            }
            
            /* City input field */
            QLineEdit#city-input {
                font-size: 22px;
                font-family: "Segoe UI", sans-serif;
                color: #ffffff;
                background-color: #1a2333;
                border: 2px solid #2d3748;
                border-radius: 12px;
                padding: 10px;
                margin-bottom: 5px;
            }
            /* Input field hover effect */
            QLineEdit#city-input:hover {
                border: 2px solid #4a5568;
            }
            /* Input field focus effect */
            QLineEdit#city-input:focus {
                border: 2px solid #3182ce;
            }
            /* Placeholder text color */
            QLineEdit#city-input::placeholder {
                color: #4a5568;
            }
            
            /* Get Weather button with 3D click effect */
            QPushButton#get-weather-button {
                font-family: "Segoe UI", sans-serif;
                font-size: 18px;
                font-weight: bold;
                color: #ffffff;
                background-color: #3182ce;
                border: none;
                border-bottom: 3px solid #2b6cb0;
                border-radius: 12px;
                padding: 12px;
            }
            QPushButton#get-weather-button:hover {
                background-color: #3182ce;
                border-bottom: 3px solid #4299e1;
            }
            QPushButton#get-weather-button:pressed {
                background-color: #2b6cb0;
                border-bottom: 1px solid #2b6cb0;
                margin-top: 2px;
            }
            /* Style for disabled button during API request */
            QPushButton#get-weather-button:disabled {
                background-color: #2d3748;
                color: #718096;
                border-bottom: 3px solid #1a2333;
            }
            
            /* Temperature display styling */
            QLabel#temperature-label {
                font-size: 70px;
                font-weight: bold;
                color: #ffffff;
                margin-top: 15px;
            }
            
            /* Emoji display styling */
            QLabel#emoji-label {
                font-size: 90px;
                font-family: "Segoe UI Emoji";
                margin-top: -10px;
                margin-bottom: -10px;
            }
            
            /* Weather description text */
            QLabel#description-label {
                font-size: 24px;
                font-weight: 400;
                color: #cbd5e0;
                text-transform: capitalize;
            }
        """)
        
        # Event connections
        self.get_weather_button.clicked.connect(self.get_weather)
        # ADDED: Pressing Enter inside the input field will now trigger the search
        self.city_input.returnPressed.connect(self.get_weather)

    def get_weather(self):
        api_key = "4aeb08f244170468d3df104d416d3fc9"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        # Disable button and update text to show loading state
        self.get_weather_button.setText("Searching...")
        self.get_weather_button.setEnabled(False)
        
        # Force UI update immediately
        QApplication.processEvents()

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400: self.display_error("Bad Request:\nPlease check input")
                case 401: self.display_error("Unauthorized:\nInvalid API key")
                case 403: self.display_error("Forbidden:\nAccess denied")
                case 404: self.display_error("Not Found:\nCity not found")
                case _: self.display_error(f"HTTP Error:\n{response.status_code}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nRequest timed out")
        except requests.exceptions.RequestException as request_error:
            self.display_error(f"Error:\n{request_error}")
        
        finally:
            # Always re-enable the button and restore text when the request is done
            self.get_weather_button.setText("Get Weather")
            self.get_weather_button.setEnabled(True)
        
    def display_error(self, message):
        # Format the label for error messages (red color, smaller text)
        self.temperature_label.setStyleSheet("font-size: 22px; color: #fc8181; font-weight: bold;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        # Restore original white style for successful weather display
        self.temperature_label.setStyleSheet("font-size: 70px; color: #ffffff; font-weight: bold;")
        
        temperature_c = data["main"]["temp"]
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        self.temperature_label.setText(f"{temperature_c:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232: return "⛈️"
        elif 300 <= weather_id <= 321: return "🌥️" 
        elif 500 <= weather_id <= 531: return "🌧️"
        elif 600 <= weather_id <= 622: return "🌨️"
        elif 701 <= weather_id <= 741: return "🌁"
        elif weather_id == 762: return "🌋"
        elif weather_id == 771: return "💨"
        elif weather_id == 781: return "🌪️"
        elif weather_id == 800: return "☀️"
        elif 801 <= weather_id <= 804: return "🌤️"
        return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())