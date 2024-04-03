'''
A program to test the random number generator to see if positions are unique.
'''
import billiardsutils.rp.utl
import billiardsutils.util.limits as limits


def _get_ball_variations(random: billiardsutils.rp.utl.Random) -> tuple[float, ...]:
	l: list[float] = []
	for _ in range(9 * 2): # ball count * dimensions (X and Z)
		l.append(random.next_f32())
	return tuple(l)


def _get_dup_count(dict: dict[int, list[int]]) -> int:
	return len([k for k, v in dict.items() if len(v) > 1])


def _main():
	# All potential ball positions are on the order of 288 GB. In order to find
	# potential collisions, hash each position tuple and put *that* in the list
	# along with the other seeds.
	hash_to_seeds: dict[int, list[int]] = {}
	for i in range(limits.U32_MAX):
		if i % 100_000 == 0: print(str(i) + " (" + str(_get_dup_count(hash_to_seeds)) + " found duplicates so far)...")
		random: billiardsutils.rp.utl.Random = billiardsutils.rp.utl.Random(i)
		hashed: int = hash(_get_ball_variations(random))
		if hashed in hash_to_seeds:
			hash_to_seeds[hashed].append(i)
		else:
			hash_to_seeds[hashed] = [i]
	for dict_h, dict_s in hash_to_seeds.items():
		if len(dict_s) > 1:
			print(str(dict_h) + " [" + ', '.join([str(x) for x in dict_s]) + ']')



if __name__ == "__main__":
	_main()
