from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    
items = {}

# CREATE API
@app.post("/items/")
async def create_item(item: Item):
   item_id = len(items) + 1
   items[item_id] = item
   return {"id": item_id, "item": item}

# READ API
@app.get("/items/{item_id}")
async def get_item(item_id:int):
   return items.get(item_id, {"error": "Item not found"})
   
# UPDATE API
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
   if item_id in items:
       items[item_id] = item
       return {"message": "Item updated", "item": item}
   return {"error": "item not found"}
   
# DELETE API
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
   if item_id in items:
       deleted_item = items.pop(item_id)
       return {"message": "Item deleted", "item": deleted_item}
   return {"error": "Item not found"}


