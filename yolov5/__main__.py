from .train import run as train
from .detect import run as detect
from .val import run as val

import fire


def main():
  fire.Fire({
      'train': train,
      'detect': detect,
      'val': val
  })

if __name__=="__main__":
    main()