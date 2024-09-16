def twoDarrays():
  comedyquesans = [
      ["What is the main plot of 'Dumb and Dumber'?",
       "two friends embark on a cross-country journey to return a briefcase"],
      ["Who plays the lead role in 'Anchorman: The Legend of Ron Burgundy'?", "will ferrell"],
      ["In 'Bridesmaids', what is the name of Kristen Wig's character?", "annie walker"],
      ["Which movie features a talking raccoon and a sentient tree?", "guardians of the galaxy"],
      ["What is the catchphrase of Ace Ventura in 'Ace Ventura: Pet Detective'?", "alrighty then"],
      ["In 'Superbad', what are the main characters trying to do?", "buy alcohol for a party"],
      ["Who directed 'The Grand Budapest Hotel'?", "wes anderson"],
      ["What is the central theme of 'Groundhog Day'?", "time loop"],
      ["Which comedy film stars Seth Rogen and James Franco as journalists involved in a CIA plot?", "the interview"],
      ["What is the title of the comedy film about a bachelor party in Las Vegas gone wrong?", "the hangover"],
      ["In 'Ferris Bueller's Day Off', what does Ferris pretend to be?", "sick"],
      ["Who plays the character of Michael Scott in the TV series 'The Office'?", "steve carell"],
      ["What is the name of the fictional newspaper in 'Anchorman'?", "channel 4 news"],
      ["Which comedy film features a character named Ron Swanson?", "parks and recreation"],
      ["What is the nickname of the character played by Jonah Hill in '21 Jump Street'?", "schmidt"],
      ["Who directed 'The 40-Year-Old Virgin'?", "judd apatow"],
      ["In 'Napoleon Dynamite', what is Napoleon's favorite hobby?", "tetherball"],
      [
          "Which comedy film stars Cameron Diaz, Leslie Mann, and Kate Upton as women seeking revenge on a cheating husband?",
          "the other woman"],
      ["What is the name of the dog in 'There's Something About Mary'?", "puffy"],
      ["Which movie features a character named McLovin?", "superbad"]
  ]
  actionquesans = [
      ["Who played the character of John McClane in 'Die Hard'?", "bruce willis"],
      ["What is the name of the artificial intelligence in the 'Terminator' series?", "skynet"],
      ["In 'The Matrix', what pill does Neo take?", "the red pill"],
      ["Which actor portrayed Ethan Hunt in the 'Mission: Impossible' series?", "tom cruise"],
      ["What is the title of the first 'Rambo' film?", "first blood"],
      ["Who directed 'Mad Max: Fury Road'?", "george miller"],
      ["In 'The Dark Knight', who played the Joker?", "heath ledger"],
      ["What is the name of the fictional African country in 'Black Panther'?", "wakanda"],
      ["Which movie features a character named Jason Bourne?", "the bourne identity"],
      ["Who directed 'Kill Bill: Volume 1' and 'Kill Bill: Volume 2'?", "quentin tarantino"],
      ["What is the name of the organization that opposes the IMF in 'Mission: Impossible'?", "the syndicate"],
      [
          "Which film follows a team of illusionists who pull off bank heists during their performances and reward their audiences with the money?",
          "now you see me"],
      ["Who is the protagonist of the 'John Wick' film series?", "john wick"],
      ["In 'The Terminator', what is the model number of the Terminator played by Arnold Schwarzenegger?", "t-800"],
      ["What is the main plot of 'Speed'?",
       "a cop must prevent a bomb from exploding on a city bus if its speed drops below 50 mph"],
      ["Who played the role of Trinity in 'The Matrix' trilogy?", "carrie anne moss"],
      ["Which movie features a character named Sarah Connor?", "the terminator"],
      ["What is the name of the fictional spy agency in the 'Kingsman' films?", "kingsman"],
      ["In 'Mad Max: Fury Road', what is Furiosa's mission?", "to rescue Immortan joe's wives"],
      ["Who directed the 'Lethal Weapon' film series?", "richard donner"]
  ]
  horrorquesans = ["In the horror film 'the conjuring,' what is the name of the possessed doll", "annabelle"], [
      "Which 1980 film follows a group of camp counselors who are stalked and murdered by an unknown assailant",
      "friday the 13th"], ["What is the name of the demon nun in 'the nun' (2018)", "valak"], [
      "In the horror movie 'a nightmare on elm street,' how does freddy krueger haunt his victims",
      "in their dreams"], [
      "What 2017 film features a group of kids facing a shape-shifting entity that often takes the form of a clown",
      "it"], ["In the movie 'the blair witch project,' what type of setting do the characters explore", "forest"], [
      "What is the name of the mysterious videotape in the japanese horror film 'ringu' (1998)",
      "the cursed videotape"], [
      "Which horror film involves a family being terrorized by malevolent supernatural forces after moving into a new house (1982)",
      "poltergeist"], ["In 'the cabin in the woods,' what is revealed to be controlling the events in the cabin",
                       "government organization"], ["What is the name of the hotel in stephen king's 'the shining'",
                                                    "the overlook"], [
      "Which classic horror film tells the story of a man who transforms into a giant insect", "the fly"], [
      "In the horror movie 'insidious,' what is the alternate realm visited by the characters", "the further"], [
      "What 2004 horror film involves a group of people facing terrifying experiences inside an abandoned insane asylum",
      "session 9"], [
      "Which horror film is known for its found footage style and depicts the events of a paranormal investigation (2009)",
      "paranormal activity"], [
      "In 'the others' (2001), what is the twist ending regarding the characters and the haunted house",
      "they are the ghosts"], ["What is the name of the family in 'the texas chain saw massacre' (1974)",
                               "the sawyers"], [
      "Which horror film features a creature that can only be seen by those who are about to die", "it follows"], [
      "What 1968 horror film directed by george a. romero is considered a classic in the zombie genre",
      "night of the living dead"], [
      "In 'rosemary's baby,' what is the name of the demonic cult that manipulates rosemary", "the castevets"], [
      "What is the title of the horror film that revolves around a deadly curse transmitted through a videotape",
      "the ring"]
  return comedyquesans, actionquesans, horrorquesans


