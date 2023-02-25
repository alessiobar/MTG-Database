import json
import re

import pandas as pd

# with open("AtomicCards.json", "r", encoding="utf8") as myfile:
#   myjson = json.load(myfile)
#   myjson_data = myjson["data"]
#   attributes = set()
#   for key in myjson_data:
#     value = myjson_data[key][0]
#     for attr in value:
#       attributes.add(attr)
#
#   col_drop = ["colorIdentity", "colorIndicator", "foreignData", "hand", "hasAlternativeDeckLimit", "identifiers",
#               "leadershipSkills", "life", "purchaseUrls", "side", "type"]
#
#   attributes = sorted(list(attributes - set(col_drop)))
#
#   cards = pd.DataFrame(columns=attributes)
#   colors = pd.DataFrame(columns=["card", "color"])
#   keywords = pd.DataFrame(columns=["card", "keyword"])
#   legalities = pd.DataFrame(columns=["card", "commander", "historic", "legacy", "modern", "pauper", "standard", "vintage"])
#   legal_list = ["commander", "historic", "legacy", "modern", "pauper", "standard", "vintage"]
#   printings = pd.DataFrame(columns=["card", "set"])
#   rulings = pd.DataFrame(columns=["card", "date", "text"])
#   subtypes = pd.DataFrame(columns=["card", "subtype"])
#   supertypes = pd.DataFrame(columns=["card", "supertype"])
#   types = pd.DataFrame(columns=["card", "type"])
#
#   count = 0
#
#   for key in myjson_data:
#     print(count/len(myjson_data))
#     count+=1
#     value = myjson_data[key][0]
#     newrow = dict.fromkeys(attributes, r"\N")
#     newrow["isReserved"] = 0
#     for v in value:
#       if v not in attributes: continue
#       if v=="convertedManaCost":
#         if(isinstance(value[v], float)): newrow[v] = int(value[v])
#         else: newrow[v] = value[v]
#       elif v=="colors":
#         mylist = value[v]
#         for word in mylist:
#           x = {"card": value["name"], "color": word}
#           colors = colors.append(x, ignore_index = True)
#       elif v=="isReserved":
#         newrow[v] = 1
#       elif v=="keywords":
#         mylist = value[v]
#         for word in mylist:
#           x = {"card": value["name"], "keyword": word}
#           keywords = keywords.append(x, ignore_index = True)
#       elif v=="legalities":
#         mylist = value[v]
#         x = {"card": value["name"]}
#         for word in legal_list:
#           if word not in mylist: x[word] = "Not Legal"
#           else: x[word] = mylist[word]
#         legalities = legalities.append(x, ignore_index = True)
#       elif v=="printings":
#         mylist = value[v]
#         for word in mylist:
#           x = {"card": value["name"], "set": word}
#           printings = printings.append(x, ignore_index = True)
#       elif v=="rulings":
#         mylist = value[v]
#         c = 1
#         last_date = ""
#         for ruling in mylist:
#           if ruling["date"] != last_date:
#             c = 1
#             last_date = ruling["date"]
#           else: c+=1
#           x = {"card": value["name"], "date": ruling["date"], "daily_id": c, "text": ruling["text"]}
#           rulings = rulings.append(x, ignore_index = True)
#       elif v=="subtypes":
#         mylist = value[v]
#         for word in mylist:
#           x = {"card": value["name"], "subtype": word}
#           subtypes = subtypes.append(x, ignore_index = True)
#       elif v=="supertypes":
#         mylist = value[v]
#         for word in mylist:
#           x = {"card": value["name"], "supertype": word}
#           supertypes = supertypes.append(x, ignore_index = True)
#       elif v=="types":
#         mylist = value[v]
#         for word in mylist:
#           x = {"card": value["name"], "type": word}
#           types = types.append(x, ignore_index = True)
#       elif v=="text":
#         newrow[v] = re.sub(r"\n"," ", value[v])
#       else: newrow[v] = value[v]
#     cards = cards.append(newrow, ignore_index = True)

