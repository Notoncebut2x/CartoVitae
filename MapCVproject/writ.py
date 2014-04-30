import csv
file = open('file.html',"w")  #opens and creates a file called file.html

coded=open('hardcode.html','r')  #opens the hardcode html and reads it
for line in coded:              #for every line in the html this writes it to the open file
    file.write(line)
    
with open("data.csv", 'rU') as csvfile:    #now we open the csv called data.csv
     linereader = csv.reader(csvfile, delimiter=',')  #reads the csv
     next(linereader, None)             #skips the header
     for line in linereader:            #goes through each line in the csv
        file.write("\nvar popup = L.popup()")       #write the popup line for the html
        file.write("\n            .setLatLng(["+line[6]+","+line[7]+"])")   #puts in the lat and lon from csv line
        file.write("\n            .setContent('<p><b>"+line[0]+"</b> <BR/>"+line[1]+"<br/> BLURB </p>')")  #puts in the city and country from csv line
        file.write("\n            .addTo(map);")   #another line for html

file.write('\n</script>')  #ends the html script
file.write('\n</body>')
file.write('\n</html>')

coded.close()   #closes the hardcode file
file.close()    #closes the file