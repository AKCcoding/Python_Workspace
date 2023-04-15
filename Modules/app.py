# One way to use a module is to import it
import converter
# This is the other way to import a module but selected functions
from converter import kg_to_lbs
from converter import lbs_to_kg

print(converter.kg_to_lbs(70))
print(converter.lbs_to_kg(154))