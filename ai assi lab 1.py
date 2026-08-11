def next_sum_sq_digits(n: int) -> int:
	"""Return sum of squares of digits of n."""
	return sum(int(d) * int(d) for d in str(n))


def is_happy(n: int) -> bool:
	"""Check if n is a happy number using cycle detection (Floyd's algorithm)."""
	if n <= 0:
		return False
	slow = n
	fast = n
	while True:
		slow = next_sum_sq_digits(slow)
		fast = next_sum_sq_digits(next_sum_sq_digits(fast))
		if slow == fast:
			break
	return slow == 1


def generate_happy(count: int):
	"""Generate first `count` happy numbers (count >= 1)."""
	found = 0
	n = 1
	while found < count:
		if is_happy(n):
			yield n
			found += 1
		n += 1


if __name__ == "__main__":
	import sys

	try:
		k = int(sys.argv[1]) if len(sys.argv) > 1 else 20
	except ValueError:
		k = 20

	for i, h in enumerate(generate_happy(k), start=1):
		print(f"{i}: {h}")

