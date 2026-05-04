from pyscript import document

gallery_data = [
    {"name": "Christmas", "desc": "Christmas Party 2025!", "img": "679349584_1496754521987076_4145454189393776092_n.jpg"},
    {"name": "CAT Grad", "desc": "Our first Graduation in Junior High!", "img": "CAT Graduation.jpeg"},
    {"name": "Friends :D", "desc": "Friendship is Magic", "img": "unnamed (10).webp"},

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
