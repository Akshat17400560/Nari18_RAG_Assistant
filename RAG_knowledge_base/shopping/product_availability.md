---
document_id: nari18_product_availability
title: Nari18 Product Availability
category: shopping
company: Nari18
---

# Nari18 Product Availability

## 1. Overview

Nari18's product availability is **dynamic and product-specific**. Products can be available for purchase, temporarily sold out, or unavailable for a particular size or variant.

The Nari18 catalog currently contains more than 100 unstitched suit listings across multiple fabric categories, and individual products display their current purchasing status directly on the catalog or product page. The catalog currently shows **115 products under the "All fabrics" filter**, although this count can change as products are added, removed, sold out, or reorganized.

A customer should always check the **current individual product page** before assuming that a product is available.

---

# 2. Availability Statuses Used by Nari18

Nari18 currently uses several visible purchase states.

### In Stock

When a product page displays **"In stock"**, the product is currently available for purchase.

Example:

**Classic Ivory / Soft Cream Organza Suit**

- ₹4,679
- Current status: In stock
- Add to cart available
- Buy Now available

### Add to Cart

An **"Add to cart"** button generally indicates that the customer can currently add the product to the shopping cart.

### Buy Now

A **"Buy now"** button allows the customer to proceed directly toward purchasing the product.

When both **Add to cart** and **Buy now** are visible, the product is generally currently purchasable.

### Sold Out

When the product page displays **"Sold out"**, the product is currently unavailable for purchase.

Example:

**Warm Mustard-Beige Suit**

- ₹3,210
- Current status: Sold out
- Sold-out button displayed

---

# 3. Product Page Is the Primary Availability Source

For RAG responses, the individual product page should normally be treated as the strongest source for current availability.

A product can appear in:

- Homepage sections
- New-arrival sections
- Best-seller sections
- Fabric collections
- Catalog listings

and still be sold out.

For example, **Banarasi Cotton Unstitched Suit** appears in the current catalog and homepage, but its current product listing displays **Sold out**.

### RAG rule

Do not interpret a product appearing on a collection or homepage as proof that it is currently available.

---

# 4. Available Product Example

Current Nari18 product pages show products that can be purchased immediately.

### Classic Ivory / Soft Cream Organza Suit

Current snapshot:

- Price: ₹4,679
- Listed price: ₹7,100
- Status: In stock
- Add to cart: Available
- Buy now: Available
- Custom tailoring option: Book a Tailor

This is an example of a currently purchasable product.

---

# 5. Sold-Out Product Example

### Warm Mustard-Beige Suit

Current snapshot:

- Price: ₹3,210
- Listed price: ₹5,890
- Status: Sold out
- Purchase button: Sold out

The product may still have:

- Product images
- Product description
- Reviews
- Price information
- Product details

but this does not mean that it can currently be ordered.

---

# 6. Collection Pages Can Contain Sold-Out Products

Nari18's collection pages can show a mixture of available and unavailable products.

For example, the current Organza collection contains:

### Available

**Classic Ivory / Soft Cream Organza Suit**

- ₹4,679
- Add to cart
- Buy now

### Sold Out

**Crimson Red Organza Unstitched Suit**

- ₹4,995
- Sold out

### Sold Out

**Olive Green Embroidered Organza Silk Unstitched Suit**

- ₹5,949
- Sold out

Therefore, customers should verify each product individually rather than assuming the entire collection is available.

---

# 7. Availability and New Arrivals

Nari18's New Arrivals section contains recently curated products, but "New Arrival" does not automatically mean that every product is available.

Current New Arrivals include products such as:

- Midnight Chevron Muse Muslin Unstitched Suit
- Royal Teal Muse Muslin Unstitched Suit
- Rustic Petals Muslin Unstitched Suit
- Heritage Arch Muslin Unstitched Suit

Several currently display **Add to cart** and **Buy now**, indicating that they are currently purchasable.

However, availability can change after the catalog is updated.

---

# 8. Best-Seller Does Not Mean In Stock

Nari18 also has a **Best-Selling Unstitched Suits** section.

A product can remain visible in a best-seller section even when it becomes unavailable.

For example:

**Banarasi Cotton Unstitched Suit**

appears in Nari18's best-selling section but currently displays **Sold out**.

### RAG rule

Never answer:

> "The product is available because it is a bestseller."

Instead, verify the current product status.

---

# 9. Availability by Fabric

Availability differs between fabric categories.

The current Nari18 catalog shows approximately:

