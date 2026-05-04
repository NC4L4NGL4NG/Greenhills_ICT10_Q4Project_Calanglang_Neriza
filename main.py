from pyscript import document

gallery_data = [
    {"name": "Christmas", "desc": "Christmas Party 2025!", "img": "679349584_1496754521987076_4145454189393776092_n.jpg"},
    {"name": "CAT Grad", "desc": "Our first Graduation in Junior High!", "img": "CAT Graduation.jpeg"},
    {"name": "#", "desc": "#", "img": "https://i.pinimg.com/1200x/c0/f0/16/c0f0167a545b3e55eded2d51622b17fa.jpg"},
    {"name": "#", "desc": "#", "img": "https://i.pinimg.com/1200x/c0/f0/16/c0f0167a545b3e55eded2d51622b17fa.jpg"},

]

container = document.querySelector("#gallery-container")

for item in gallery_data:
    card = document.createElement("div")
    card.className = "gallery-card"

    card.innerHTML = f"""
        <div class="image-container">
            <img src="{item['img']}" class="card-image">
        </div>
        <div class="card-details">
            <h3 class="card-title">{item['name']}</h3>
            <p class="card-subtitle">{item['desc']}</p>
        </div>
    """
    
    container.appendChild(card)
