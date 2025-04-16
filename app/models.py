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
    def __init__(self, id, author, content, created_at, likes=0, comments=None, liked_by=None):
        self.id = id
        self.author = author
        self.content = content
        self.created_at = created_at
        self.likes = likes
        self.comments = comments or []
        self.liked_by = liked_by or set()  # Store user emails or IDs

    def toggle_like(self, user_email):
        if user_email in self.liked_by:
            self.liked_by.remove(user_email)
            self.likes -= 1
        else:
            self.liked_by.add(user_email)
            self.likes += 1

    def to_dict(self):
        return {
            "id": self.id,
            "author": self.author,
            "content": self.content,
            "created_at": self.created_at,
            "likes": self.likes,
            "comments": self.comments,
            "liked_by": list(self.liked_by)
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id"),
            author=data.get("author"),
            content=data.get("content"),
            created_at=data.get("created_at"),
            likes=data.get("likes", 0),
            comments=data.get("comments", []),
            liked_by=set(data.get("liked_by", []))
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

product_list = [
    Product("p1", "NEBULA T-Shirt - White", 25.00, "images/desktop-store-whitetshirt.webp"),
    Product("p2", "NEBULA T-Shirt - Black", 25.00, "images/desktop-store-blacktshirt.webp"),
    Product("p3", "NEBULA Sweat - White", 45.00, "images/desktop-store-whitesweatshirt.webp"),
    Product("p4", "NEBULA Sweat - Black", 45.00, "images/desktop-store-blacksweatshirt.webp"),
    Product("p5", "NEBULA Baseball Cap", 15.00, "images/desktop-store-blackhat.webp"),
    Product("p6", "NEBULA Keyring - Black", 5.00, "images/desktop-store-keyring.webp"),
    Product("p7", "NEBULA Mug - White", 10.00, "images/desktop-store-whitemug.webp"),
    Product("p8", "NEBULA Mug - Black", 10.00, "images/desktop-store-blackmug.webp"),
]