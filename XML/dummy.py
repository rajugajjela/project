# Creating an HTML file
Func = open("GFG-1.html","w")
   
# Adding input data to the HTML file
Func.write("<html>\n<head>\n<title> \nOutput Data in an HTML file \
           </title>\n</head> <body><h1>Welcome to <u>GeeksforGeeks</u></h1>\
           \n<h2>A <u>CS</u> Portal for Everyone</h2> \n</body></html>")
              
# Saving the data into the HTML file
Func.close()