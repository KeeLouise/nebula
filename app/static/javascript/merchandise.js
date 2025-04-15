//Cart script - KR 15/04/2025

document.addEventListener("DOMContentLoaded", () => {
  const cartToggle = document.getElementById("cart-toggle");
  const cartDropdown = document.getElementById("cart-dropdown");
  const cartItemsList = document.getElementById("cart-items");
  const cartTotal = document.getElementById("cart-total");
  const cartCount = document.getElementById("cart-count");
  const addToCartButtons = document.querySelectorAll(".add-to-cart-btn");

  let cart = JSON.parse(localStorage.getItem("cart")) || [];

  function saveCart() {
    localStorage.setItem("cart", JSON.stringify(cart));
    updateCartUI();
  }

  function updateCartUI() {
    cartItemsList.innerHTML = "";
    let total = 0;

    cart.forEach((item, index) => {
      total += item.price;

      const li = document.createElement("li");
      li.textContent = `${item.name} - €${item.price.toFixed(2)}`;

      const removeBtn = document.createElement("button");
      removeBtn.textContent = "❌";
      removeBtn.style.marginLeft = "10px";
      removeBtn.addEventListener("click", () => {
        cart.splice(index, 1);
        saveCart();
      });

      li.appendChild(removeBtn);
      cartItemsList.appendChild(li);
    });

    cartTotal.textContent = total.toFixed(2);
    cartCount.textContent = cart.length;
  }

  addToCartButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const productCard = button.closest(".product");
      const title = productCard.querySelector(".product-title").textContent;
      const priceText = productCard.querySelector(".product-price").textContent.replace("€", "");
      const price = parseFloat(priceText);

      const item = {
        name: title,
        price: price
      };

      cart.push(item);
      saveCart();
    });
  });

  cartToggle.addEventListener("click", () => {
    console.log("Cart button clicked");
    cartDropdown.classList.toggle("show");
    console.log("Dropdown classes:", cartDropdown.className);
  });

  // Initial load - KR 15/04/2025
  updateCartUI();
});