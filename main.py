# Thomas Martin 

# Import requests module
import requests

# Import lxml module
from lxml import html

def parseInput(teamInput):

    # Converts user input to lowercase and removes leading and trailing spaces
    teamInput = teamInput.lower().strip()

    # Arizona Diamondbacks
    if teamInput == "arizona diamondbacks" or teamInput == "diamondbacks" or teamInput == "ari":
        return "Diamondbacks,ARI"
    
    # Atlanta Braves
    elif teamInput == "atlanta braves" or teamInput == "braves" or teamInput == "atl":
        return "Braves,ATL"
    
    # Baltimore Orioles
    elif teamInput == "baltimore orioles" or teamInput == "orioles" or teamInput == "bal":
        return "Orioles,BAL"
    
    # Boston Red Sox
    elif teamInput == "boston red sox" or teamInput == "red sox" or teamInput == "bos":
        return "Red Sox,BOS"

    # Chicago Cubs
    elif teamInput == "chicago cubs" or teamInput == "cubs" or teamInput == "chc":
        return "Cubs,CHC"
    
    # Chicago White Sox
    elif teamInput == "chicago white sox" or teamInput == "white sox" or teamInput == "chw":
        return "White Sox,CHW"
    
    # Cincinnati Reds
    elif teamInput == "cincinnati reds" or teamInput == "reds" or teamInput == "cin":
        return "Reds,CIN"
    
    # Cleveland Indians
    elif teamInput == "cleveland indians" or teamInput == "indians" or teamInput == "cle":
        return "Indians,CLE"
    
    # Colorado Rockies
    elif teamInput == "colorado rockies" or teamInput == "rockies" or teamInput == "col":
        return "Rockies,COL"
    
    # Detroit Tigers
    elif teamInput == "detroit tigers" or teamInput == "tigers" or teamInput == "bal":
        return "Tigers,DET"
    
    # Houston Astros
    elif teamInput == "houston astros" or teamInput == "astros" or teamInput == "hou":
        return "Astros,HOU"
    
    # Kansas City Royals
    elif teamInput == "kansas city royals" or teamInput == "royals" or teamInput == "kcr":
        return "Royals,KCR"
    
    # Los Angeles Angels
    elif teamInput == "los angeles angels" or teamInput == "angels" or teamInput == "laa":
        return "Angels,LAA"
    
    # Los Angeles Dodgers
    elif teamInput == "los angeles dodgers" or teamInput == "dodgers" or teamInput == "lad":
        return "Dodgers,LAD"
    
    # Miami Marlins
    elif teamInput == "miami marlins" or teamInput == "marlins" or teamInput == "mia":
        return "Marlins,MIA"
    
    # Milwaukee Brewers
    elif teamInput == "milwaukee brewers" or teamInput == "brewers" or teamInput == "mil":
        return "Brewers,MIL"
    
    # Minnesota Twins
    elif teamInput == "minnesota twins" or teamInput == "twins" or teamInput == "min":
        return "Twins,MIN"
    
    # New York Mets
    elif teamInput == "new york mets" or teamInput == "mets" or teamInput == "nym":
        return "Mets,NYM"
    
    # New York Yankees
    elif teamInput == "new york yankees" or teamInput == "yankees" or teamInput == "nyy":
        return "Yankees,NYY"
    
    # Oakland Athletics
    elif teamInput == "oakland athletics" or teamInput == "athletics" or teamInput == "oak":
        return "Athletics,OAK"
    
    # Philadelphia Phillies
    elif teamInput == "philadelphia phillies" or teamInput == "phillies" or teamInput == "phi":
        return "Phillies,PHI"
    
    # Pittsburgh Pirates
    elif teamInput == "pittsburgh pirates" or teamInput == "pirates" or teamInput == "pit":
        return "Pirates,PIT"
    
    # San Diego Padres
    elif teamInput == "san diego padres" or teamInput == "padres" or teamInput == "sdp":
        return "Padres,SDP"
    
    # San Francisco Giants
    elif teamInput == "san francisco giants" or teamInput == "giants" or teamInput == "sfg":
        return "Giants,SFG"
    
    # Seattle Mariners
    elif teamInput == "seattle mariners" or teamInput == "mariners" or teamInput == "sea":
        return "Mariners,SEA"
    
    # St. Louis Cardinals
    elif teamInput == "st. louis cardinals" or teamInput == "cardinals" or teamInput == "stl":
        return "Cardinals,STL"
    
    # Tampa Bay Rays
    elif teamInput == "tampa bay rays" or teamInput == "rays" or teamInput == "tbr":
        return "Rays,TBR"
    
    # Texas Rangers
    elif teamInput == "texas rangers" or teamInput == "rangers" or teamInput =="tex":
        return "Rangers,TEX"
    
    # Toronto Blue Jays
    elif teamInput == "toronto blue jays" or teamInput == "blue jays" or teamInput == "tor":
        return "Blue Jays,TOR"
    
    # Washington Nationals
    elif teamInput == "washington nationals" or teamInput == "nationals" or teamInput == "wsn":
        return "Nationals,WSN"
    
    # Invalid team
    else:
        return "invalid"

