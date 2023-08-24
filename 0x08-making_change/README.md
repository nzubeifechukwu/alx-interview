## Make change
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

- Prototype: `def makeChange(coins, total)`
- `coins` is a list of available coin denominations; each denomination is infinite
- Return
	- least number of coins equal to `total` if `total` is at least 1 and achievable by given coins
	- 0 if `total` less than 1
	- -1 if no combination of given coins can achieve `total`

