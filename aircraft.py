# Every flight that is found arriving or departing the selected airfield will be in this class.
# Also there are some string splitting and modification from the original JSON data to show more 
# 'in real life' style in the finished flight strip.
# 
# (1) Due to different user input styles on the altitude value (variable 'alt') we have to first identify the 
# style of the input and after that split and concatenate the values to be coherent with the ICAO standards
# and of course to achieve the IRL feel of the product.
# 
# (2) Also later on we check the route field of the flight plan to determine if the flight already has a runway 
# and SID or STAR procedure set. This is a network limitation and this info is being amended by a controller
# within their software. This ATC software then modifies the route section of the flight plan and adds certain
# data to store the active runway and SID or STAR procedure.


class Aircraft:
    def __init__(self, callsign="", phonetic="", code=0, atyp="", remarks="", time=0, alt=0, sidstar="", rwy="", dep="", dest="", ete=0, route="", frules=""):
        self.callsign = callsign
        self.phonetic = phonetic
        self.code = code
        if len(atyp) <= 7:
            self.atyp = atyp
        else:
            self.atyp = atyp[0:6]
        self.remarks = remarks[0:65]
        self.time = time

        if alt[0:2] == "FL":        # (1)
            alt = alt[2:] * 100
        if int(alt) > 4999:
            self.alt = "F" + alt[0:3]
        else:
            self.alt = "A" + "0" + alt[0:2]
        if dest == "EFHK":          # (2)
            if "/" in route[-11:] and len(route) >= 11 and frules == "I":
                self.sidstar = route[-11:].split("/")[0]
                self.rwy = route[-11:].split("/")[1]
            else:
                self.sidstar = ""
                self.rwy = ""
        elif dep == "EFHK":
            if "/" in route[0:11] and len(route) >= 11 and frules == "I":
                self.sidstar = route[0:11].split("/")[0]
                self.rwy = route[0:11].split("/")[1]
            if "AHDG" in route[0:4] and len(route) >= 11 and frules == "I":
                self.sidstar = route[0:7].split("/")[0]
                self.rwy = route[0:7].split("/")[1]
            else:
                self.sidstar = ""
                self.rwy = ""
        else:
            self.sidstar = ""
            self.rwy = ""
        self.depdest = dep + ' ' + dest
        self.ete = ete
        self.route = route[0:24]
        self.frules = frules