def getUserInputs():

    # Gets home team
    while True:
        teamInput = input("Enter the name of the home team: ")
        if parseInput(teamInput) == "invalid":
            print("invalid team.")
            continue
        else:
            homeTeam = parseInput(teamInput).split(",")[0]
            homeAbbr = parseInput(teamInput).split(",")[1]
            break

    # Gets home year
    while True:
        homeYear = input("Enter the year: ")
        homePage = requests.get("http://baseball-reference.com/teams/" + homeAbbr + "/" + homeYear + ".shtml")
        if str(homePage) == "<Response [404]>":
            print("Invalid year.")
            continue
        else:
            break
    
    # Gets away team
    while True:
        teamInput = input("Enter the name of the away team: ")
        if parseInput(teamInput) == "invalid":
            print("invalid team.")
            continue
        else:
            awayTeam = parseInput(teamInput).split(",")[0]
            awayAbbr = parseInput(teamInput).split(",")[1]
            break

    # Gets away year
    while True:
        awayYear = input("Enter the year: ")
        awayPage = requests.get("http://baseball-reference.com/teams/" + awayAbbr + "/" + awayYear + ".shtml")
        if str(awayPage) == "<Response [404]>":
            print("Invalid year.")
            continue
        else:
            break
    
    # Creates a list of inputs
    inputList = [homeTeam, awayTeam, homeAbbr, awayAbbr, homeYear, awayYear]
    return inputList

