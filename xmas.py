from random import random
globes = 0.2
c = lambda x: print(x.center(20))
e = lambda: 'o' if random() < globes else '*'
[c(r) for r in 'A-< >-V'.split('-')]
[c(''.join(e() for _ in range(i))) for i in range(3,20,2)]
[c(r) for r in r'| |-| |-_/_|_\_'.split('-')]