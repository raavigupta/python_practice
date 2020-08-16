# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
sum = 0

# write your loop here
for headline in headlines:
    if (sum > 141 or len(news_ticker.join(headline)) > 141):
        break
    else:
        news_ticker=news_ticker.join(headline)
        #news_ticker=join(news_ticker)
        sum += len(news_ticker)
print(news_ticker)
    #    #print(headline)
    #    sum += len(headline)
    #    #sum += 1
    #    news_ticker=news_ticker.join("")
    #    news_ticker=news_ticker.join(news_ticker)
    #   print(sum)
    #print(news_ticker)
        
        #sum+= len(headline)
        #print(len(headline))
#print(news_ticker)
        #print(news_ticker)
    #elif(sum + len(headline) < 141):
   # continue
          
#print(sum)


#provided logic
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)
   
