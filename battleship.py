# -*- coding: utf-8 -*-

"""
def guess(record):
    #-All Code Here-
     
    x,y = 0,0
    while True:
        if record.get_status_at(x,y) == Board.Status.EMPTY and x in range(0,10) and y in range(0,10):
            break
        else:
            if record.get_latest() == False :
                x=0
                y=0

            else :

                latest = record.get_latest()

                x = latest['guess']['x'] + 1
                y = latest['guess']['y'] 

                if x == 10:
                    x = 0
                    y = latest['guess']['y'] + 1


    #-All Code End-
    return x,y
"""




"""
def guess(record):
    #-All Code Here-
     
    x,y = 0,0
    while True:
        if record.get_status_at(x,y) == Board.Status.EMPTY and x in range(0,10) and y in range(0,10):
            break
        else:
            if record.get_latest() == False :
#                print "record = false"
                x=0
                y=0

            else :

                latest = record.get_latest()

                x = latest['guess']['x'] + 1
                y = latest['guess']['y'] 

                if x == 10:
                    for i in range(0,10):
                        if record.board[i][y] == -1 :
                            record.data[i]=y

                    if len(record.data) == 0 :
                        x = 0
                        y = latest['guess']['y'] + 1

                    else :
                        x = 0
                        y = latest['guess']['y'] + 1



    print x,y
    #-All Code End-
    return x,y
"""



# -*- coding: utf-8 -*-

def guess(record):
    #-All Code Here-
     
    x,y = 0,0
    while True:
        if record.get_status_at(x,y) == Board.Status.EMPTY and x in range(0,10) and y in range(0,10):
            break
        else:


            ### 첫턴이면 ###

            if record.get_latest() == False :
                x=0
                y=0
                record.data['bomb'] = []


            ###  두번째 턴 이상이고 걸린게 하나도 없으면 ###

            elif len(record.data['bomb']) == 0 and record.get_latest() == True:

                latest = record.get_latest()

                x = latest['guess']['x'] + 1
                y = latest['guess']['y'] 

                if x == 10:
                    for i in range(0,10):
                        if record.board[i][y] == Board.Status.HIT :
                            record.data['bomb'].append([i,y,'vec_y'])

                    if len(record.data) == 0 :
                        x = 0
                        y = latest['guess']['y'] + 1

                    else :
                        x = record.data['bomb'][0][0]
                        y = record.data['bomb'][0][1] + 1

                        del record.data['bomb'][0]
                      



            ### 두번째 턴 이상이고 걸린게 하나라도 있으면 ###

            elif len(record.data['bomb']) != 0 and record.get_latest() == True:


                ### 딕셔너리에서 꺼낸 리스트의 벡터값이 vec_y이면  ###

                if record.data['bomb'][0][2] == 'vec_y' :

                    x = latest['guess']['x']
                    y = latest['guess']['y'] + 1

                    if y == 10:
                        for i in range(record.data['bomb'][0][1],10):
                            if record.board[record.data['bomb'][0][0]][i] == Board.Status.HIT :
                                record.data['bomb'].append([record.data['bomb'][0][0],i,'vec_x'])

                    del record.data['bomb'][0]


                ### 딕셔너리에서 꺼낸 리스트의 벡터값이 vec_x이면  ###

                elif record.data['bomb'][0][2] == 'vec_x' :

                    x = latest['guess']['x'] + 1
                    y = latest['guess']['y'] 

                    if x == 10:
                        for i in range(record.data['bomb'][0][0],10):
                            if record.board[i][record.data['bomb'][0][1]] == Board.Status.HIT :
                                record.data['bomb'].append(i,[record.data['bomb'][0][0],'vec_y'])

                    del record.data['bomb'][0]




               


    #-All Code End-

    return x,y





