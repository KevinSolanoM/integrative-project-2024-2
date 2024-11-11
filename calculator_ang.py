from connect2bt import envio2esp


def receptionDate(base:int,valor2:int,mode:str):
    if mode=='disp':
        sendVal('7',0,0)

    elif mode=='rec':
        sendVal('1',0,0)
    elif mode=='rec1':
        if valor2==1:
            sendVal('1',1,0)
        elif valor2==2:
            sendVal('1',2,0)
    elif mode=='rec_gat':
        sendVal('6',0,0)
    elif mode=='manual':
        sendVal('3',base,valor2)

    elif mode=='auto':#---no esta listo para su uso
        #mode a cambiar, 
        sendVal('0',base,66)
    else:
        print('error:in recptionDate')


def sendVal(modo:str,base:int,canon:int):
    if base<10:
        baseStr = '00'+str(base) 
    elif base<=99:
        baseStr = '0'+str(base)
    else:
        baseStr = str(base)
    
    if canon<10:
        canonStr='0'+str(canon)
    else:
        canonStr=str(canon)

    inf = modo+baseStr+canonStr
    print(inf)
    envio2esp(inf+'\n')