| Fabric Category | Current Catalog Count |
|---|---:|
| Silk | 19 |
| Organza | 8 |
| Tissue | 11 |
| Muslins | 12 |
| Cotton Suits | 31 |
| Linen Suits | 3 |
| Georgette | 9 |
| Chanderi | 3 |
| Crape | 2 |
| Chiffon | 3 |
| Lycra Net | 1 |
| Mul-Cotton | 13 |

The catalog currently shows **115 products under All fabrics**. These numbers are dynamic and should not be treated as permanent inventory quantities.

---

# 10. Availability Is Not the Same as Catalog Count

The number shown beside a fabric category represents products currently listed under that category.

It should **not automatically be interpreted as the number of products physically available for immediate purchase**.

For example:

- A collection may contain 8 Organza products.
- Some may be in stock.
- Others may be sold out.

Therefore:

**Catalog count ≠ available inventory count.**

---

# 11. Product Availability vs Stock Quantity

Nari18 does not always expose an exact remaining inventory quantity to customers.

A product page may simply indicate:

- In stock
- Add to cart
- Sold out

Even when customer activity information is displayed, such as "people bought this" or "viewing this piece now," this should not be interpreted as the exact remaining stock quantity.

For example, a product page may show how many people purchased or are currently viewing a product while separately showing its availability status.

### RAG rule

Never invent an exact remaining stock quantity unless Nari18 explicitly publishes it.

---

# 12. Product Availability and Variants

Some Nari18 products have colour or other variants.

The current homepage states that product pages list:

- Colour variants
- Pricing
- Availability

Therefore, availability can potentially differ by variant.

### Example interpretation

If a product has:

- Ivory variant
- Black variant
- Blue variant

the customer should select the required variant and verify its current availability.

Do not assume that all variants are simultaneously available.

---

# 13. Availability of Stitched Products

Nari18 also offers stitched products.

Stitched products can use a different purchasing interface from unstitched products.

For example, the current catalog shows a **Classic Beige Slub Cotton Co-ord Set** with a **"Select size"** control rather than simply displaying the same purchase interface used for every unstitched suit.

For stitched or size-based products:

1. Open the product.
2. Select the required size.
3. Check whether the selected size is available.
4. Select quantity.
5. Add the product to cart or use Buy Now if available.

Do not assume that the product is available in every size.

---

# 14. Size Availability

For products requiring size selection, availability can depend on the selected size.

Possible situations include:

- Product available in all displayed sizes
- Some sizes available
- A particular size unavailable
- Product completely sold out

The live product page should be used to determine the current size-specific status.

### RAG rule

Never tell a customer:

> "Size M is available"

unless the current product page or checkout explicitly confirms it.

---

# 15. Custom Stitching and Availability

Nari18 offers custom stitching/tailoring on applicable unstitched products.

However:

**Custom stitching does not mean that a sold-out product becomes available.**

The fabric/product must first be available for purchase.

For example:

- Product in stock → customer may be able to order and request tailoring where offered.
- Product sold out → custom tailoring cannot normally be initiated for that unavailable product unless Nari18 separately confirms a special arrangement.

Current Nari18 pages show **Book a Tailor** on product pages, but this should not be interpreted as a guarantee that every sold-out product can be custom stitched.

---

# 16. Sold-Out Products

When a product is sold out, customers may still be able to view:

- Product name
- Images
- Product description
- Fabric information
- Product reviews
- Previous/current displayed price
- Promotional information

The presence of these details does not mean the product is orderable.

### Example

**Elegant Georgette Chikankari Suit**

currently displays:

- ₹8,109
- Sold out
- Sold-out purchase button

while the product page remains fully accessible.

---

# 17. What to Do When a Product Is Sold Out

If a customer wants a sold-out product:

1. Check whether another colour/variant is available.
2. Browse the same fabric category.
3. Search for a similar design.
4. Check New Arrivals.
5. Check the full catalog.
6. Contact Nari18 for product availability or alternatives.

Nari18's website provides contact/WhatsApp support for product and tailoring assistance.

Do not promise a restock date unless Nari18 explicitly provides one.

---

# 18. Restock Information

A sold-out product does not automatically have a known restock date.

### RAG rule

Never invent statements such as:

- "It will be back next week."
- "It will restock tomorrow."
- "Nari18 is manufacturing more."
- "You will receive a restock notification."

unless the current Nari18 website or customer-support communication explicitly confirms it.

If the customer asks when a product will return, recommend contacting Nari18 directly.

---

# 19. Availability Can Change Quickly

Product availability is dynamic because customers can purchase products while another customer is browsing.

A product can change from:

**In stock → Sold out**

without the product page itself changing in every catalog section immediately.