def login():
  username = input("Welcome to the Movie Quiz, create your username please (maximum 10 characters and minimum 1 character please):")
  while len(username) > 10 or len(username) < 1:
      username = input("Try again, create your username please:")
  usergenre = input("Enter one of the following genres please (comedy, action, or horror): ")
  while usergenre != "comedy" and usergenre != "action" and usergenre != "horror":
      usergenre = input("Enter one of the following genres please (comedy, action, or horror): ")
  else:
      print("You selected the genre:", usergenre)
      print("")
      print("The rules are as follows:")
      print("")
      print("1. Answer 10 movie-related questions without using uppercase letters")
      print("2. You have 3 tries for each question")
      print(
          "3. If you answer incorrectly, you will recieve an incorrect answer message; if you're out of tries, you will recieve the correct answer and move on to the next question")
      print("4. If you answer correctly, the question ends, and you proceed to the next question")
      print("5. After completing all questions, you'll be told how many you answered correctly")
      print("6. You will be given the choice to display your info on a genre-based leaderboard through a website")
      print("")
  agree_disagree = input("Do you agree to and accept rules? Enter 'yes' or 'no':")
  if agree_disagree == "yes":
      print("you may start quiz")
      return agree_disagree, usergenre, username
  else:
      print("you cannot start quiz")
      return agree_disagree, usergenre, username


import random
def questions(usergenre, agree_disagree, comedyquesans, actionquesans, horrorquesans):
  total = 0
  if agree_disagree == "yes" and usergenre == "comedy":
      question_indices = list(range(len(comedyquesans)))
      random.shuffle(question_indices)
      for i in range(10):
          x = question_indices[i]
          print("")
          print(str(i + 1) + ".", comedyquesans[x][0])
          useranswer = input("Enter your answer:")
          if useranswer == comedyquesans[x][1]:
              print("")
              print("Correct, onto the next question!")
              total = total + 1
          else:
              tries = 2
              while tries > 1 and useranswer != comedyquesans[x][1]:
                  print("Incorrect, you have", tries, "tries left")
                  tries = tries - 1
                  useranswer = input("Enter your answer:")
                  if tries == 1 and useranswer != comedyquesans[x][1]:
                      print("Incorrect, you have", tries, "try left")
                      useranswer = input("Enter your answer:")
              if useranswer == comedyquesans[x][1]:
                  print("")
                  print("Correct, onto the next question!")
                  total = total + 1
              else:
                  print("")
                  print("The correct answer is:", comedyquesans[x][1])

  if agree_disagree == "yes" and usergenre == "action":
      question_indices = list(range(len(actionquesans)))
      random.shuffle(question_indices)
      for i in range(10):
          x = question_indices[i]
          print("")
          print(str(i + 1) + ".", actionquesans[x][0])
          useranswer = input("Enter your answer:")
          if useranswer == actionquesans[x][1]:
              print("")
              print("Correct, onto the next question!")
              total = total + 1
          else:
              tries = 2
              while tries > 1 and useranswer != actionquesans[x][1]:
                  print("Incorrect, you have", tries, "tries left")
                  tries = tries - 1
                  useranswer = input("Enter your answer:")
                  if tries == 1 and useranswer != actionquesans[x][1]:
                      print("Incorrect, you have", tries, "try left")
                      useranswer = input("Enter your answer:")
              if useranswer == actionquesans[x][1]:
                  print("")
                  print("Correct, onto the next question!")
                  total = total + 1
              else:
                  print("")
                  print("The correct answer is:", actionquesans[x][1])

  if agree_disagree == "yes" and usergenre == "horror":
      question_indices = list(range(len(horrorquesans)))
      random.shuffle(question_indices)
      for i in range(10):
          x = question_indices[i]
          print("")
          print(str(i + 1) + ".", horrorquesans[x][0])
          useranswer = input("Enter your answer:")
          if useranswer == horrorquesans[x][1]:
              print("")
              print("Correct, onto the next question!")
              total = total + 1
          else:
              tries = 2
              while tries > 1 and useranswer != horrorquesans[x][1]:
                  print("Incorrect, you have", tries, "tries left")
                  tries = tries - 1
                  useranswer = input("Enter your answer:")
                  if tries == 1 and useranswer != horrorquesans[x][1]:
                      print("Incorrect, you have", tries, "try left")
                      useranswer = input("Enter your answer:")
              if useranswer == horrorquesans[x][1]:
                  print("")
                  print("Correct, onto the next question!")
                  total = total + 1
              else:
                  print("")
                  print("The correct answer is:", horrorquesans[x][1])

  return total


