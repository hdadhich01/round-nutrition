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

All subnutrient functions take in an `int` or `str` argument for `quantity`

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

⚠️ As of `1.1.x` all functions are global with no need for special imports

\*Has a `boolean` parameter of `minimal` to opt for a cleaner UI

## Sources

- [Food and Drug Administration](https://www.fda.gov/files/food/published/Food-Labeling-Guide-%28PDF%29.pdf#page=129)
- [National Dairy Council](https://www.usdairy.com/getmedia/7f24626b-c08b-459a-b964-7a8478c88cd0/dmi%20quick%20reference%20guide_nutrition%20claims%20for%20dairy%20products_2018.pdf.pdf.aspx#page=10)

## Contributing

Make a pull request for any idea/fix you have, or make an issue if you're lazy

## License

[MIT](https://github.com/hdadhich01/round-nutrition/blob/main/LICENSE)
