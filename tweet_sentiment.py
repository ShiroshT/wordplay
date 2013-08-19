import sys
import json



def dec_dict():
    afinnfile = open("AFINN-111.txt")
    scores = {}                        # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. 
      scores[term] = int(score)        # Convert the score to an integer.
    return scores                      # Print every (term, score) pair in the dictionary




def lines(fp):
    print str(fp.readlines())




def main():
    data_file = open(sys.argv[1])
    scores = dec_dict()
    start_string = lines(data_file)    





if __name__ == '__main__':
    main()
