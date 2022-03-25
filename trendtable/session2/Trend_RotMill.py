button9 = event.source.selected
if button9 == 1:
    tagpens = event.source.parent.getComponent('Easy Chart').tagPens
    for row in range(tagpens.rowCount):
        subplot = tagpens.getValueAt(row, "Subplot")
        if subplot == 9:
            tagpens = system.dataset.setValue(tagpens, row, "Hidden", 0)
    event.source.parent.getComponent('Easy Chart').tagPens = tagpens
    calcpens = event.source.parent.getComponent('Easy Chart').calcPens
    for row in range(calcpens.rowCount):
        subplot = calcpens.getValueAt(row, "Subplot")
        if subplot == 9:
            calcpens = system.dataset.setValue(calcpens, row, "Hidden", 0)
    event.source.parent.getComponent('Easy Chart').calcPens = calcpens
else:
    tagpens = event.source.parent.getComponent('Easy Chart').tagPens
    for row in range(tagpens.rowCount):
        subplot = tagpens.getValueAt(row, "Subplot")
        if subplot == 9:
            tagpens = system.dataset.setValue(tagpens, row, "Hidden", 1)
    event.source.parent.getComponent('Easy Chart').tagPens = tagpens

    calcpens = event.source.parent.getComponent('Easy Chart').calcPens
    for row in range(calcpens.rowCount):
        subplot = calcpens.getValueAt(row, "Subplot")
        if subplot == 9:
            calcpens = system.dataset.setValue(calcpens, row, "Hidden", 1)
    event.source.parent.getComponent('Easy Chart').calcPens = calcpens
