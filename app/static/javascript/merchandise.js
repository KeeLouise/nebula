// Hamburger nav script - KR 15/04/2025
document.addEventListener("DOMContentLoaded", () => {
    const hamburger = document.querySelector(".hamburger-menu");
    const mobileNav = document.querySelector("#mobile-nav");
  
    if (hamburger && mobileNav) {
      hamburger.addEventListener("click", () => {
        mobileNav.classList.toggle("active");
      });
    }
  
    // Cart script - KR 15/04/2025
    const cartToggle = document.getElementById("cart-toggle");
    const cartDropdown = document.getElementById("cart-dropdown");
    const cartItemsList = document.getElementById("cart-items");
    const cartTotal = document.getElementById("cart-total");
    const cartCount = document.getElementById("cart-count");
    const addToCartButtons = document.querySelectorAll(".add-to-cart-btn");
    const checkoutBtn = document.getElementById("checkout-btn");
  
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
        li.style.display = "flex";
        li.style.alignItems = "center";
        li.style.marginBottom = "10px";
  
        const img = document.createElement("img");
        img.src = item.image_url || "";
        img.alt = item.name;
        img.style.width = "40px";
        img.style.height = "40px";
        img.style.objectFit = "cover";
        img.style.marginRight = "10px";
        img.style.borderRadius = "6px";
  
        const text = document.createElement("span");
        text.textContent = `${item.name} - €${item.price.toFixed(2)}`;
  
        const removeBtn = document.createElement("button");
        removeBtn.classList.add("remove-btn");
        removeBtn.innerHTML = '<i class="bi bi-x-circle"></i>';
        removeBtn.setAttribute("aria-label", "Remove item");
        removeBtn.style.marginLeft = "10px";
  
        removeBtn.addEventListener("click", () => {
          cart.splice(index, 1);
          saveCart();
        });
  
        li.appendChild(img);
        li.appendChild(text);
        li.appendChild(removeBtn);
        cartItemsList.appendChild(li);
      });
  
      cartTotal.textContent = total.toFixed(2);
      cartCount.textContent = cart.length;
    }
  
    addToCartButtons.forEach((button) => {
      button.addEventListener("click", () => {
        const productCard = button.closest(".product");
        const title = productCard.querySelector(".product-title")?.textContent || "Unknown";
        const priceText = productCard.querySelector(".product-price")?.textContent.replace("€", "") || "0";
        const price = parseFloat(priceText);
        const image = productCard.querySelector("img")?.getAttribute("src") || "";
  
        const item = {
          name: title,
          price: price,
          image_url: image
        };
  
        cart.push(item);
        saveCart();
      });
    });
  
    if (cartToggle) {
      cartToggle.addEventListener("click", () => {
        cartDropdown.classList.toggle("show");
      });
    }
  
    if (checkoutBtn) {
      checkoutBtn.addEventListener("click", () => {
        window.location.href = "/checkout"; // Leads to 404 route - KR 15/04/2025
      });
    }
  
    // Load cart on page load - KR 15/04/2025
    updateCartUI();
  });