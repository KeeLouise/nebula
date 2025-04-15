class User:
    def __init__(self, full_name, email, password):
        self.full_name = full_name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "email": self.email,
            "password": self.password
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            full_name=data.get("full_name"),
            email=data.get("email"),
            password=data.get("password")
        )
    
class Post:
     def __init__(self, id, author, content, created_at, likes=0, comments=None):
      self.id = id
      self.author = author
      self.content = content
      self.created_at = created_at
      self.likes = likes
      self.comments = comments or []

     def to_dict(self):
        return {
            "id": self.id,
            "author": self.author,
            "content": self.content,
            "created_at": self.created_at,
            "likes": self.likes,
            "comments": self.comments
        }

     @classmethod
     def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            author=data.get("author"),
            content=data.get("content"),
            created_at=data.get("created_at"),
            likes=data.get("likes", 0),
            comments=data.get("comments", [])
        )
    
class Product:
     def __init__(self, id, name, price, image_url):
        self.id = id
        self.name = name
        self.price = price
        self.image_url = image_url

     def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "image_url": self.image_url
        }
     
     @classmethod
     def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            name=data.get("name"),
            price=data.get("price"),
            image_url=data.get("image_url")
        )

class Cart:
    def __init__(self):
        self.items = []  # list of product objects - kr 15/04/2025

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product_id):
        self.items = [item for item in self.items if item.id != product_id]

    def total_price(self):
        return sum(item.price for item in self.items)

    def to_dict(self):
        return [item.to_dict() for item in self.items]