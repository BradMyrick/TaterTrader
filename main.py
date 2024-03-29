import tweepy
import re
import requests
import json
import hmac
import hashlib
import time

# Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Bitmart API credentials 
bitmart_api_key = "your_bitmart_api_key"
bitmart_secret_key = "your_bitmart_secret_key"
bitmart_memo = "your_bitmart_memo"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Tate brothers Twitter user IDs
tate_user_ids = ["1081562931937067009", "2334614718"] 

# Follow the Tate brothers
for user_id in tate_user_ids:
    api.create_friendship(user_id=user_id)
    print(f"Followed user {user_id}")

# Stream Tate brothers tweets
class TateStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.user.id_str in tate_user_ids:
            print(f"New tweet from {status.user.screen_name}: {status.text}")
            
            # Check for token mentions
            token_matches = re.findall(r'\$[a-zA-Z]+', status.text)
            if token_matches:
                token = token_matches[0]
                print(f"Detected token: {token}")
                
                # Buy the token on Bitmart
                buy_token(token)
            
    def on_error(self, status_code):
        print(f"Error with status code: {status_code}")
        return True

def buy_token(token):
    url = "https://api-cloud.bitmart.com/spot/v1/submit_order"
    
    params = {
        "symbol": f"{token}_USDT",  
        "side": "buy",
        "type": "market",
        "size": "10",
        "timestamp": int(time.time() * 1000)
    }
    
    # Generate signature
    message = f'{params["timestamp"]}#{bitmart_memo}#bitmart.WebSocket'
    signature = hmac.new(bitmart_secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()
    
    headers = {
        "X-BM-KEY": bitmart_api_key,
        "X-BM-SIGN": signature,
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, data=json.dumps(params), headers=headers)
    print(f"Bitmart buy response: {response.text}")
    

if __name__ == "__main__":
    stream_listener = TateStreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.filter(follow=tate_user_ids)