def getBatters(abbrs, years):

    # Page in which data for home team is sourced from
    homePage = requests.get("http://baseball-reference.com/teams/" + abbrs["home"] + "/" + years["home"] + ".shtml")
    homeTree = html.fromstring(homePage.content)

    # Page in which data for away team is sourced from
    awayPage = requests.get("http://baseball-reference.com/teams/" + abbrs["away"] + "/" + years["away"] + ".shtml")
    awayTree = html.fromstring(awayPage.content)

    # Initializes batters
    batters = {"home": 
                            [
                                [[""], [0], [0], [0], [0], [0], [0]],
                                [[""], [0], [0], [0], [0], [0], [0]],
                                [[""], [0], [0], [0], [0], [0], [0]],
                                [[""], [0], [0], [0], [0], [0], [0]],
                                [[""], [0], [0], [0], [0], [0], [0]],
                                [[""], [0], [0], [0], [0], [0], [0]],
                                [[""], [0], [0], [0], [0], [0], [0]],
                                [[""], [0], [0], [0], [0], [0], [0]],
                                [[""], [0], [0], [0], [0], [0], [0]]
                            ],
                    "away":
                            [
                                [[""], [0], [0], [0], [0], [0], [0]],
                                [[""], [0], [0], [0], [0], [0], [0]],
                                [[""], [0], [0], [0], [0], [0], [0]],
                                [[""], [0], [0], [0], [0], [0], [0]],
                                [[""], [0], [0], [0], [0], [0], [0]],
                                [[""], [0], [0], [0], [0], [0], [0]],
                                [[""], [0], [0], [0], [0], [0], [0]],
                                [[""], [0], [0], [0], [0], [0], [0]],
                                [[""], [0], [0], [0], [0], [0], [0]]
                            ]
    }

    # Scrapes name, AVG, OBP, SLG, HR, RBI, and OPS of first 8 batters
    for i in range(8):

        # Home team
        # Scrapes name of batter and adds to batters
        fullName = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[' + str(i+1) + "]/td[2]/@csk")
        firstName = str(fullName).partition(",")[2]
        lastName = str(fullName).partition(",")[0]
        batters["home"][i][0] = firstName.strip("[],'") + " " + lastName.strip("[],'")

        # Scrapes AVG of batter and adds to batters
        avg = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[' + str(i+1) + "]/td[17]/text()")
        batters["home"][i][1] = float(str(avg).strip("[]'"))

        # Scrapes OBP of batter and adds to batters
        obp = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[' + str(i+1) + "]/td[18]/text()")
        batters["home"][i][2] = float(str(obp).strip("[]'"))

        # Scrapes SLG of batter and adds to batters
        slg = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[' + str(i+1) + "]/td[19]/text()")
        batters["home"][i][3] = float(str(slg).strip("[]'"))

        # Scrapes HR of batter and adds to batters
        hr = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[' + str(i+1) + "]/td[11]/text()")
        batters["home"][i][4] = int(str(hr).strip("[]'"))

        # Scrapes RBI of batter and adds to batters
        rbi = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[' + str(i+1) + "]/td[12]/text()")
        batters["home"][i][5] = int(str(rbi).strip("[]'"))

        # Scrapes OPS of batter and adds to batters
        ops = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[' + str(i+1) + "]/td[20]/text()")
        batters["home"][i][6] = float(str(ops).strip("[]'"))

        # Away team
        # Scrapes name of batter and adds to batters
        fullName = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[' + str(i+1) + "]/td[2]/@csk")
        firstName = str(fullName).partition(",")[2]
        lastName = str(fullName).partition(",")[0]
        batters["away"][i][0] = firstName.strip("[],'") + " " + lastName.strip("[],'")

        # Scrapes AVG of batter and adds to batters
        avg = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[' + str(i+1) + "]/td[17]/text()")
        batters["away"][i][1] = float(str(avg).strip("[]'"))

        # Scrapes OBP of batter and adds to batters
        obp = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[' + str(i+1) + "]/td[18]/text()")
        batters["away"][i][2] = float(str(obp).strip("[]'"))

        # Scrapes SLG of batter and adds to batters
        slg = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[' + str(i+1) + "]/td[19]/text()")
        batters["away"][i][3] = float(str(slg).strip("[]'"))

        # Scrapes HR of batter and adds to batters
        hr = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[' + str(i+1) + "]/td[11]/text()")
        batters["away"][i][4] = int(str(hr).strip("[]'"))

        # Scrapes RBI of batter and adds to batters
        rbi = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[' + str(i+1) + "]/td[12]/text()")
        batters["away"][i][5] = int(str(rbi).strip("[]'"))

        # Scrapes OPS of batter and adds to batters
        ops = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[' + str(i+1) + "]/td[20]/text()")
        batters["away"][i][6] = float(str(ops).strip("[]'"))

    # Scrapes name, AVG, OBP, SLG, HR, RBI, and OPS of 9th batter separately because of the designated hitter in the National League

    # Home team
    fullName = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[9]/td[2]/@csk')
    if fullName == []:
        fullName = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[10]/td[2]/@csk')
    firstName = str(fullName).partition(",")[2]
    lastName = str(fullName).partition(",")[0]
    batters["home"][8][0] = firstName.strip("[],'") + " " + lastName.strip("[],'")

    avg = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[9]/td[17]/text()')
    if avg == []:
        avg = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[10]/td[17]/text()')
    batters["home"][8][1] = float(str(avg).strip("[]'"))

    obp = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[9]/td[18]/text()')
    if obp == []:
        obp = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[10]/td[18]/text()')
    batters["home"][8][2] = float(str(obp).strip("[]'"))

    slg = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[9]/td[19]/text()')
    if slg == []:
        slg = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[10]/td[19]/text()')
    batters["home"][8][3] = float(str(slg).strip("[]'"))

    hr = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[9]/td[11]/text()')
    if hr == []:
        hr = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[10]/td[11]/text()')
    batters["home"][8][4] = int(str(hr).strip("[]'"))

    rbi = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[9]/td[12]/text()')
    if rbi == []:
        rbi = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[10]/td[12]/text()')
    batters["home"][8][5] = int(str(rbi).strip("[]'"))

    ops = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[9]/td[20]/text()')
    if ops == []:
        ops = homeTree.xpath('//table[@id="team_batting"]/tbody/tr[10]/td[20]/text()')
    batters["home"][8][6] = float(str(ops).strip("[]'"))

    # Away team
    fullName = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[9]/td[2]/@csk')
    if fullName == []:
        fullName = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[10]/td[2]/@csk')
    firstName = str(fullName).partition(",")[2]
    lastName = str(fullName).partition(",")[0]
    batters["away"][8][0] = firstName.strip("[],'") + " " + lastName.strip("[],'")

    avg = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[9]/td[17]/text()')
    if avg == []:
        avg = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[10]/td[17]/text()')
    batters["away"][8][1] = float(str(avg).strip("[]'"))

    obp = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[9]/td[18]/text()')
    if obp == []:
        obp = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[10]/td[18]/text()')
    batters["away"][8][2] = float(str(obp).strip("[]'"))

    slg = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[9]/td[19]/text()')
    if slg == []:
        slg = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[10]/td[19]/text()')
    batters["away"][8][3] = float(str(slg).strip("[]'"))

    hr = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[9]/td[11]/text()')
    if hr == []:
        hr = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[10]/td[11]/text()')
    batters["away"][8][4] = int(str(hr).strip("[]'"))

    rbi = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[9]/td[12]/text()')
    if rbi == []:
        rbi = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[10]/td[12]/text()')
    batters["away"][8][5] = int(str(rbi).strip("[]'"))

    ops = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[9]/td[20]/text()')
    if ops == []:
        ops = awayTree.xpath('//table[@id="team_batting"]/tbody/tr[10]/td[20]/text()')
    batters["away"][8][6] = float(str(ops).strip("[]'"))

    # Assigns batting order based on on base percentage
    batters["home"] = sorted(batters["home"], key=lambda i: i[6], reverse=True)
    batters["away"] = sorted(batters["away"], key=lambda i: i[6], reverse=True)

    return batters

inputs = getUserInputs()
teams = {"home": inputs[0], "away": inputs[1]}
abbrs = {"home": inputs[2], "away": inputs[3]}
years = {"home": inputs[4], "away": inputs[5]}

batters = getBatters(abbrs, years)

# print(batters)

def formatAvg(avg):

  # Convert to string
  avgString = str(avg)

  # Remove leading zero
  avgString = avgString[1:]

  # Add trailing zeroes if necessary
  if len(avgString) == 2:
    avgString += "00"
  elif len(avgString) == 3:
    avgString += "0"
  
  return avgString

def formatObp(obp):

 # Convert to string
  obpString = str(obp)

  # Remove leading zero
  obpString = obpString[1:]

  # Add trailing zeroes if necessary
  if len(obpString) == 2:
    obpString += "00"
  elif len(obpString) == 3:
    obpString += "0"
  
  return obpString

def formatSlg(slg):
    
 # Convert to string
  slgString = str(slg)

  # Remove leading zero
  slgString = slgString[1:]

  # Add trailing zeroes if necessary
  if len(slgString) == 2:
    slgString += "00"
  elif len(slgString) == 3:
    slgString += "0"
  
  return slgString

def formatOps(ops):

  # Convert to string
  opsString = str(ops)

  # OPS over 1
  if ops >= 1:

    # Add trailing zeroes if necessary
    if len(opsString) == 3:
      opsString += "00"
    elif len(opsString) == 4:
      opsString += "0"

    return opsString
  
  else:

    # Remove leading zero
    opsString = opsString[1:]

    # Add trailing zeroes if necessary
    if len(opsString) == 2:
      opsString += "00"
    elif len(opsString) == 3:
      opsString += "0"

    return opsString

def formatTripleSlash(avg, slg, obp):
  avg = str(formatAvg(avg))
  obp = str(formatObp(obp))
  slg = str(formatSlg(slg))

  tripleSlash = avg + "/" + slg + "/" + obp

  return tripleSlash

print("")
print("Lineup for the", str(years["home"]), str(teams["home"]) + ":")

for i in range(9):
  print(str(i+1) + ". ", end="")
  print(batters["home"][i][0] + " ", end="")
  avg = batters["home"][i][1]
  obp = batters["home"][i][2]
  slg = batters["home"][i][3]
  ops = batters["home"][i][6]
  print(str(formatTripleSlash(avg, obp, slg)) + " ", end="")
  print(str(batters["home"][i][4]) + " HR ", end="" )
  print(str(batters["home"][i][5]) + " RBI ", end="" )
  print(formatOps(ops), end="")
  print("")

print("")
print("Lineup for the", str(years["away"]), str(teams["away"]) + ":")

for i in range(9):
  print(str(i+1) + ". ", end="")
  print(batters["away"][i][0] + " ", end="")
  avg = batters["away"][i][1]
  obp = batters["away"][i][2]
  slg = batters["away"][i][3]
  ops = batters["away"][i][6]
  print(str(formatTripleSlash(avg, obp, slg)) + " ", end="")
  print(str(batters["away"][i][4]) + " HR ", end="" )
  print(str(batters["away"][i][5]) + " RBI ", end="" )
  print(formatOps(ops), end="")
  print("")
