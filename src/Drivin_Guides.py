from ApiRequest import delGuide, creGuide, getDrivId

def createGuide(guides):
    print("create guide function")
    for guide in guides:
        creGuide(guide)

def deleteGuide(guides):
    for guide in guides:
        driv_id = getDrivId(guide['id'])
        delGuide(driv_id)
