import pandas
import twitter
from twython import Twython
import tweepy as tw
consumer_key= 'Zk3KCifttPtpQxxCyCWBNkAp4'
consumer_secret= 'HWR4XlrDHDZ1XtP2ODmg47uVI2A1RfxmcE25Xw3n2jzciNghgG'
access_token= '1206881625818034176-r8P4UupNrEbrT6XF5vu8tJ38KW5YNp'
access_token_secret= 'SBIXpsKmGmsdbYovX2ASVQzDMBrENNgQoVtKTqQgWuMbi'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# OAUTH_TOKEN = "1206881625818034176-r8P4UupNrEbrT6XF5vu8tJ38KW5YNp"
# OAUTH_TOKEN_SECRET = "SBIXpsKmGmsdbYovX2ASVQzDMBrENNgQoVtKTqQgWuMbi"
#
# APP_KEY = "Zk3KCifttPtpQxxCyCWBNkAp4"
# APP_SECRET = "HWR4XlrDHDZ1XtP2ODmg47uVI2A1RfxmcE25Xw3n2jzciNghgG"
# api  = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
# api = twitter.Api(consumer_key="Zk3KCifttPtpQxxCyCWBNkAp4",
#                   consumer_secret="HWR4XlrDHDZ1XtP2ODmg47uVI2A1RfxmcE25Xw3n2jzciNghgG",
#                   access_token_key="1206881625818034176-r8P4UupNrEbrT6XF5vu8tJ38KW5YNp",
#                   access_token_secret="SBIXpsKmGmsdbYovX2ASVQzDMBrENNgQoVtKTqQgWuMbi")
# api.sleep_on_rate_limit = True

# from csv import reader
# # read csv file as a list of lists
# with open('NBA.csv', 'r') as read_obj:
#     # pass the file object to reader() to get the reader object
#     csv_reader = reader(read_obj)
#     # Pass reader object to list() to get a list of lists
#     list_of_rows = list(csv_reader)
#     print(list_of_rows)
df = pandas.read_csv("NBA.csv",delimiter=',')
queries = [list(row) for row in df.values]


def getUserFromName(name, api):
    user_list = api.GetUsersSearch(term=name, page=1, count=1)
    if user_list:
        user = user_list[0]
        if user.verified:
            return user
    return None


V = []
for i in range(len(queries)):
    user = getUserFromName(queries[i][0], api)
    if user:
        row = [repr(user.id), user.name, user.screen_name]
        for attribute in queries[i][1:]:
            row.append(attribute)
    V.append(row)

print(V)