Similarly, a product may become available again after inventory is updated.

Therefore, current availability should always be verified close to the time of purchase.

---

# 20. Homepage Availability

Nari18's homepage contains several merchandising sections, including:

- New Arrivals
- Best Sellers
- Fabric collections
- Featured products

Products shown on the homepage may have different availability states.

For example, the current homepage shows **Midnight Chevron Muse Muslin Unstitched Suit** with Add to cart/Buy now, while **Banarasi Cotton Unstitched Suit** is shown with Sold out.

### RAG rule

Homepage visibility should not be treated as an availability guarantee.

---

# 21. Catalog Availability

The catalog provides a broader view of Nari18 products.

The current catalog:

- Shows product cards.
- Shows prices.
- Shows discount percentages.
- Shows purchase controls.
- Allows filtering by fabric.
- Allows filtering by price.
- Contains multiple catalog pages.

The current catalog displays **Page 1 of 10** in the current snapshot.

A customer can use the catalog to discover products, but should open the product page before relying on availability.

---

# 22. Availability and Price Are Separate

A product can be:

- Discounted and in stock
- Discounted and sold out
- Full price and in stock
- Full price and sold out

For example, **Crimson Red Organza Unstitched Suit** currently shows a 41% discount but is sold out.

Therefore:

**Discount ≠ availability.**

A low price or large discount does not mean that the product can currently be ordered.

---

# 23. Availability and Reviews

A product can have reviews even when it is currently sold out.

For example, current sold-out products such as Banarasi Cotton and Elegant Georgette Chikankari display customer ratings/review counts alongside their sold-out status.

### RAG rule

Do not use:

- Review count
- Rating
- Number of buyers
- Product popularity

as evidence that the product is currently available.

---

# 24. Availability and Offers

A sold-out product page can still display promotional information.

For example, the current sold-out Elegant Georgette Chikankari page still shows:

- Welcome Sale
- WELCOME5
- ₹50 prepaid offer
- Free wardrobe styling

even though the product itself is sold out.

### Important RAG rule

**Promotional visibility does not override product availability.**

If a product is sold out, do not tell the customer that they can use the displayed offer to purchase it.

---

# 25. Availability and Payment

A product's payment options do not prove that the product is available.

For example, sold-out product pages can still display:

- COD available
- Razorpay
- UPI/cards

alongside a Sold out button.

Therefore:

**Payment method availability ≠ product availability.**

The product's purchase status should be checked first.

---

# 26. Availability and Shipping

A product being listed on Nari18 does not necessarily mean that it can currently be shipped.

A sold-out product cannot normally proceed through a new purchase workflow.

For available products, shipping eligibility should still be checked at checkout based on the current delivery information and applicable shipping rules.

Nari18 currently promotes pan-India delivery on its product pages.

---

# 27. Recommended Availability Check

Before telling a customer that a product is available:

### Step 1
Find the exact product.

### Step 2
Open the current product page.

### Step 3
Check the displayed status:

- In stock
- Add to cart
- Buy now
- Sold out

### Step 4
If there are variants, select the required variant.

### Step 5
If there is a size selector, select the required size.

### Step 6
Check whether the purchase button remains available.

### Step 7
Only then provide the availability answer.

---

# 28. Availability Answer Examples

### Product is available

> Yes, the product is currently shown as in stock and can be added to the cart.

### Product is sold out

> This product is currently sold out on Nari18. You can check similar products or contact Nari18 for availability information.

### Variant uncertain

> The product is listed, but availability depends on the selected variant. Please select the required colour/variant on the product page to confirm.

### Size uncertain

> The product is available for selection, but the availability of your specific size should be checked on the product page.

---

# 29. Similar Product Recommendations

When the requested product is sold out, recommendations should prioritize:

1. Same fabric
2. Similar colour
3. Similar occasion
4. Similar price range
5. Similar design/detailing
6. Currently available products

For example, if an Organza product is sold out, suggest currently available Organza products before recommending an unrelated fabric.

The recommendation must be based on **current availability**, not merely catalog presence.

---

# 30. Availability vs Product Variations

Nari18 may display multiple colour images or variants for the same product.

The assistant should distinguish:

- Product listing
- Product variant
- Colour option
- Size option
- Actual availability

Do not infer availability from an image.

A colour shown in the product gallery does not automatically mean that the colour is currently orderable.

---

# 31. Important Dynamic Data

The following information should be treated as dynamic:

- In-stock status
- Sold-out status
- Available variants
- Available sizes
- Product count
- Product price
- Discount
- Stock quantity
- Product visibility
- New arrivals
- Collection membership