def clarification(total, agree_disagree, usergenre, username):
  print("")
  if agree_disagree == "yes":
      print("You scored", total, "/10 !")
      infodisplayed = input("Would you like your name and score displayed on a leaderboard based on the genre you have picked? Enter 'yes' or 'no':")
      if infodisplayed == "yes" and usergenre == "comedy":
          import csv
          filetowrite = open("unsortedlbcomedy.csv", "a")
          newcontents = csv.writer(filetowrite)
          newcontents.writerow([username, total, usergenre])

      import csv
      if infodisplayed == "yes" and usergenre == "action":
          filetowrite = open("unsortedlbaction.csv", "a")
          newcontents = csv.writer(filetowrite)
          newcontents.writerow([username, total, usergenre])

      import csv
      if infodisplayed == "yes" and usergenre == "horror":
          filetowrite = open("unsortedlbhorror.csv", "a")
          newcontents = csv.writer(filetowrite)
          newcontents.writerow([username, total, usergenre])

      return infodisplayed

class playerinfo:
  def __init__(self):
      self.username = ""
      self.score = 0
      self.genre = ""


def arrayofrecord(usergenre):
  playerlistcomedy = []
  playerlistaction = []
  playerlisthorror = []

  import csv
  if usergenre == "comedy":
      filetoread = open("unsortedlbcomedy.csv", "r")
      filecontents = csv.reader(filetoread)
      for line in filecontents:
          if line:
              player = playerinfo()
              if len(line) >= 3:
                  player.username = line[0]
                  player.score = line[1]
                  player.genre = line[2]
                  playerlistcomedy.append(player)

  import csv
  if usergenre == "action":
      filetoread = open("unsortedlbaction.csv", "r")
      filecontents = csv.reader(filetoread)
      for line in filecontents:
          if line:
              player = playerinfo()
              if len(line) >= 3:
                  player.username = line[0]
                  player.score = line[1]
                  player.genre = line[2]
                  playerlistaction.append(player)

  import csv
  if usergenre == "horror":
      filetoread = open("unsortedlbhorror.csv", "r")
      filecontents = csv.reader(filetoread)
      for line in filecontents:
          if line:
              player = playerinfo()
              if len(line) >= 3:
                  player.username = line[0]
                  player.score = line[1]
                  player.genre = line[2]
                  playerlisthorror.append(player)

  return playerlistcomedy, playerlistaction, playerlisthorror


def bubblesort(playerlistcomedy, playerlistaction, playerlisthorror, usergenre):
  if usergenre == "comedy":
      n = len(playerlistcomedy) - 1
      swapped = True
      while swapped == True and n >= 0:
          swapped = False
          for i in range(n):
              if playerlistcomedy[i].score < playerlistcomedy[i + 1].score:
                  temp = playerlistcomedy[i]
                  playerlistcomedy[i] = playerlistcomedy[i + 1]
                  playerlistcomedy[i + 1] = temp
                  swapped = True

  if usergenre == "action":
      n = len(playerlistaction) - 1
      swapped = True
      while swapped == True and n >= 0:
          swapped = False
          for i in range(n):
              if playerlistaction[i].score < playerlistaction[i + 1].score:
                  temp = playerlistaction[i]
                  playerlistaction[i] = playerlistaction[i + 1]
                  playerlistaction[i + 1] = temp
                  swapped = True

  if usergenre == "horror":
      n = len(playerlisthorror) - 1
      swapped = True
      while swapped == True and n >= 0:
          swapped = False
          for i in range(n):
              if playerlisthorror[i].score < playerlisthorror[i + 1].score:
                  temp = playerlisthorror[i]
                  playerlisthorror[i] = playerlisthorror[i + 1]
                  playerlisthorror[i + 1] = temp
                  swapped = True


