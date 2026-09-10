---
document_id: nari18_product_reviews
title: Nari18 Product Reviews
category: products
company: Nari18
---

# Nari18 Product Reviews

## 1. Overview

Nari18 product pages include customer ratings and reviews that provide feedback about products, stitching, fabric quality, styling, service, and the overall shopping experience.

Reviews are associated with individual products and should not automatically be treated as feedback for the entire Nari18 catalog.

## 2. Product Ratings

The Nari18 catalog displays a star rating and review count for individual products.

Current catalog examples include products showing ratings such as:

- 5.0 with 13 reviews
- 5.0 with 16 reviews
- 5.0 with 17 reviews
- 5.0 with 18 reviews
- 5.0 with 19 reviews

These values are dynamic and can change as new reviews are submitted.

## 3. Customer Review Topics

Published reviews on Nari18 products commonly discuss:

- Fabric and product quality
- Design and appearance
- Fit and stitching
- Styling guidance
- Customer service
- Boutique experience
- Personalized tailoring
- Overall satisfaction

For example, published customer feedback mentions appreciation for Nari18's designs, fabric quality, styling assistance, stitching, and attention to detail.

## 4. Review Moderation

Nari18 states that:

- Reviews are checked before they appear publicly.
- One review is allowed per account per product.
- Customers can submit a review through the product page after signing in.

Therefore, the visible reviews represent **published/approved customer feedback**, rather than an unmoderated collection of comments.

## 5. Product-Level Reviews

Reviews should always be connected to the specific product on which they were published.

For example, a customer review for a particular Chanderi, Silk, Cotton, or Organza suit should not be presented as a review of every product made from that fabric.

The RAG assistant should preserve this product-level context.

## 6. How to Use Reviews in RAG Responses

When a customer asks:

**"What do customers say about this product?"**

The assistant can summarize the published reviews associated with that specific product.

When a customer asks:

**"Is this product highly rated?"**

The assistant should provide the current product rating and review count if available.

Example:

> "This product currently has a 5.0 rating based on 18 reviews."

The rating and review count must be taken from the current product data because they can change.

## 7. Important RAG Rules

- Never invent customer reviews.
- Never attribute a review to the wrong product.
- Never treat one customer's opinion as an objective product fact.
- Do not generalize a product review to the entire Nari18 catalog.
- Use the current product page for the latest rating and review count.
- Clearly distinguish customer opinions from verified product specifications.
- Summarize reviews rather than presenting them as guaranteed product characteristics.

## 8. RAG Usage

Use this document for questions such as:

- Does this product have reviews?
- What are customers saying about this suit?
- What is the product's current rating?
- How many reviews does this product have?
- Do customers mention the stitching or fabric quality?

For **current ratings, review counts, or specific customer comments**, retrieve the individual product page because review information changes over time.