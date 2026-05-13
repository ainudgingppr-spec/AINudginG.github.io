python
import random
def calculate_score(product, preferences):
"""
根据 Study 2 规则计算推荐分数
"""                      
# 1. 价格匹配度 (PriceFit)
price_diff = abs(product['price'] - preferences['budget'])
if preferences['price_sensitivity'] == 'high':
price_fit = max(0, 1 - (price_diff / preferences['budget']))
elif preferences['price_sensitivity'] == 'medium':
price_fit = 0.7 + random.uniform(0, 0.3)
else: # low
price_fit = 0.9 + random.uniform(0, 0.1)       
# 2. 可持续性匹配度 (SustainabilityMatch)
if preferences['sustainability_importance'] == 'high':
    sustainability_fit = product['sustainability_score'] / 10.0
elif preferences['sustainability_importance'] == 'medium':
    sustainability_fit = 0.5
else:  # low
    sustainability_fit = 0.2

# 3. 兴趣匹配度 (InterestMatch)
if product['category'] == preferences['product_interest']:
    interest_fit = 1.0
else:
    interest_fit = 0.3

# 总分计算 (权重：价格30%，可持续40%，兴趣30%)
total_score = (price_fit * 0.3) + (sustainability_fit * 0.4) + (interest_fit * 0.3)

return round(total_score, 2)