def sortedlb(playerlistcomedy, playerlistaction, playerlisthorror, usergenre):
  import csv
  if usergenre == "comedy":
      filetowrite = open("sortedlbcomedy.csv", "w")
      newcontents = csv.writer(filetowrite)
      for player in playerlistcomedy:
          newcontents.writerow([player.username, player.score])

  import csv
  if usergenre == "action":
      filetowrite = open("sortedlbaction.csv", "w")
      newcontents = csv.writer(filetowrite)
      for player in playerlistaction:
          newcontents.writerow([player.username, player.score])

  import csv
  if usergenre == "horror":
      filetowrite = open("sortedlbhorror.csv", "w")
      newcontents = csv.writer(filetowrite)
      for player in playerlisthorror:
          newcontents.writerow([player.username, player.score])

import webbrowser
def data_to_webpage(playerlist, usergenre, agree_disagree, infodisplayed):
  if usergenre == "action" and agree_disagree == "yes" and infodisplayed == "yes":
      with open("actionlb.html", "w") as fileout:
          html_str = """
          <!DOCTYPE html>
          <html>
          <head>
          <title>Action Movie Quiz Leaderboard</title>
          <link rel="stylesheet" href="styles.css">
          </head>
          <body>
          <h1>Action Movie Quiz Leaderboard</h1>
          <table border=1>
          <tr><td class= "header"> Username </td> <td class="header"> Score </td></tr>
          """
          fileout.write(html_str)

          for player in playerlist:
              html_str = """
                              <tr><td> %s </td> <td> %s </td></tr>  
                              """ % (player.username, player.score)
              fileout.write(html_str)

          html_str = """
          </table>
          </body>
          </html>
          """
          fileout.write(html_str)

      webbrowser.open('actionlb.html', new=1, autoraise=True)
  elif usergenre == "comedy" and agree_disagree == "yes" and infodisplayed == "yes":
      with open("comedylb.html", "w") as fileout:
          html_str = """
          <!DOCTYPE html>
          <html>
          <head>
          <title>Comedy Movie Quiz Leaderboard</title>
          <link rel="stylesheet" href="styles.css">
          </head>
          <body>
          <h1>Comedy Movie Quiz Leaderboard</h1>
          <table border=1>
          <tr><td class= "header"> Username </td> <td class="header"> Score </td></tr>
          """
          fileout.write(html_str)

          for player in playerlist:
              html_str = """
                              <tr><td> %s </td> <td> %s </td></tr> 
                              """ % (player.username, player.score)
              fileout.write(html_str)

          html_str = """
          </table>
          </body>
          </html>
          """
          fileout.write(html_str)

      webbrowser.open('comedylb.html', new=1, autoraise=True)
  elif usergenre == "horror" and agree_disagree == "yes" and infodisplayed == "yes":
      with open("horrorlb.html", "w") as fileout:
          html_str = """
          <!DOCTYPE html>
          <html>
          <head>
          <title>Horror Movie Quiz Leaderboard</title>
          <link rel="stylesheet" href="styles.css">
          </head>
          <body>
          <h1>Horror Movie Quiz Leaderboard</h1>
          <table border=1>
          <tr><td class= "header"> Username </td> <td class="header"> Score </td></tr>
          """
          fileout.write(html_str)

          for player in playerlist:
              html_str = """
                              <tr><td> %s </td> <td> %s </td></tr>  
                              """ % (player.username, player.score)
              fileout.write(html_str)

          html_str = """
          </table>
          </body>
          </html>
          """
          fileout.write(html_str)

      webbrowser.open('horrorlb.html', new=1, autoraise=True)

comedyquesans, actionquesans, horrorquesans = twoDarrays()
agree_disagree, usergenre, username = login()
total = questions(usergenre, agree_disagree, comedyquesans, actionquesans, horrorquesans)
infodisplayed = clarification(total, agree_disagree, usergenre, username)
playerlistcomedy, playerlistaction, playerlisthorror = arrayofrecord(usergenre)
bubblesort(playerlistcomedy, playerlistaction, playerlisthorror, usergenre)
sortedlb(playerlistcomedy, playerlistaction, playerlisthorror, usergenre)

if usergenre == "action":
  data_to_webpage(playerlistaction, usergenre, agree_disagree, infodisplayed)
elif usergenre == "comedy":
  data_to_webpage(playerlistcomedy, usergenre, agree_disagree, infodisplayed)
elif usergenre == "horror":
  data_to_webpage(playerlisthorror, usergenre, agree_disagree, infodisplayed)