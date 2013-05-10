def queens(n=8, state=()):
  for pos in range(num):
    if not conflict(state, pos):
      if len(state) == n-1:
        yield (pos,)
      else:
        for result in queens(n, state + (pos,)):
          yield (pos,) + result
