"""dict={"mike":[11, 22, 33],"John":"55 44 33"}
print(dict['mike'])
scores=dict['mike']"""
import re

regex_pattern = r"M{,3}[(C{,3})(CD)(D)(DC)(DCC)(DCCC)(CM)][(X{,3})(XL)(L)(LX)(LXX)(LXXX)(XC)][I{,3}(IV)(V)(VI)(VII)(VIII)(IX)]"	# Do not delete 'r'.

import re
res=re.match(regex_pattern, "MCCXXIV")
print(res)
