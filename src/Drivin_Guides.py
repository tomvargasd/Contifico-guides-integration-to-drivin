from src.ApiRequest import delGuide, creGuide, getDrivId

def createGuide(guides):
    print("Number of new guides is: "+str(len(guides)))
    for guide in guides:
        creGuide(guide)
        

def deleteGuide(guides):
    print("Number of Nulled guides is: "+str(len(guides)))
    for guide in guides:
        driv_id = getDrivId(guide['numero_documento'])
        delGuide(driv_id)
        