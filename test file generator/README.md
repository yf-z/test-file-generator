# Test Files Generator for Voting System

Yifan Zhang

29/03/2020

## Dependencies

```python
import os
import names
import secrets
import pandas as pd
import glob
import random
import functools
from typing import List, NamedTuple
from typing import List
import math
```

## Reference

* [helpers.py](<https://github.com/jontingvold/pyrankvote/blob/master/pyrankvote/helpers.py>)
* [models.py](<https://github.com/jontingvold/pyrankvote/blob/master/pyrankvote/models.py>)
* [multiple_seat_ranking_methods.py](<https://github.com/jontingvold/pyrankvote/blob/master/pyrankvote/multiple_seat_ranking_methods.py>)
* Change the droop quota formula in multiple_seat_ranking_methods.py

##Create Test Files for Plurality Election

```python
create_plurality_test_files(numCandidate, numBallots, testFileName, numFiles)
```

| Parameter    | type                                                         |
| ------------ | ------------------------------------------------------------ |
| numBallots   | The number of ballots; **integer**                           |
| numCandidate | The number of candidates; **integer**                        |
| testFileName | The directory name that all test files will be stored in; **string** |
| numFiles     | The number of test files user wants; **integer**             |

### Example

```python
create_plurality_test_files(10, 1000, 'test10', 5)
```

![](/Users/zhangyifan/Desktop/grad/2020 spring/CSCI 5801 (002) Software Engineering/project #1/test files generator/plurality result 0.png)

#### Result

**Data**

```
Frank Higgins,Nick Owen,Eliza Thompson,Angelo Luciano,Richard Shelton,Eugenia Smith,Alice Broe,Tim Brady,Vito Duet,Rebekah Coleman
,,,,1,,,,,
,,,,,1,,,,
1,,,,,,,,,
,,,,1,,,,,
,,,,,,,,,1
,,,,,,1,,,
,1,,,,,,,,
,,1,,,,,,,
,,,,1,,,,,
,,,,,,,,,1
,,1,,,,,,,
```

**Election Result**

```
Winners:
Richard Shelton : 0.117
Losers:
Frank Higgins : 0.113
Nick Owen : 0.085
Eliza Thompson : 0.113
Angelo Luciano : 0.096
Eugenia Smith : 0.097
Alice Broe : 0.083
Tim Brady : 0.082
Vito Duet : 0.108
Rebekah Coleman : 0.106
```

##Create Test Files for STV Election

```python
create_STV_test_files(numCandidate, numBallots, numSeats, testFileName, numFiles)
```

| Parameters   | Type                                                         |
| ------------ | ------------------------------------------------------------ |
| numCandidate | The number of candidates; **integer**                        |
| numBallots   | The number of ballots; **integer**                           |
| numSeats     | The number of seats; **integer**                             |
| testFileName | The directory name that all test files will be stored in; **string** |
| numFiles     | The number of test files user wants; **integer**             |

### Example

```
create_STV_test_files(10, 1000, 2, 'test11', 5)
```

![](/Users/zhangyifan/Desktop/grad/2020 spring/CSCI 5801 (002) Software Engineering/project #1/test files generator/STV result 0.png)

####Result

**Data**

```
Shawna Combs,Edith Santos,Leona Morton,Joan Briggs,Sally Costley,Margaret West,Frank Williams,Samuel Thomas,Garnett Carson,Fred Fye
5,2,8,6,3,7,,9,4,1
7,8,1,9,4,6,,3,2,5
2,3,,,,1,6,5,,4
4,2,3,,,7,6,,5,1
1,,3,5,4,7,,,2,6
7,2,6,,1,5,4,8,3,9
8,7,9,6,3,2,1,4,5,
2,6,5,3,1,8,,7,9,4
6,2,9,,3,1,8,5,4,7
2,4,8,,7,1,9,6,5,3
7,6,2,5,1,,,3,4,
```

**Election Result**

```
ROUND 1
Candidate         Votes  Status
--------------  -------  --------
Leona Morton        138  Hopeful
Joan Briggs         122  Hopeful
Shawna Combs        118  Hopeful
Garnett Carson      111  Hopeful
Edith Santos        107  Hopeful
Frank Williams      105  Hopeful
Sally Costley       102  Hopeful
Margaret West       102  Hopeful
Samuel Thomas        95  Rejected
Fred Fy               0  Rejected

ROUND 2
Candidate         Votes  Status
--------------  -------  --------
Leona Morton        158  Hopeful
Joan Briggs         136  Hopeful
Shawna Combs        129  Hopeful
Garnett Carson      122  Hopeful
Edith Santos        120  Hopeful
Margaret West       115  Hopeful
Frank Williams      114  Hopeful
Sally Costley       106  Rejected
Samuel Thomas         0  Rejected
Fred Fy               0  Rejected

ROUND 3
Candidate         Votes  Status
--------------  -------  --------
Leona Morton        173  Hopeful
Joan Briggs         150  Hopeful
Shawna Combs        149  Hopeful
Garnett Carson      135  Hopeful
Frank Williams      134  Hopeful
Edith Santos        132  Hopeful
Margaret West       127  Rejected
Sally Costley         0  Rejected
Samuel Thomas         0  Rejected
Fred Fy               0  Rejected

ROUND 4
Candidate         Votes  Status
--------------  -------  --------
Leona Morton        200  Hopeful
Joan Briggs         171  Hopeful
Shawna Combs        169  Hopeful
Edith Santos        155  Hopeful
Garnett Carson      155  Hopeful
Frank Williams      150  Rejected
Margaret West         0  Rejected
Sally Costley         0  Rejected
Samuel Thomas         0  Rejected
Fred Fy               0  Rejected

ROUND 5
Candidate         Votes  Status
--------------  -------  --------
Leona Morton        223  Hopeful
Joan Briggs         203  Hopeful
Shawna Combs        198  Hopeful
Edith Santos        191  Hopeful
Garnett Carson      184  Rejected
Frank Williams        0  Rejected
Margaret West         0  Rejected
Sally Costley         0  Rejected
Samuel Thomas         0  Rejected
Fred Fy               0  Rejected
Blank votes           1  Rejected

ROUND 6
Candidate         Votes  Status
--------------  -------  --------
Leona Morton        272  Hopeful
Edith Santos        242  Hopeful
Shawna Combs        242  Hopeful
Joan Briggs         239  Rejected
Garnett Carson        0  Rejected
Frank Williams        0  Rejected
Margaret West         0  Rejected
Sally Costley         0  Rejected
Samuel Thomas         0  Rejected
Fred Fy               0  Rejected
Blank votes           5  Rejected

ROUND 7
Candidate         Votes  Status
--------------  -------  --------
Leona Morton        349  Elected
Edith Santos        319  Hopeful
Shawna Combs        315  Hopeful
Joan Briggs           0  Rejected
Garnett Carson        0  Rejected
Frank Williams        0  Rejected
Margaret West         0  Rejected
Sally Costley         0  Rejected
Samuel Thomas         0  Rejected
Fred Fy               0  Rejected
Blank votes          17  Rejected

FINAL RESULT
Candidate         Votes  Status
--------------  -------  --------
Leona Morton     334.00  Elected
Edith Santos     324.93  Elected
Shawna Combs     321.19  Rejected
Joan Briggs        0.00  Rejected
Garnett Carson     0.00  Rejected
Frank Williams     0.00  Rejected
Margaret West      0.00  Rejected
Sally Costley      0.00  Rejected
Samuel Thomas      0.00  Rejected
Fred Fy            0.00  Rejected
Blank votes       19.88  Rejected
```

## Run STV Election with Test Files

```python
STV(dirName, numSeats)
```

| Parameters | Type                                                         |
| ---------- | ------------------------------------------------------------ |
| dirName    | The name of the directory where all test files are stored in; **string** |
| numSeats   | The number of seats; **integer**                             |

### Example

```python
STV('test6', 2)
```

![](/Users/zhangyifan/Desktop/grad/2020 spring/CSCI 5801 (002) Software Engineering/project #1/test files generator/Run STV Election with Test Files.png)

#### Result

**Election Result**

```
ROUND 1
Candidate           Votes  Status
----------------  -------  --------
Solomon Warren        129  Hopeful
Alex Crouse           118  Hopeful
Neil Gentry           118  Hopeful
Gail Wilson           115  Hopeful
Tom Hopkins           113  Hopeful
Terri Mcclure         112  Hopeful
Shirley Hoagland      110  Hopeful
Ernest Carillo        104  Hopeful
Jayne Nguyen           81  Rejected
Miriam Ro               0  Rejected

ROUND 2
Candidate           Votes  Status
----------------  -------  --------
Solomon Warren        140  Hopeful
Neil Gentry           131  Hopeful
Alex Crouse           131  Hopeful
Gail Wilson           124  Hopeful
Terri Mcclure         121  Hopeful
Shirley Hoagland      119  Hopeful
Tom Hopkins           119  Hopeful
Ernest Carillo        115  Rejected
Jayne Nguyen            0  Rejected
Miriam Ro               0  Rejected

ROUND 3
Candidate           Votes  Status
----------------  -------  --------
Solomon Warren        161  Hopeful
Alex Crouse           151  Hopeful
Neil Gentry           146  Hopeful
Terri Mcclure         138  Hopeful
Gail Wilson           138  Hopeful
Tom Hopkins           137  Hopeful
Shirley Hoagland      129  Rejected
Ernest Carillo          0  Rejected
Jayne Nguyen            0  Rejected
Miriam Ro               0  Rejected

ROUND 4
Candidate           Votes  Status
----------------  -------  --------
Alex Crouse           181  Hopeful
Solomon Warren        179  Hopeful
Neil Gentry           165  Hopeful
Tom Hopkins           163  Hopeful
Terri Mcclure         159  Hopeful
Gail Wilson           153  Rejected
Shirley Hoagland        0  Rejected
Ernest Carillo          0  Rejected
Jayne Nguyen            0  Rejected
Miriam Ro               0  Rejected

ROUND 5
Candidate           Votes  Status
----------------  -------  --------
Alex Crouse           209  Hopeful
Solomon Warren        208  Hopeful
Neil Gentry           205  Hopeful
Terri Mcclure         192  Hopeful
Tom Hopkins           186  Rejected
Gail Wilson             0  Rejected
Shirley Hoagland        0  Rejected
Ernest Carillo          0  Rejected
Jayne Nguyen            0  Rejected
Miriam Ro               0  Rejected

ROUND 6
Candidate           Votes  Status
----------------  -------  --------
Alex Crouse           257  Hopeful
Solomon Warren        253  Hopeful
Neil Gentry           252  Hopeful
Terri Mcclure         237  Rejected
Tom Hopkins             0  Rejected
Gail Wilson             0  Rejected
Shirley Hoagland        0  Rejected
Ernest Carillo          0  Rejected
Jayne Nguyen            0  Rejected
Miriam Ro               0  Rejected
Blank votes             1  Rejected

FINAL RESULT
Candidate           Votes  Status
----------------  -------  --------
Neil Gentry           329  Elected
Alex Crouse           328  Elected
Solomon Warren        324  Rejected
Terri Mcclure           0  Rejected
Tom Hopkins             0  Rejected
Gail Wilson             0  Rejected
Shirley Hoagland        0  Rejected
Ernest Carillo          0  Rejected
Jayne Nguyen            0  Rejected
Miriam Ro               0  Rejected
Blank votes            19  Rejected
```

## Restrictions

1. Test files with ties need to be created manually
2. When there is multiple test files for STV Election, reading these files in different order will also result in different election results.
3. The STV algorithm is different for redistributing :(.
