import csv



with open('IMDb movies.csv') as f:
    reader = csv.DictReader(f)
    movies = [line for line in reader]
    action_movies = [movie for movie in movies if 'Action' in movie['Genre']]
   
print(action_movies)   



with open('title.principals.csv','r') as f:
    f = list(f)
     
    actors = []
       
for i in f:
    string_data = ""
    data_list = []

    for x in i:
        
        if x == ",":
            data_list.append(string_data)
            string_data = ""
        
        string_data += x
         

    
    if 'actor' in data_list[3]:
        actors.append(data_list[2])



                

        