# VATSIM FLIGHT STRIP PRINTER

## Purpose:
To get IRL like flight strips to be used in air traffic control tower positions within the VATSIM network.

### Function:
<p>- Program fetches real time updated JSON file from VATSIM API, which then gets parsed firstly by the airfield. The field is hard coded at the moment to point at Helsinki (EFHK). In addition of the VATSIM data JSON, another JSON is used to get phonetic callsigns for the flights, just to clarify the controller which airline is in question.</p>

<p>- Program then appends the necessary data from retrieved flight plans to a list and then they get added to a class, from where the SVGWRITE drawn flight strips are populated with their data.</p>

<p>- Lastly user can choose if the finished SVG file is opened with a browser or not.</p>



## Background:
<p>Virtual Air Traffic Simulation Network (VATSIM) is a nonprofit organization that operates an online flight-simulation network noted for its active membership and realism. Members can fly either as pilots or direct traffic as air traffic controllers, participating in what has been described as a close approximation of real-life aviation procedures.</p>

<p>VATSIM provides a flight-simulation network that allows users to either fly online as pilots or direct traffic as air traffic controllers, producing an organic simulation of air traffic. Communications between pilots and controllers are carried out using integrated VoIP or in-game text messages. Users require custom software to join the simulation.</p>

<p>Because the simulation adheres as closely as possible to real-life aviation procedures and radio phraseology, VATSIM can function as a training aid for student pilots lacking experience and private and commercial pilots looking to enhance their skills in radio communications. Events in the simulation are not hard coded on the network but rather emerge through human interaction and error. Consequently, the network has been described as bringing immersion to what was historically a solitary exercise and credited with playing a key role in the commodification of flight-simulation software.
<i>Source: Wikipedia</i></p>



## Flight strips
<p>
Program mimics the in real life Finnish standard in flight strips. Strips are used normally in every day operations in all of the Finnish controlled airfields. Flight strips come out from the printer pre-filled with data from the original flight plan filed by the pilot in command of the aircraft. </p>

<p>
The controller then fills the strip with clearances that he/she has given to the pilot of the aircraft and other types of markings that act like reminders for the controller. These markings vary from cleared altitudes, used runways, taxi instructions, departure and arrival times, etc.
</p>

<img src="https://i.gyazo.com/f8229c3b636e529b3e4a2e6bc042655b.jpg">
<em>Picture from Jyväskylä Airport's ATC tower position with several flight strips. Each representing a single flight.</em>



## Technologies used:
- Python 3.10.0
- CSS
- svgwrite
- urllib.request
- json
- webbrowser
- sys
