from ApiRequest import delGuide, creGuide, getDrivId

def createGuide(guides):
    print("create guide function")
    created = 0
    skiped = 0
    for guide in guides:
        created_guide = creGuide(guide)
        if created_guide['success']:
            created+=1
        else:
            skiped+=1
    
    return {
        'guides_created': created,
        'guides_skiped': skiped
    }

def deleteGuide(guides):
    deleted = 0
    skiped = 0
    for guide in guides:
        driv_id = getDrivId(guide['id'])
        deleted_guide = delGuide(driv_id)
        if deleted_guide['success']:
            deleted+=1
        else:
            skiped+=1
    
    return {
        'guides_deleted': deleted,
        'guides_skiped': skiped
    }
