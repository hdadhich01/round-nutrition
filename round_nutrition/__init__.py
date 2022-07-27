from .main import Main
from .mineral import Mineral
from .other import Other
from .vitamin import Vitamin

__version__ = "1.0.9"
__doc__ = "Round nutritional values for federal compliance with FDA and NDC guidelines. More information available at https://github.com/hdadhich01/round-nutrition."
__all__ = ["Main", "Mineral", "Other", "Vitamin"]
__sources__ = [
    "https://www.fda.gov/files/food/published/Food-Labeling-Guide-%28PDF%29.pdf",
    "https://www.usdairy.com/~/media/usd/public/dmi-quick-reference-guide_nutrition-claims-for-dairy-products_2018.pdf",
]
