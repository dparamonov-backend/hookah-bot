from pydantic import BaseModel

class Kit(BaseModel):
    code: str
    name: str
    price: int

KITS: dict[str, Kit] = {
    "standart": Kit(code = "standart", name = "🥂 Standart", price = 1990),
    "premium": Kit(code = "premium", name ="🍾 Premium", price = 2390 )

}