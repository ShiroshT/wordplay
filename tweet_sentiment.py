import sys
import json


def dec_dict():
    afinnfile = open("AFINN-111.txt")
    scores = {}                        # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. 
      scores[term] = int(score)        # Convert the score to an integer.
    return scores                      # Print every (term, score) pair in the dictionary


def lines(fp):
    print str(fp.readlines())


def get_next_target(ss):
    start_str = ss.find('created_at"')
    start_tweet = ss.find('"', start_str)
    end_tweet = ss.find('"created_at"', start_tweet + 3) 
    tweet = ss[ start_tweet + 3: end_tweet] 
    return tweet, end_tweet
  
  

def get_tweets(page, scores):
    tweet_list = []
    tweet_lst= []
    tweet_lst_temp = []

    while True:
      tweet, endpos = get_next_target(page)
      if tweet:
	  tweet_list.append(tweet)
	  page = page[endpos: ]
      else:
	  break  
	  
    for i in tweet_list:
        start_str = i.find('text"')
	start_tweet = i.find('"', start_str)
	end_tweet = i.find('"', start_tweet + 3) 
	tweet = i[ start_tweet + 3: end_tweet]  
	words = tweet.split()
	f = []
	for i in words:
	    p = '@'
	    q ='http'
	    ss = '\\'	
	    r ='\u'
	    if p not in i:
		if q not in i:
		  if r not in i:
		    if ss not in i:
		        f.append(i)
	               
	tweet_lst_temp.append(f)
	
    tweet_lst = [x for x in tweet_lst_temp if x != []]
    
    sentiment_list = []
    scores_new = {}
    
    for i in tweet_lst:
        total_word = len(i)
        total = 0.
        val = 0.
        sentiment = 0.
        
        for tword in i:
	    if tword in scores:
	       val = scores[tword]
               total = total + val	   
	sentiment = total 
       
        for tword in i:
	     temp1 = scores.get(tword)
	     temp = scores_new.get(tword)
	     
	     if(temp1 == None or temp == None):	        
	        temp_sc = sentiment/total_word	        
	        scores_new.update({tword : temp_sc})	
	        
	     elif(temp != None):
	          temp_sc = sentiment/total_word
		  sco = scores_new[tword]
		  
		  new_v = (temp_sc + sco)/2.0
		  scores_new[tword] = new_v		        


    for key, value in scores_new.iteritems():
        print key, value
    
    


def main():
    data_file = open(sys.argv[1])
    scores = dec_dict()
    start_string = lines(data_file)    





if __name__ == '__main__':
    main()
