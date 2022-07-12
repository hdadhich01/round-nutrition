[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/hdadhich01/round-nutrition/main.svg)](https://results.pre-commit.ci/latest/github/hdadhich01/round-nutrition/main)
![build](https://github.com/hdadhich01/round-nutrition/actions/workflows/build.yml/badge.svg)
[![PyPI](https://img.shields.io/pypi/v/round-nutrition)](https://pypi.org/project/round-nutrition/)

# round-nutrition
A lightweight Python package to round nutritional values for federal compliance with [FDA](https://www.fda.gov/) and [NDC](https://www.usdairy.com/about-us/national-dairy-council) guidelines.
## Example
```py
>>> a, b = Main(), Vitamin()
>>> print([a.tot_carb('0.8g'), b.vitamin_k('125.5 mcg')])
['less than 1 g', '126mcg']
>>> print(a.tot_carb('0.8 g', minimal=True))
'<1g'
```

## Setup
First, install the package with:
```shell
$ pip install round-nutrition
```
Then, import the module with the desired nutrient(s):
```py
from round_nutrition import Main # Vitamin, Mineral, Other
```

## Usage
All subnutrient methods take in an `integer` or `string` argument of `quantity`.
```js
          Main                    Vitamin                  Mineral                  Other
      added_sugars*           biotin                      calcium                  choline
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
      tot_carb*
      tot_fat
      tot_sugars*
      trans_fat
```
*Some functions have an additional `boolean` argument of `minimal` that can be set to `True` for a cleaner user interface implementation. By default, this parameter is set to `False`.

## License
[MIT](https://github.com/hdadhich01/round-nutrition/blob/main/LICENSE)