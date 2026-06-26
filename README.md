# Weather App 🌤️

A sleek, modern desktop Weather Application built with **Python 3** and **PyQt5**. The application fetches real-time weather data via the **OpenWeatherMap API** and features a premium dark-themed user interface with dynamic visual feedback.

## Features ✨

* **Real-time Data:** Fetches live temperature, weather descriptions, and contextual emojis using the OpenWeatherMap API.
* **Modern Dark UI:** Premium `#121824` dark mode styling with custom input focus highlights and responsive layouts.
* **3D Button Animations:** Interactive "Get Weather" button that provides physical pressing depth and hover effects.
* **Smart Loading State:** The search button automatically disables and changes to `"Searching..."` during API calls to prevent redundant network requests.
* **Seamless UX:** Trigger searches instantly by either clicking the button or pressing the **Enter / Return** key inside the input field.
* **Robust Error Handling:** Structured `try-except` blocks and `match-case` routing to handle custom messages for 404 (City not found), network timeouts, and connection losses without breaking the UI.
* **Custom Desktop Icon:** Fully integrated application branding with a dedicated taskbar and window icon.

## Preview 📱

![Weather App Preview](preview.png)

## Prerequisites 🛠️

Before running the application, ensure you have Python installed and install the required dependencies:

```bash
pip install PyQt5 requests

How to Run 🚀
Clone this repository or download the source code.

Ensure your custom application icon (weather-icon.png) is located in the same directory as main.py.

Run the application from your terminal:

Bash
python main.py
Project Structure 📁
Plaintext
├── main.py             # Main application logic and UI styling
├── weather-icon.png    # Custom application window and taskbar icon
└── README.md           # Project documentation
Technical Details 🧠
GUI Framework: PyQt5 (QtWidgets, QtCore, QtGui)

Styling: Custom Qt Style Sheets (QSS) mimicking modern CSS variables.

HTTP Client: requests library utilizing secure endpoints with metric unit configurations.

State Management: Utilizes QApplication.processEvents() to force UI responsiveness during network handshakes.