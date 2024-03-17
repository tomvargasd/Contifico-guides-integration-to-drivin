
def filterDocs(anulado, data):
    elements=[]
    for element in data:
        if element['anulado'] == anulado:
            elements.append(element)
    return elements