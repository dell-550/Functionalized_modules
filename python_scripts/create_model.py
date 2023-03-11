import sys

import sqlacodegen.main

if __name__ == '__main__':
    genstr = 'sqlacodegen --noviews --outfile models.py mysql+pymysql://root:luo12138@localhost:3306/dbmysql' \
             '*'
    temp = genstr.split(' ')[1:]
    genarr = []
    for a_temp in temp: 
        if not a_temp == '':
            genarr.append(a_temp)
    sys.argv.extend(genarr)
    sqlacodegen.main.main()