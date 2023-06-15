import constValues
from popUp import open_popup

def convertToColumn(lst, columns):
    res_col = {columns[i]: lst[i] for i in range(0, len(lst))}
    return res_col

def toPrice(value):
   return "{:.2f}".format(value)

def addItem(tree, itemName):
  productName = constValues.products[itemName]['name']
  for item in tree.get_children():
      if productName == tree.item(item)['values'][0]:
        oldItem = convertToColumn(tree.item(item)['values'], constValues.columns)
        newPrice = constValues.products[itemName]['price'] * (float(oldItem['count']) + 1)
        newData = (oldItem['product'], float(oldItem['count']) + 1, toPrice(newPrice))
        tree.item(item, values=newData)
        return
  tree.insert("", 'end', values=(constValues.products[itemName]['name'], 1, toPrice(constValues.products[itemName]['price'])))

def getTotalPrice(tree):
  total = 0
  for item in tree.get_children():
    total += float(convertToColumn(tree.item(item)['values'], constValues.columns)['price'])
  return f'Podsumowanie: {toPrice(total)} zł'

def item_selected(app, tree):
  if len(tree.selection()) > 1:
     return

  selectedItem = tree.selection()[0]
  newValue = open_popup(app, convertToColumn(tree.item(selectedItem)['values'], constValues.columns))

  selectedKey = ''
  for key, value in constValues.products.items():
    if value['name'] == tree.item(selectedItem)['values'][0]:
      selectedKey = key
      break

  if newValue == 0:
    tree.delete(selectedItem)
  elif newValue > 0:
    oldItem = convertToColumn(tree.item(selectedItem)['values'], constValues.columns)
    newPrice = constValues.products[selectedKey]['price'] * newValue
    newData = (oldItem['product'], newValue, toPrice(newPrice))
    tree.item(selectedItem, values=newData)