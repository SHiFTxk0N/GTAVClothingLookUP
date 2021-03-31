import xml.etree.ElementTree as ET

'''
P_head		= PHEAD		= hat
p_eyes      = PEYES     = eyes
p_ears      = PEARS     = ears
            = PLEFT_WRIST
            = PRIGHT_WRIST
            = PHEAD
Berd		= BERD		= mask
p_eyes		= PEYES		= glasses
uppr		= TORSO		= gloves
accs		= ACCS		= torso 1 
Decl		= DECL		= Decal
Feet		= FEET		= Shoes
hair		= HAIR		= hair
jbib		= JBIB		= torso 2
lowr		= LEGS		= legs
teef		= TEEF/TEETH	= accessories
task            = TASK          = armor 
parachute       = HAND          = parachute / duffle 

'''

class parse:
    def __init__(self, filename, gender):
       self.filename = filename
       self.tree = ET.parse('xmlfiles\\'+ self.filename + '.meta')
       self.root = self.tree.getroot()
       if gender == 'male':
           self.gender = self.root[2][0]
       elif gender == 'female':
           self.gender = self.root[2][1]    

    def display_all(self):
        for n in self.gender.findall("Item"):
            key = n.get('key')
            value = n.get('value')
            print(key, ' = ', value)
    
    def display_by_dlc(self, dlc):
        for n in self.gender.findall('Item'):
            key = n.get('key')
            d = key.split('_')
            if d[2] == dlc:
                value = n.get('value')
                print(key, ' = ', value)
    
    def display_by_variation(self, variation):
        for n in self.gender.findall('Item'):
            key = n.get('key')
            d = key.split('_')
            if d[4] == variation:
                value = n.get('value')
                print(key, ' = ', value)
    
    def display_by_dlc_and_variation(self, dlc, variation):
        for n in self.gender.findall('Item'):
            key = n.get('key')
            d = key.split('_')
            if d[2] == dlc:
                if d[4] == variation:
                    value = n.get('value')
                    print(key, ' = ', value)

    def compare_by_value(self, value):
        newlist = []
        for n in self.root[2][0].findall('Item'):
            d = n.get('value')
            if str(value) == d:
                key = n.get('key')
                newlist.append(key + ' = ' + d)

        for n in self.root[2][1].findall('Item'):
            d = n.get('value')
            if str(value) == d:
                key = n.get('key')
                newlist.append(key + ' = ' + d)

        for n in range(len(newlist)):
            a = newlist[n].split('_')
            if a[3] == 'M':
                print('\nMALE =', newlist[n])
            if a[3] == 'F':
                print('\nFEMALE =', newlist[n])

    def display_by_value(self, value, gender):
        newlist = []
        if gender == 'male':
            for n in self.root[2][0].findall('Item'):
                d = n.get('value')
                if str(value) == d:
                    key = n.get('key')
                    newlist.append(key)
        elif gender == 'female':
            for n in self.root[2][1].findall('Item'):
                d = n.get('value')
                if str(value) == d:
                    key = n.get('key')
                    newlist.append(key)

        #for n in range(len(newlist)):
            #print(newlist[n])
        return newlist

    def display_by_ID(self, Drawable, Texture):
        a = []
        drawID = str(Drawable)
        textID = str(Texture)
        for n in self.gender.findall("Item"):
            key = n.get('key')
            b = []
            b.append(key)
            for i in range(len(b)):
                c = b[i].split('_')
                d = c[::-1]
                #print('c is ', d)
                if d[0] == textID and d[1] == drawID:
                    a.append(key)                            
            b.pop
            
            #value = n.get('value')
            #print(key, ' = ', value)
        
        print(a)
    
        



if __name__ == '__main__':
    p = parse('scriptmetadata', 'male')
    #p.display_by_variation('PLEFT')
    #p.display_by_dlc_and_variation('H4','PEARS')
    #p.display_by_dlc('SUM')
    #p.compare_by_value(2900)
    #list1 = p.display_by_value(2900, 'female')
    #print(list1)

    #a = list1[0].split('_')
    #print(a[::-1])

    p.display_by_ID(11, 7)