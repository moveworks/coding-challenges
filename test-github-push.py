import stripe
stripe.api_key = "sk_live_4eC39HqLyjWDarjtT1zdp7dcTYooMQauvdEDq54NiTphI7jx"

stripe.Charge.create(
  amount=2000,
  currency="usd",
  source="tok_amex", # obtained with Stripe.js
  description="Charge for jenny.rosen@example.com"
)
