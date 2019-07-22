
"""
Solving RCPSP problems with gurobi, limited to J30 test case dataset

The data sets is from  http://www.om-db.wi.tum.de/psplib/data.html

Existing optimal solution can be find in  https://people.eng.unimelb.edu.au/pstuckey/rcpsp/

"""

import gurobi_RCPSP
import Gantt_chart_draw

def main(file):
     start,finish=gurobi_RCPSP.Gurobi_RSPSP_J30(file)
     Gantt_chart_draw.Gantt_chart(start,finish)

if __name__ == '__main__':
    main(file="./data/j30.sm/j304_7.sm")