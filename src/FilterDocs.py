
#state E:emitido, A:anulado
def filterDocs(state, data, date):
    elements=[]
    for element in data:
        try:
            if element['estado'] == state and element['fecha_emision'] == date:
                elements.append(element)
        except:
            print("skip")
    return elements