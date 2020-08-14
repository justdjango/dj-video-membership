
# Video Membership Project

User

## Content via Vimeo

Video
    - vimeo_id

BlogPost
    - title
    - description

Content
    - content: video / blog post / newsletter / podcast
    - data: 
        video: { vimeo_video_id: 372847324 }
        blog post: { title, description, image }
    - Pricing (ManyToMany)

## Subscription via Stripe

Pricing
    - price per month
    - currency
    - id
    - name (basic/pro/business)

Subscription
    - User (FK)
    - stripe_subscription_id
    - status (active / canceled / past_due / trialing)
    - Pricing (FK)
    