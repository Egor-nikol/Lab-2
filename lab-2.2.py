import xml.etree.ElementTree as ET

tree = ET.parse('currency.xml')
root = tree.getroot()

charcod_vector = []
values_vector = []

for valute in root.findall('Valute'):
    charcod_vector.append(valute.find('CharCode').text)     
    values_vector.append(float(valute.find('Value').text.replace(',', '.')))

print("CharCodes:", charcod_vector)
print("Values:", values_vector)