The current product page or checkout should take priority over an older stored answer.

---

# 32. Current Availability Examples

The following are examples from the current Nari18 website snapshot:

### Currently shown as available

**Classic Ivory / Soft Cream Organza Suit**

- ₹4,679
- In stock
- Add to cart
- Buy now

**Rangrez Rouge Cotton Suit Set**

- ₹2,699
- In stock
- Add to cart
- Buy now

**Mustard Yellow Floral Printed Suit**

- ₹4,699
- In stock
- Add to cart

### Currently shown as sold out

**Warm Mustard-Beige Suit**

- ₹3,210
- Sold out

**Elegant Georgette Chikankari Suit**

- ₹8,109
- Sold out

**Banarasi Cotton Unstitched Suit**

- ₹2,854
- Sold out

**Crimson Red Organza Unstitched Suit**

- ₹4,995
- Sold out

These are examples from the current website snapshot and are **not permanent inventory records**.

---

# 33. RAG Retrieval Rules

1. Treat product availability as dynamic.
2. Prefer the exact current product page for availability questions.
3. Use collection/catalog pages for discovery, not as the final availability authority.
4. "Add to cart" generally indicates that the product is currently purchasable.
5. "Buy now" generally indicates that the product is currently purchasable.
6. "In stock" indicates current availability.
7. "Sold out" means the product is currently unavailable for purchase.
8. Do not infer availability from homepage visibility.
9. Do not infer availability from collection membership.
10. Do not infer availability from New Arrival status.
11. Do not infer availability from Best Seller status.
12. Do not infer availability from reviews.
13. Do not infer availability from number of buyers.
14. Do not infer availability from current discounts.
15. Do not infer availability from payment methods.
16. Do not infer availability from product images.
17. Do not invent remaining inventory quantities.
18. Do not invent restock dates.
19. Do not promise that a sold-out product will return.
20. For colour variants, verify the selected variant.
21. For size-based products, verify the selected size.
22. Do not assume every colour or size is available.
23. Custom tailoring does not make a sold-out product available.
24. A "Book a Tailor" option does not override a sold-out status.
25. A sold-out product may still display offers; do not interpret those offers as purchase availability.
26. Product price and availability are separate fields.
27. Product discounts and availability are separate fields.
28. Payment availability and product availability are separate fields.
29. If a product is sold out, suggest similar currently available products where appropriate.
30. When answering a time-sensitive availability question, use the latest available website information.
31. If the customer asks about a future restock, direct them to Nari18 rather than inventing a date.
32. If availability is unclear, say that it needs to be confirmed on the live product page.
33. Do not claim that an exact stock quantity is available unless Nari18 explicitly publishes it.
34. Catalog counts are dynamic and should not be treated as permanent inventory totals.
35. Current checkout/product-page status takes priority over older RAG content.

---

# 34. Short RAG Answers

**Is this Nari18 product available?**  
Check the current individual product page. "In stock" or an active Add to cart/Buy now option indicates that it is currently purchasable.

**What does Sold out mean?**  
It means the product is currently unavailable for purchase.

**Can a sold-out product still appear on Nari18?**  
Yes. Nari18 can continue displaying sold-out products in the catalog, homepage, best-seller sections, or collection pages.

**Can I buy a product just because it appears in the catalog?**  
Not necessarily. Open the product page and check its current availability status.

**Does Add to cart mean the product is available?**  
Generally yes. An active Add to cart/Buy now option indicates that the product is currently purchasable.

**Does a discount mean the product is available?**  
No. A product can be heavily discounted and still be sold out.

**Can I custom stitch a sold-out product?**  
Normally, the product/fabric must first be available. A Book a Tailor option does not override a sold-out status.

**Can I get a sold-out product restocked?**  
Nari18 may be able to provide availability information, but do not assume a restock date unless Nari18 confirms one.

**Are all colours of a product available?**  
Not necessarily. Availability can depend on the selected colour or variant.

**Are all sizes available for stitched products?**  
Not necessarily. Check the selected size on the current product page.

**Does being a bestseller mean the product is in stock?**  
No. For example, Nari18's current Banarasi Cotton bestseller is shown as sold out.

**How do I know if a product is currently available?**  
Open the exact Nari18 product page and check for "In stock," "Add to cart," or "Buy now." If it says "Sold out," it is currently unavailable.

**Can availability change after I add an item to my cart?**  
Yes. Inventory is dynamic, so the final checkout should be treated as the latest purchasing state.

**Are Nari18 catalog counts exact stock quantities?**  
No. Fabric/category counts represent listed products, not necessarily the exact number of units physically available.