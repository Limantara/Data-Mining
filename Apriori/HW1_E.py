#!/usr/bin/python

import sys 

"""
	CS249 - HW1 
	Edwin Limantara - 004888537
"""

"""
	Convert an input file to a list of values
"""
def parse_file(filename):
	with open(filename) as f:
		rows = f.readlines()
	return [row.strip().split(',') for row in rows] 
	
"""
	Get frequent itemsets of size k
"""
def get_1_frequent_itemsets(min_threshold, transactions):
	counter = dict()
	
	# Count support for 1-items
	for i in range(len(transactions)):
		for j in range(len(transactions[i])):
			item = transactions[i][j]
			if item in counter:
				counter[item] += 1
			else:
				counter[item] = 1
				
	# Only take items with support >= min_threshold
	for item, count in counter.items():
		if not (count >= min_threshold):
			counter.pop(item)
			
	return counter.keys()
	
""" 
	Generate next candidates from a given frequent itemsets
	(this is the self-join part of the Apriori Algorithm)
"""
def generate_next_candidates(frequent_itemsets):
	candidates = list()
	
	n = len(frequent_itemsets)
	for i in range(n):
		for j in range(i+1, n):
			f1 = frequent_itemsets[i]
			f2 = frequent_itemsets[j]
			if (f1[:-1] is f2[:-1]) and (f1[-1:] is not f2[-1:]):
				candidates.append(f1[:-1] + f1[-1:] + f2[-1:])
			
	return candidates
	
def get_frequent_itemsets(min_threshold, candidates, transactions):
	frequent_itemsets = []
	counter = dict()
	
	# init counter
	for candidate in candidates:
		counter[candidate] = 0
	
	for candidate in candidates:
		for transaction in transactions:
#			print "Checking if ", set(transaction), " contains ", set(list(candidate)), "... ", set(list(candidate)) <= set(transaction)
			if set(list(candidate)) <= set(transaction):
				counter[candidate] += 1
				if(counter[candidate] >= min_threshold):
					frequent_itemsets.append(candidate)
					break
		
	return frequent_itemsets
		
"""
	Find frequent patterns using Apriori algorithm
"""
def apriori(min_threshold, transactions):
	frequent_patterns = set()
	L = dict() # Frequent itemset of size k
	C = dict() # Candidate itemset of size k
	
	k = 1
	L[k] = get_1_frequent_itemsets(int(min_threshold), transactions)
	frequent_patterns = frequent_patterns.union(L[k])
#	print "L[", k, "]: ", L[k]
	while len(L[k]) != 0:
		C[k+1] = generate_next_candidates(L[k])
#		print "C[", k+1, "]: ", C[k+1]
		L[k+1] = get_frequent_itemsets(int(min_threshold), C[k+1], transactions)
#		print "L[", k+1, "]: ", L[k+1]
		frequent_patterns = frequent_patterns.union(L[k+1])
		k += 1
		
	return list(frequent_patterns)
	
"""
	Main
"""
min_threshold = sys.argv[1];
filename = sys.argv[2];

print 'Min Threshold : ', min_threshold
print 'Input File    : ', filename

print '\nFinding all frequent itemsets in the file...\n'

transactions = parse_file(filename);
print 'Transaction DB: ', transactions
print 'Frequent items: ', apriori(min_threshold, transactions)
