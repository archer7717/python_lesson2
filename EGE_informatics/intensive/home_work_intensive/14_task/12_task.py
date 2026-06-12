

def tr(ds):
  return sum(x*40**i for i, x in enumerate(ds[::-1]))
m = []
for x in range(40):

  A = tr([7, x, 8, 2, 3, x, 3])
  B = tr([4, 4, 1, x, 4, 3])
  if (A+B) % 39 == 0:
      m.append((A+B) // 39)

print(m[-1]-m[0])