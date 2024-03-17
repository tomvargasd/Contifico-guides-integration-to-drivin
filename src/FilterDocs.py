
#state E:emitido, A:anulado
def filterDocs(state, data):
    elements=[]
    for element in data:
        if element['estado'] == state:
            elements.append(element)
    return elements