#  cards = cards.drop(columns=["colors","keywords","legalities","printings","rulings","subtypes","supertypes","types"])

  # cards.to_csv('cards.csv', sep="§", encoding="utf-8")
  # colors.to_csv('colors.csv', sep="§", encoding="utf-8")
  # keywords.to_csv('keywords.csv', sep="§", encoding="utf-8")
  # legalities.to_csv('legalities.csv', sep="§", encoding="utf-8")
  # printings.to_csv('printings.csv', sep="§", encoding="utf-8")
  # rulings.to_csv('rulings.csv', sep="§", encoding="utf-8")
  # subtypes.to_csv('subtypes.csv', sep="§", encoding="utf-8")
  # supertypes.to_csv('supertypes.csv', sep="§", encoding="utf-8")
  # types.to_csv('types.csv', sep="§", encoding="utf-8")

# with open("SetList.json", "r", encoding="utf8") as myfile:
#   myjson = json.load(myfile)
#   myjson_data = myjson["data"]
#   attributes = set()
#   for s in myjson_data:
#     for key in s:
#         attributes.add(key)
#
#   col_drop = ["codeV3", "isForeignOnly", "isNonFoilOnly", "isPaperOnly", "isPartialPreview", "keyruneCode", "mcmId",
#               "mcmIdExtras", "mcmName", "mtgoCode", "parentCode", "sealedProduct", "tcgplayerGroupId", "translations"]
#
#   attributes = sorted(list(attributes - set(col_drop)))
#
#   count = 0
#
#   sets = pd.DataFrame(columns=attributes)
#
# for s in myjson_data:
#   newrow = dict.fromkeys(attributes, r"\N")
#   for key in s:
#     print(count/len(myjson_data))
#     count+=1
#     if key not in attributes: continue
#     value = s[key]
#     if key=="isFoilOnly":
#       value = str(value)
#       if value.lower()=="true": newrow[key] = 1
#       else: newrow[key] = 0
#     elif key == "isOnlineOnly":
#       value = str(value)
#       if value.lower()=="true": newrow[key] = 1
#       else: newrow[key] = 0
#     else: newrow[key] = value
#   sets = sets.append(newrow, ignore_index = True)
#
#   sets.to_csv('sets.csv', sep="§", encoding="utf-8")
#

# with open("DeckList.json", "r", encoding="utf8") as myfile:
#   myjson = json.load(myfile)
#   myjson_data = myjson["data"]
#   attributes = set()
#   for s in myjson_data:
#     for key in s:
#         attributes.add(key)
#
#   col_drop = ["fileName", "name"]
#
#   attributes = sorted(list(attributes - set(col_drop)))
#
#   count = 0
#
#   decks = pd.DataFrame(columns=attributes)
#
# last_row = dict.fromkeys(attributes, r"\N")
# for s in myjson_data:
#   newrow = dict.fromkeys(attributes, r"\N")
#   for key in s:
#     print(count/len(myjson_data))
#     count+=1
#     if key not in attributes: continue
#     value = s[key]
#     newrow[key] = value
#   if newrow["code"]==last_row["code"]:
#     decks = decks[:-1]
#   decks = decks.append(newrow, ignore_index = True)
#   last_row = newrow
#
#
#   decks.to_csv('decks.csv', sep="§", encoding="utf-8")

# mycols = ["artist", "frameVersion", "isFullArt", "isPromo",
#           "isTextless", "name", "rarity", "setCode", "uuid"]
#
# df = pd.read_csv("cards_printings.csv", usecols=mycols, low_memory=False)
#
# df.to_csv("printings.csv", sep="|")

with open("AllPrices.json", "r", encoding="utf8") as myfile:
  myjson = json.load(myfile)
  myjson_data = myjson["data"]

  prices = pd.DataFrame(columns=["uuid","normal","foil"])

  count = 0
  d = 0

  for card in myjson_data:
      print(count/len(myjson))
      count+=1
      card_obj = myjson_data[card]
      newrow = {"uuid": card, "normal": r"\N", "foil": r"\N"}
      if "paper" in card_obj.keys():
          paper = card_obj["paper"]
          if "cardmarket" in paper.keys():
              d+=1
              mkm = paper["cardmarket"]
              if "retail" in mkm.keys():
                  retail = mkm["retail"]
                  for type in retail:
                      x = retail[type]
                      price = 0
                      for data in x:
                          price+=x[data]
                      newrow[type] = price/len(x)
      prices = prices.append(newrow, ignore_index=True)

  print(count/d)
  prices.to_csv('prices.csv', sep="§", encoding="utf-8")



