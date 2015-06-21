#!/usr/bin/env python
###############################################################################
#
# https://en.wikipedia.org/wiki/Kirkman's_schoolgirl_problem
# http://gurmeet.net/puzzles/kirkmans-schoolgirl-problem/
#
###############################################################################

import math
import sys

#------------------------------------------------------------------------------
#
# If we represent the solution in three dimensional matrix?
#
# [
#     [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ],  // 1st day
#     [ [1, 4, 7], [2, 5, 8], [3, 6, 9] ],  // 2nd day
#     ...                                   // ...
# ]
#
#------------------------------------------------------------------------------

girls = range(1, 10)

COLS = len(girls) / 3
ROWS = {
    9: 4,
    15: 7
}[len(girls)]

#------------------------------------------------------------------------------

def C(n, k): return math.factorial(n) / (math.factorial(k)*math.factorial(n-k))

#------------------------------------------------------------------------------
# Group combinations
#------------------------------------------------------------------------------

def dogroups():

    groups = []

    for a in girls:
        for b in girls:
            if b <= a: continue
            for c in girls:
                if c <= a: continue
                if c <= b: continue
                groups.append([a, b, c])

    return groups

#------------------------------------------------------------------------------
# Row combinations
#------------------------------------------------------------------------------

rows = []

def dorows(groups, row = []):
    
    def isUnique(row):
        
        def test(row, stored):
            for group in row:
                if group not in stored: return True
            return False
        
        global rows
        for stored in rows:
            if not test(row, stored): return False
        return True
        
    if len(row) == COLS:
        if isUnique(row):
            if (len(rows) % 100) == 0:
                print "Rows...:", len(rows), "\r",
                sys.stdout.flush()
            rows.append(row)
    
    def validrow(group, row):
        for girl in group:
            for team in row:
                if girl in team: return False
        return True
    
    for group in groups:
        if validrow(group, row):
            dorows(groups, row + [ group ])
            # print row + [ group ]

groups = dogroups()
print "Groups.:", len(groups)

dorows(groups)
print "Rows...:", len(rows)
print "--------"

#------------------------------------------------------------------------------
# From groups, choose a set so that any girl is grouped two other only once
#------------------------------------------------------------------------------

solutions = []

def recurse(rows, solution = []):

    #--------------------------------------------------------------------------
    # Do we already have solution?
    #--------------------------------------------------------------------------
    
    if len(solution) == ROWS:
        global solutions
        
        def isSame(solution, stored):
            for row in solution:
                if row not in stored: return False
            return True

        def isUnique(solution):
            for stored in solutions:
                if isSame(solution, stored): return False
            return True
            
        if isUnique(solution):
            solutions.append(solution)
            print "Solution %d:" % len(solutions)
            for row in solution:
                print "    ", row
        # sys.exit(0)
        return
        
    #--------------------------------------------------------------------------
    # Who have been paired already?
    #--------------------------------------------------------------------------

    paired = {}
    for girl in girls:
        paired[girl] = {}
        paired[girl][girl] = True

    for row in solution:
        for group in row:
            for girl in group:
                for mate in group:
                    paired[girl][mate] = True

    #--------------------------------------------------------------------------
    # Check valid rows for solution
    #--------------------------------------------------------------------------

    def alreadypaired(group):
        a, b, c = group
        return (a in paired[b]) or (a in paired[c]) or (b in paired[c])

    def validrow(row):
        for group in row:
            if alreadypaired(group): return False
        return True

    #--------------------------------------------------------------------------
    # Pick groups and try them out
    #--------------------------------------------------------------------------

    for row in rows:
        if not validrow(row): continue

        recurse(rows, solution + [row])

#------------------------------------------------------------------------------

print "Girls..:", girls
print "Matrix.:", COLS, "x", ROWS

recurse(rows)

