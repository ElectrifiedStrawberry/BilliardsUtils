from __future__ import annotations

import billiardsutils.util.casts as casts
import billiardsutils.util.limits as limits

_RAND_MAX = 0xFFFF
_RAND_SHIFT = 16
_RAND_SEED_STEP = 0x10DCD # 69069

class Random:
	__slots__ = ('seed',)

	seed: int

	def __init__(self, seed: int) -> None:
		self.seed = seed

	def next_f32(self) -> float:
		value: int = (_RAND_MAX & (self._calc() >> _RAND_SHIFT)) % limits.U16_MAX
		return casts.u32_to_f32(value) / casts.u32_to_f32(_RAND_MAX + 1)

	def _calc(self) -> int:
		self.seed = (self.seed * _RAND_SEED_STEP + 1) % limits.U32_MAX
		return self.seed
