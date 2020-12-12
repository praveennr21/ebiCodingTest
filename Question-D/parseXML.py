import xml.etree.ElementTree as ET


tree = ET.parse('input.xml') 
root = tree.getroot() 

res = {}
names = set()
for article in root.findall('./Article'):
    for author in article.findall('./AuthorList/Author'):
            
            name1 = author.find('LastName').text + ', ' + author.find('ForeName').text.replace(" ", "")
            names.add(name1)
            for author in article.findall('./AuthorList/Author'):
                name2 = author.find('LastName').text + ', ' + author.find('ForeName').text.replace(" ", "")
                tup1 = (name1,name2)
                if tup1 in res:
                    res[tup1] +=  1
                else:
                    res[tup1] =  1


for name1 in sorted(names):
     for name2 in sorted(names):
        tup = (name1,name2)
        if tup in res:
            out = '{'+name1+' : '+name2+'} => '+str(res[tup])
        else:
            out = '{'+name1+' : '+name2+'} => 0'
        print(out)
       
