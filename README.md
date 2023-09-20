[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/hdadhich01/round-nutrition/main.svg)](https://results.pre-commit.ci/latest/github/hdadhich01/round-nutrition/main)
[![PyPI](https://img.shields.io/pypi/v/round-nutrition)](https://pypi.org/project/round-nutrition/)
[![Downloads](https://pepy.tech/badge/round-nutrition)](https://pepy.tech/project/round-nutrition)

# round-nutrition

A lightweight Python package to round nutritional values for federal compliance with [FDA](https://www.fda.gov/) and [NDC](https://www.usdairy.com/about-us/national-dairy-council) guidelines

```pycon
>>> print([total_carb('0.8g'), vitamin_k('125.5 mcg')])
['less than 1g', '126mcg']
>>> print(total_carb('0.8 g', minimal=True))
<1g
```

## Installation

Install the package:

```bash
pip install round-nutrition
```

Import the module:

```py
from round_nutrition import * # or specific functions
```

## Usage

All subnutrient functions take in an `int` or `str` argument for `quantity`.

```js
         General                   Vitamin                  Mineral                  Other
      added_sugars*           biotin                      calcium                   choline
      calories                folate                      chromium
      cholesterol*            niacin                      copper
      dietary_fiber*          pantothenic_acid            iodine
      insoluble_fiber*        riboflavin                  iron
      mono_fat                thiamine                    magnesium
      other_carb*             vitamin_a                   manganese
      poly_fat                vitamin_b12                 molybdenum
      potassium               vitamin_b6                  potassium
      protein*                vitamin_c                   phosphorus
      sat_fat                 vitamin_d                   selenium
      sodium                  vitamin_e                   zinc
      soluble_fiber*          vitamin_k
      sugar_alcohol*
      total_carb*
      total_fat
      total_sugars*
      trans_fat
```

⚠️ As of `1.1.x` all functions have been made external with no need for object instantiation

\*Some functions have a `boolean` parameter of `minimal` to opt for a cleaner user interface implementation. By default, its argument is set to `False`

## Contributing

Make a pull request for any idea/fix you have, or make an issue if you're lazy

## License

[MIT](https://github.com/hdadhich01/round-nutrition/blob/main/LICENSE)
