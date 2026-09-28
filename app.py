from flask import Flask, render_template

app = Flask(__name__)

MENU = {
    "Fried Chicken": [
        ("1 pc", 69, "Ketchup + Mayonnaise + Maja SP Sauce"),
        ("2 pcs", 139, "Ketchup + Mayonnaise + Maja SP Sauce"),
        ("4 pcs", 269, "Ketchup + Mayonnaise + Maja SP Sauce"),
        ("8 pcs", 529, "Ketchup + Mayonnaise + Maja SP Sauce"),
        ("12 pcs", 779, "Ketchup + Mayonnaise + Maja SP Sauce"),
    ],
    "Burgers": [
        ("Mini Burger", 49, ""),
        ("Burger (Large)", 99, ""),
        ("Burger (Large + Cheese)", 119, ""),
        ("Burger (Double)", 229, ""),
    ],
    "Rolls & Snacks": [
        ("Maja Roll", 159, ""),
        ("Loaded Fries", 199, ""),
        ("Club Sandwich", 119, "Ketchup + Mayonnaise + Maja SP Sauce"),
        ("Veg. Sandwich", 99, "Ketchup + Mayonnaise + Maja SP Sauce"),
        ("Chicken Popcorn (Medium)", 89, ""),
        ("Chicken Popcorn (Large)", 139, ""),
    ],
    "Combos": [
        ("Rider Combo", 299, "Jumbo Burger + Fried Chicken + Pepsi 250 ml"),
        ("Lunch Meal Combo", 289, "Maja Role + Fried Chicken + Bun + Pepsi 250 ml"),
        ("Kids Meal Combo", 149, "Mini Burger + Popcorn Medium + Fries 50 g + Pepsi 250 ml"),
        ("Loaded Meal Combo", 309, "Loaded Fries + Soft Drink"),
        ("Loaded Couple Meal Combo", 599, "Loaded Fries + Maja Role + 2 Soft Drinks"),
        ("Couple Combo", 449, "2 Fried Chicken + French Fries + 2 Mini Burgers + 2 Soft Drinks"),
        ("Family Combo", 529, "8 Fried Chicken + 4 Buns + French Fries"),
        ("Super Family Combo", 899, "12 Fried Chicken + 6 Buns + Large Popcorn + French Fries"),
        ("Party Combo", 1899, "20 Fried Chicken + 6 Burgers + French Fries + 10 Buns"),
    ],
    "Drinks": [
        ("Mojito", 130, "Passion Fruit / Water Melon / Lemon Mint / Blue Ocean"),
    ],
}

@app.route("/")
def home():
    return render_template("index.html", menu=MENU)

if __name__ == "__main__":
    app.run(debug=True)
