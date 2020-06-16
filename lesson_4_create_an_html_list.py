items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

#write your code here

for item in items:
    html_str += str("<li>") + item + str("</li>")  +"\n"
html_str +=  "</ul>"
print(html_str)

#output
<ul>
<li>first string</li>
<li>second string</li>
</ul>

#Provided solution using format

items = ['first string', 'second string']
html_str = "<ul>\n"          # The "\n" here is the end-of-line char, causing
                             # chars after this in html_str to be on next line

for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)
