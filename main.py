import tweepy
import config

client = tweepy.Client(bearer_token =config.BEARER_TOKEN)


def searchTweet( key ):
  
   response = client.search_recent_tweets(query=key, max_results=10, tweet_fields = {'created_at'}, expansions=['author_id'])
   users = {u['id']: u  for u in response.includes['users']}

   for tweet in response.data:
     if users[tweet.author_id]:
        print('-------------------------------------------------------------------------------------------------------\n')   
        user = users[tweet.author_id]
        print('Tweet Dari : ',user.username)
        print(tweet.text)
        print('-------------------------------------------------------------------------------------------------------\n')
   x = (input("Kembali ke menu (y/n) ? :  "))
   if x == 'y':
      main()
   else:
      exit()
   

def display_banner():
   banner_text='''  
88888888888                              888    .d8888b.                                    
    888                                  888   d88P  Y88b                                   
    888                                  888   Y88b.                                        
    888  888  888  888  .d88b.   .d88b.  888888 "Y888b.    .d8888b 888d888 8888b.  88888b.  
    888  888  888  888 d8P  Y8b d8P  Y8b 888       "Y88b. d88P"    888P"      "88b 888 "88b 
    888  888  888  888 88888888 88888888 888         "888 888      888    .d888888 888  888 
    888  Y88b 888 d88P Y8b.     Y8b.     Y88b. Y88b  d88P Y88b.    888    888  888 888 d88P 
    888   "Y8888888P"   "Y8888   "Y8888   "Y888 "Y8888P"   "Y8888P 888    "Y888888 88888P"  
                                                                                   888      
                                                                                   888      
                                                                                   888       
   Tweet Scrap v1.0
   Coded by Jevon Adelwin
   -------------------------------------------------------------------------------------------------------
   '''
   print(banner_text)
   
def main():
   print('Pilih tools di bawah ini :\n')
   print('1. Search Tweet')
   print('2. Get Trends')
   print('3. Count Result \n')
   num = (input("Masukkan pilihan anda :"))

   if num == '1':
      key = (input("Masukkan kata pencarian :"))
      searchTweet(key)
   elif num == '2' :
      print('dua')
   else:
      print('tiga')


display_banner()
main()




#link https://youtu.be/0EekpQBEP_8