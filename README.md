# travel_planner

This is a 2 agent system where one system uses tavily to retrieve information and the other uses langchain to access LLAMA llam to answer the users query throught the retrieved information.
Here the lenght of the retrieved information is limited to keep up with the Ratelimit of the LLAMA api.

What information the agent asks from the user:
Start location
destination
date of travel
budget
extra preferences

An example prompt I gave:
Start location: Mysore
destination: bangalore
date of travel: 28th march
Budget: Medium
extra preferences: Veg food

#Output:
Based on the information from BudgetYourTrip.com, here's a breakdown of the average travel costs for a trip to Bangalore, India:

**Average Daily Cost:**
The average daily cost for a trip to Bangalore can vary depending on your travel style and preferences. However, here are some estimated daily costs:

* Budget: ₹2,500 - ₹3,500 (approximately $35-$50 USD) per day
* Mid-range: ₹4,000 - ₹6,000 (approximately $55-$85 USD) per day
* Luxury: ₹8,000 - ₹12,000 (approximately $110-$170 USD) per day

**Weekly and Monthly Costs:**
Here are some estimated costs for a trip to Bangalore for one week, two weeks, and one month:

* One week:
	+ Budget: ₹17,500 - ₹24,500 (approximately $240-$350 USD)
	+ Mid-range: ₹28,000 - ₹42,000 (approximately $390-$590 USD)
	+ Luxury: ₹56,000 - ₹84,000 (approximately $780-$1,170 USD)
* Two weeks:
	+ Budget: ₹35,000 - ₹49,000 (approximately $490-$690 USD)
	+ Mid-range: ₹56,000 - ₹84,000 (approximately $780-$1,170 USD)
	+ Luxury: ₹112,000 - ₹168,000 (approximately $1,560-$2,340 USD)
* One month:
	+ Budget: ₹70,000 - ₹98,000 (approximately $980-$1,370 USD)
	+ Mid-range: ₹112,000 - ₹168,000 (approximately $1,560-$2,340 USD)
	+ Luxury: ₹224,000 - ₹336,000 (approximately $3,120-$4,680 USD)

**Travel Plan:**
To plan a trip to Bangalore, consider the following:

1. **Accommodation:** Book a hotel or hostel in advance to get the best rates. You can expect to pay around ₹1,500 - ₹3,000 (approximately $20-$40 USD) per night for a budget-friendly option.
2. **Food:** Eat at local restaurants and street food stalls to save money. A meal can cost around ₹100 - ₹200 (approximately $1.50-$3 USD).
3. **Transportation:** Use public transportation or hire a taxi/auto-rickshaw to get around the city. A one-way ticket on public transportation can cost around ₹10 - ₹20 (approximately $0.15-$0.30 USD).
4. **Activities:** Visit popular attractions like the Bangalore Palace, Lalbagh Botanical Garden, and the ISKCON Temple. Entry fees can range from ₹50 - ₹200 (approximately $0.75-$3 USD) per person.
5. **Shopping:** Explore local markets like the Commercial Street and MG Road for souvenirs and shopping. Be prepared to bargain and negotiate prices.

Overall, Bangalore can be a relatively affordable destination, especially for budget-conscious travelers. With some planning and research, you can have a great time exploring the city without breaking the bank.
