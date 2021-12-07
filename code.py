from vatsimdata import get_data
import svgwrite
from svgwrite import cm, mm
import webbrowser

print("*************************************************")
print("*       VATSIM FLIGHT STRIP PRINTER             *")
print("*                                               *")
print("* Get preformatted and 'print ready' strips for *")
print("*           Helsinki Airport (EFHK)             *")
print("*                                               *")
print("*    ONLY FOR FLIGHT SIMULATION PURPOSES        *")
print("*************************************************")

arr = get_data()
dwg = svgwrite.Drawing('flightstrip.svg', profile='full')
file = 'flightstrip.svg'

# IBM Plex Mono font + styling
dwg.add_stylesheet("styles.css", title="pls")


def draw_strip(y, flight):
    # Draw the actual strips blackish lines.
    dwg.add(dwg.rect((10, 10+y), (20*cm, 29*mm),
                     stroke=svgwrite.rgb(10, 10, 16, '%'),
                     fill='none')
            )
    dwg.add(dwg.line((160, 10+y), (160, 120 + y),
                     stroke=svgwrite.rgb(10, 10, 16, '%'),
                     fill='none')
            )
    dwg.add(dwg.rect((10, 10+y), (10, 20),
                     stroke=svgwrite.rgb(10, 10, 16, '%'),
                     fill='black')
            )
    dwg.add(dwg.line((240, 10+y), (240, 120 + y),
                     stroke=svgwrite.rgb(10, 10, 16, '%'),
                     fill='none')
            )
    dwg.add(dwg.line((320, 10+y), (320, 120 + y),
                     stroke=svgwrite.rgb(10, 10, 16, '%'),
                     fill='none')
            )
    dwg.add(dwg.line((400, 10+y), (400, 120 + y),
                     stroke=svgwrite.rgb(10, 10, 16, '%'),
                     fill='none')
            )
    dwg.add(dwg.line((480, 10+y), (480, 120 + y),
                     stroke=svgwrite.rgb(10, 10, 16, '%'),
                     fill='none')
            )
    dwg.add(dwg.line((560, 10+y), (560, 120 + y),
                     stroke=svgwrite.rgb(10, 10, 16, '%'),
                     fill='none')
            )
    dwg.add(dwg.line((560, 65+y), (765, 65 + y),
                     stroke=svgwrite.rgb(10, 10, 16, '%'),
                     fill='none')
            )
    dwg.add(dwg.line((628, 65+y), (628, 120 + y),
                     stroke=svgwrite.rgb(10, 10, 16, '%'),
                     fill='none')
            )
    dwg.add(dwg.line((696, 65+y), (696, 120 + y),
                     stroke=svgwrite.rgb(10, 10, 16, '%'),
                     fill='none')
            )

    # Fill the strip with parsed JSON data
    dwg.add(dwg.text(flight.callsign,
                     insert=(25, 35 + y),
                     fill='black',
                     class_='largebold'
                     )
            )
    dwg.add(dwg.text(flight.phonetic,
                     insert=(85, 50 + y),
                     fill='black',
                     class_='normal'
                     )
            )
    dwg.add(dwg.text(flight.code,
                     insert=(25, 65 + y),
                     fill='black',
                     class_='largebold'
                     )
            )
    dwg.add(dwg.text(flight.atyp,
                     insert=(25, 90 + y),
                     fill='black',
                     class_='normal'
                     )
            )
    dwg.add(dwg.text(flight.remarks,
                     insert=(25, 115 + y),
                     fill='black',
                     class_='normal'
                     )
            )
    dwg.add(dwg.text(flight.time,
                     insert=(180, 27 + y),
                     fill='black',
                     class_='normal'
                     )
            )
    dwg.add(dwg.text(flight.alt,
                     insert=(340, 27 + y),
                     fill='black',
                     class_='normal'
                     )
            )
    dwg.add(dwg.text(flight.sidstar,
                     insert=(410, 27 + y),
                     fill='black',
                     class_='normal'
                     )
            )
    dwg.add(dwg.text(flight.rwy,
                     insert=(505, 35 + y),
                     fill='black',
                     class_='largebold'
                     )
            )
    dwg.add(dwg.text(flight.depdest,
                     insert=(560, 35 + y),
                     fill='black',
                     class_='largebold'
                     )
            )
    dwg.add(dwg.text(flight.ete,
                     insert=(690, 35 + y),
                     fill='black',
                     class_='normal'
                     )
            )
    dwg.add(dwg.text(flight.frules,
                     insert=(750, 27 + y),
                     fill='black',
                     class_='normal'
                     )
            )
    dwg.add(dwg.text(flight.route,
                     insert=(560, 60 + y),
                     fill='black',
                     class_='normal'
                     )
            )

# Produce a strip for every flight that is found and also add
# 140 px to every strip to get multiple strips on the SVG.
print("\nThe following flights have been saved to the SVG file. ")
for i, flight in enumerate(arr):
    draw_strip(i * 140, flight)
    print(f" {i+1}: {flight.callsign}")

print(f"\nTotal of {i+1} flights have been found")

# Save the SVG file
dwg.save()

a = input("\nOpen the flightstrip.svg in a browser? (y/n) ")
if a == "y":
    webbrowser.open(file, new=2)

print("\nThe program will now exit.")
